'''
This file, schema.py, is generated by reflect.py but may have small manual
modifications. It should only require regeneration when the database schema
changes. It does not provide much past what the following snippet does, except
that it doesn't require database calls to reflect the database on start up.

    class Something(Base):
        __table__ = Table('somethings', metadata, autoload=True)

from schema import (
    DamageClassification,
    TokenizedLabel,
    UniformSample,
    Label,
    KeywordSample,
    Tweet,
)
'''

from sqlalchemy import Column
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base

from tweedr.models.metadata import metadata


class BaseMixin(object):
    def __json__(self):
        '''This method serves to both clone the record (copying its values)
        as well as filter out the special sqlalchemy key (_sa_instance_state)
        '''
        return dict((k, v) for k, v in self.__dict__.items() if k != '_sa_instance_state')

    def __unicode__(self):
        type_name = self.__class__.__name__
        pairs = [u'%s=%s' % (k, v) for k, v in self.__json__().items()]
        return u'<{type_name} {pairs}>'.format(type_name=type_name, pairs=u' '.join(pairs))

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return str(self)

Base = declarative_base(metadata=metadata, cls=BaseMixin)


class DamageClassification(Base):
    __tablename__ = 'DamageClassification'
    id = Column(mysql.INTEGER(display_width=11), primary_key=True)
    DSSG_ID = Column(mysql.INTEGER(display_width=11))
    Tweet = Column(mysql.TEXT())
    Infrastructure = Column(mysql.TINYINT(display_width=1))
    Casualty = Column(mysql.TINYINT(display_width=1))
    mturk_code = Column(mysql.TEXT())
    which_sample = Column(mysql.VARCHAR(length=10))
    is_extracted = Column(mysql.INTEGER(display_width=1))


class TokenizedLabel(Base):
    __tablename__ = 'tokenized_labels'
    id = Column(mysql.INTEGER(display_width=20), primary_key=True)
    dssg_id = Column(mysql.INTEGER(display_width=100))
    tweet = Column(mysql.VARCHAR(length=500))
    token_start = Column(mysql.INTEGER(display_width=50))
    token_end = Column(mysql.INTEGER(display_width=50))
    token_type = Column(mysql.VARCHAR(length=500))
    token = Column(mysql.VARCHAR(length=500))
    mturk_code = Column(mysql.VARCHAR(length=50))
    which_sample = Column(mysql.VARCHAR(length=10))


class UniformSample(Base):
    __tablename__ = 'uniform_sample'
    id = Column(mysql.INTEGER(display_width=20), primary_key=True)
    dssg_id = Column(mysql.INTEGER(display_width=20))
    pwd = Column(mysql.VARCHAR(length=500))
    text = Column(mysql.VARCHAR(length=500))
    is_extracted = Column(mysql.INTEGER(display_width=11))
    is_classified = Column(mysql.INTEGER(display_width=11))
    type_sample = Column(mysql.VARCHAR(length=10))


class Label(Base):
    __tablename__ = 'labels'
    id = Column(mysql.VARCHAR(length=10), primary_key=True)
    text = Column(mysql.VARCHAR(length=100))


class KeywordSample(Base):
    __tablename__ = 'keyword_sample'
    id = Column(mysql.INTEGER(display_width=20), primary_key=True)
    dssg_id = Column(mysql.INTEGER(display_width=20))
    pwd = Column(mysql.VARCHAR(length=500))
    text = Column(mysql.VARCHAR(length=500))
    is_extracted = Column(mysql.INTEGER(display_width=11))
    is_classified = Column(mysql.INTEGER(display_width=11))
    type_sample = Column(mysql.VARCHAR(length=10))


class Tweet(Base):
    __tablename__ = 'tweets'
    dssg_id = Column(mysql.INTEGER(display_width=20), primary_key=True)
    pwd = Column(mysql.VARCHAR(length=500))
    _unit_id = Column(mysql.VARCHAR(length=500))
    _golden = Column(mysql.VARCHAR(length=500))
    _unit_state = Column(mysql.VARCHAR(length=500))
    _trusted_judgment = Column(mysql.VARCHAR(length=500))
    _last_jugment_at = Column(mysql.VARCHAR(length=500))
    choose_one = Column(mysql.VARCHAR(length=500))
    choose_oneconfidence = Column(mysql.VARCHAR(length=500))
    choose_one_gold = Column(mysql.VARCHAR(length=500))
    predicted = Column(mysql.VARCHAR(length=500))
    text_no_rt = Column(mysql.VARCHAR(length=500))
    tweet = Column(mysql.VARCHAR(length=500))
    _trusted_judgments = Column(mysql.VARCHAR(length=500))
    _last_judgment_at = Column(mysql.VARCHAR(length=500))
    source = Column(mysql.VARCHAR(length=500))
    type_of_advice_or_caution = Column(mysql.VARCHAR(length=500))
    type_of_advice_or_cautionconfidence = Column(mysql.VARCHAR(length=500))
    what = Column(mysql.VARCHAR(length=500))
    when_ = Column(mysql.VARCHAR(length=500))
    where_ = Column(mysql.VARCHAR(length=500))
    category = Column(mysql.VARCHAR(length=500))
    id = Column(mysql.VARCHAR(length=500))
    retweetcount = Column(mysql.VARCHAR(length=500))
    screenname = Column(mysql.VARCHAR(length=500))
    source_gold = Column(mysql.VARCHAR(length=500))
    text = Column(mysql.VARCHAR(length=500))
    type_of_advice_or_caution_gold = Column(mysql.VARCHAR(length=500))
    userid = Column(mysql.VARCHAR(length=500))
    what_gold = Column(mysql.VARCHAR(length=500))
    when_gold = Column(mysql.VARCHAR(length=500))
    where_gold = Column(mysql.VARCHAR(length=500))
    user_id = Column(mysql.VARCHAR(length=500))
    how_many_injured_or_dead_if_people = Column(mysql.VARCHAR(length=500))
    people_or_infrastructure = Column(mysql.VARCHAR(length=500))
    people_or_infrastructureconfidence = Column(mysql.VARCHAR(length=500))
    what_infrastructure_was_damaged_if_infrastructure = Column(mysql.VARCHAR(length=500))
    how_many_injured_or_dead_if_people_gold = Column(mysql.VARCHAR(length=500))
    people_or_infrastructure_gold = Column(mysql.VARCHAR(length=500))
    intention = Column(mysql.VARCHAR(length=500))
    intentionconfidence = Column(mysql.VARCHAR(length=500))
    type_of_donation = Column(mysql.VARCHAR(length=500))
    type_of_donationconfidence = Column(mysql.VARCHAR(length=500))
    who = Column(mysql.VARCHAR(length=500))
    intention_gold = Column(mysql.VARCHAR(length=500))
    type_of_donation_gold = Column(mysql.VARCHAR(length=500))
    who_gold = Column(mysql.VARCHAR(length=500))
    type_of_message = Column(mysql.VARCHAR(length=500))
    type_of_message_confidence = Column(mysql.VARCHAR(length=500))
    url_or_name_of_the_stationchannel = Column(mysql.VARCHAR(length=500))
    type_of_message_gold = Column(mysql.VARCHAR(length=500))
    url_or_name_of_the_stationchannel_gold = Column(mysql.VARCHAR(length=500))
    joplin_raw = Column(mysql.VARCHAR(length=500))
    creationdate = Column(mysql.VARCHAR(length=500))
    replyto = Column(mysql.VARCHAR(length=500))
    replytouser = Column(mysql.VARCHAR(length=500))
    replytoscreenname = Column(mysql.VARCHAR(length=500))
    longitude = Column(mysql.VARCHAR(length=500))
    latitude = Column(mysql.VARCHAR(length=500))
    favorite = Column(mysql.VARCHAR(length=500))
    retweet = Column(mysql.VARCHAR(length=500))
    hashtags = Column(mysql.VARCHAR(length=500))
    mediaurl = Column(mysql.VARCHAR(length=500))
    city = Column(mysql.VARCHAR(length=500))
    sandy_raw_dataset = Column(mysql.VARCHAR(length=500))
    tweet__no = Column(mysql.VARCHAR(length=500))
    user = Column(mysql.VARCHAR(length=500))
    tweet_text = Column(mysql.VARCHAR(length=500))
    url = Column(mysql.VARCHAR(length=500))
    sandy_labeled = Column(mysql.VARCHAR(length=500))
    type = Column(mysql.VARCHAR(length=500))
    hom_many_injured_or_dead_if_people = Column(mysql.VARCHAR(length=500))
    hom_many_injured_or_dead_if_people_gold = Column(mysql.VARCHAR(length=500))
    what_infrastructure_was_damaged_if_infrastructure_gold = Column(mysql.VARCHAR(length=500))
    the_author_of_the_tweet_seems_to_be_an_eye_witness_of_the_event = Column(mysql.VARCHAR(length=500))
    the_author_of_the_tweet_seems_to_be_an_eye_witness = Column(mysql.VARCHAR(length=500))
    _of_the_eventconfidence = Column(mysql.VARCHAR(length=500))
    the_author_of_the_tweet_seems_to_be_an_eye_witness_of_the_event_ = Column(mysql.VARCHAR(length=500))
    tweet_no = Column(mysql.VARCHAR(length=500))
    tweet_no_rt = Column(mysql.VARCHAR(length=500))
    type_of_mess = Column(mysql.VARCHAR(length=500))
    age_gold = Column(mysql.VARCHAR(length=500))
    _created_at = Column(mysql.VARCHAR(length=500))
    _id = Column(mysql.VARCHAR(length=500))
    _missed = Column(mysql.VARCHAR(length=500))
    _started_at = Column(mysql.VARCHAR(length=500))
    _tainted = Column(mysql.VARCHAR(length=500))
    _channel = Column(mysql.VARCHAR(length=500))
    _trust = Column(mysql.VARCHAR(length=500))
    _worker_id = Column(mysql.VARCHAR(length=500))
    _country = Column(mysql.VARCHAR(length=500))
    _region = Column(mysql.VARCHAR(length=500))
    _city = Column(mysql.VARCHAR(length=500))
    _ip = Column(mysql.VARCHAR(length=500))
    word_or_shortphrase = Column(mysql.VARCHAR(length=500))
    instruction = Column(mysql.VARCHAR(length=500))
    type_ = Column(mysql.VARCHAR(length=500))
    of_message = Column(mysql.VARCHAR(length=500))
    type_of_messageconfidence = Column(mysql.VARCHAR(length=500))
    word_or_shortphrase_gold = Column(mysql.VARCHAR(length=500))
    tokenized = Column(mysql.INTEGER(display_width=11))
    body = Column(mysql.VARCHAR(length=500))
    object_id = Column(mysql.INTEGER(display_width=50))
    type_of_sampling = Column(mysql.VARCHAR(length=500))
    is_random_keyword = Column(mysql.INTEGER(display_width=11))
    is_categorized = Column(mysql.INTEGER(display_width=11))
