from sqlalchemy import create_engine, func, \
    Column, BigInteger, DateTime, Integer, String, Boolean, Text, ForeignKey, JSON

from sqlalchemy.orm import declarative_base, relationship

from config import db_engine

engine = create_engine(db_engine)

Base = declarative_base()


class Stat_user(Base):
    __tablename__ = 'stat_user'

    pk = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now())
    joined_at = Column(DateTime)
    left_at = Column(DateTime)

    tg_user_id = Column(BigInteger)
    tg_channel_id = Column(BigInteger)

    first_name = Column(String(255))
    last_name = Column(String(255))
    username = Column(String(255))
    phone = Column(String(50))

    scam = Column(Boolean)
    premium = Column(Boolean)
    verified = Column(Boolean)
    is_joined_by_link = Column(Boolean)


class Stat_post(Base):
    __tablename__ = 'stat_post'

    pk = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now())
    date_of_post = Column(String(25))   # forgot in the schema.prism

    tg_post_id = Column(BigInteger)
    tg_channel_id = Column(BigInteger)

    message = Column(Text)
    views = Column(Integer)
    views_1h = Column(Integer)
    views_24h = Column(Integer)

    total_reactions_count = Column(Integer)
    reactions_1h = Column(Integer)
    reactions_24h = Column(Integer)

    comments_users_count = Column(Integer)
    comments_channels_count = Column(Integer)

    comments_messages_count = Column(Integer)
    comments_messages_count_1h = Column(Integer)
    comments_messages_count_24h = Column(Integer)

    link = Column(Text)
    media = Column(Text)
    forwards = Column(Integer)


class Stat_reaction(Base):
    __tablename__ = 'stat_reaction'

    pk = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now())

    tg_post_id = Column(BigInteger)
    tg_channel_id = Column(BigInteger)

    reaction_count = Column(Integer)
    reaction_emoticon = Column(String(5))
    reaction_emoticon_code = Column(Integer)


class Config__tg_channel(Base):
    __tablename__ = 'config__tg_channel'

    pk = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())

    tg_channel_id = Column(BigInteger)
    tg_channel_name = Column(String(255))

    config__tg_bot_session_pool = relationship('Config__tg_bot_session_pool')


class Config__tg_bot_session_pool(Base):
    __tablename__ = 'config__tg_bot_session_pool'

    pk = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())

    api_id = Column(String(255))
    api_hash = Column(String(255))
    phone_number = Column(String(50))
    session_bytes = Column(Text)

    status = Column(String(10), default='enabled')     # enabled/banned

    config__tg_channel = Column(BigInteger, ForeignKey('config__tg_channel.pk'))
    config__tg_channel_pk = Column(BigInteger)


class Datalake__tg_channel(Base):
    __tablename__ = 'datalake__tg_channel'

    pk = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now())

    json = Column(JSON)
    tg_channel_id = Column(BigInteger)


class Datalake__tg_post(Base):
    __tablename__ = 'datalake__tg_post'

    pk = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now())

    json = Column(JSON)
    tg_channel_id = Column(BigInteger)
    tg_post_id = Column(BigInteger)


class Datalake__tg_comment(Base):
    __tablename__ = 'datalake__tg_comment'

    pk = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now())

    json = Column(JSON)
    tg_channel_id = Column(BigInteger)
    tg_post_id = Column(BigInteger)


class Datalake__tg_admin_log(Base):
    __tablename__ = 'datalake__tg_admin_log'

    pk = Column(BigInteger, primary_key=True)
    timestamp = Column(DateTime, server_default=func.now())

    json = Column(JSON)
    tg_channel_id = Column(BigInteger)
