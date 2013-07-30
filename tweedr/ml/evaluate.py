import os
import argparse
import logging
from colorama import Fore

from tweedr.lib import bifurcate, Counts
from tweedr.lib.text import gloss
from tweedr.models import DBSession, TokenizedLabel, Label
from tweedr.ml import crf
from tweedr.ml.features import all_feature_functions, featurize

logger = logging.getLogger(__name__)


def evaluate(test_proportion, max_data, model_filepath):
    logger.debug('%d labels', DBSession.query(Label).count())
    for label in DBSession.query(Label):
        logger.debug('  %s = %s', label.id, label.text)

    # e.g., tokenized_label =
    # <TokenizedLabel dssg_id=23346 token_start=13 token_end=16
    #    tweet=Tornado Kills 89 in Missouri. http://t.co/IEuBas5 token_type=i18 token= 89 id=5>
    tokenized_labels = DBSession.query(TokenizedLabel).limit(max_data).all()
    test, train = bifurcate(tokenized_labels, test_proportion, shuffle=True)
    logger.info('Training on %d, testing on %d', len(train), len(test))

    totals = Counts()
    tagger = crf.Tagger.from_path_or_data(train, all_feature_functions, model_filepath=model_filepath)
    logger.debug('CRF model saved to %s', model_filepath)
    for tokenized_label in test:
        tokens = tokenized_label.tokens
        gold_labels = tokenized_label.labels
        tokens_features = featurize(tokens, all_feature_functions)

        predicted_labels = list(tagger.tag_raw(tokens_features))
        alignments = zip(tokens, gold_labels, predicted_labels)
        print '-' * 80
        print gloss(alignments,
            prefixes=(Fore.WHITE, Fore.YELLOW, Fore.BLUE),
            postfixes=(Fore.RESET, Fore.RESET, Fore.RESET))

        counts = Counts()
        for gold_label, predicted_label in zip(gold_labels, predicted_labels):
            counts.comparisons += 1
            if gold_label != 'None':
                if predicted_label == gold_label:
                    counts.true_positives += 1
                else:
                    counts.false_negatives += 1

            if gold_label == 'None':
                if predicted_label == gold_label:
                    counts.true_negatives += 1
                else:
                    counts.false_positives += 1

            # if gold_label != 'None' and predicted_label != 'None':
            #     # non_null_partial_matches:
            #     #   the number of items that anything but None for both gold and predicted
            #     counts.non_null_partial_matches += 1
            #     if gold_label == predicted_label:
            #         counts.non_null_exact_matches += 1
            # if gold_label == predicted_label:
            #     counts.exact_matches += 1

        totals.add(counts)

    logger.debug('totals: %r', totals)

    precision = float(totals.true_positives) / (totals.true_positives + totals.false_positives)
    recall = float(totals.true_positives) / (totals.true_positives + totals.false_negatives)
    fscore = 2 * (precision * recall / (precision + recall))

    logger.debug('Precision: %0.4f', precision)
    logger.debug('Recall: %0.4f', recall)
    logger.debug('F-score: %0.4f', fscore)

    # TODO: list top tokens for each label type


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Train CRFSuite on data from the QCRI MySQL database',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--test-proportion',
        type=float, default=0.1, help='The proportion of the total data to test on')
    parser.add_argument('--max-data',
        type=int, default=10000, help='Maximum data points to train and test on')
    parser.add_argument('--model-path',
        default='/tmp/crfsuite-ml-example.model')
    parser.add_argument('--crfsuite-version',
        action='store_true', help='Print the active crfsuite version')
    opts = parser.parse_args()

    if opts.crfsuite_version:
        print 'CRFSuite v%s' % crf.version
    else:
        if os.path.exists(opts.model_path):
            logger.info('Removing %s', opts.model_path)
            os.remove(opts.model_path)
        evaluate(opts.test_proportion, opts.max_data, opts.model_path)