from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
dog = Table('dog', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('age', VARCHAR(length=100)),
    Column('aditional_info', TEXT),
    Column('volnteer_id', INTEGER),
    Column('status', INTEGER),
    Column('gender', INTEGER),
    Column('region', INTEGER),
    Column('size', INTEGER),
)

dog = Table('dog', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('age', String(length=100)),
    Column('aditional_info', Text),
    Column('volounteer_id', Integer),
    Column('status', Integer),
    Column('gender', Integer),
    Column('region', Integer),
    Column('size', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['dog'].columns['volnteer_id'].drop()
    post_meta.tables['dog'].columns['volounteer_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['dog'].columns['volnteer_id'].create()
    post_meta.tables['dog'].columns['volounteer_id'].drop()
