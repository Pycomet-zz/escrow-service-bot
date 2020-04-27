from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

from config import *

Base = declarative_base()

engine = create_engine(
    "postgres://mkedfkiekfmfim:e6bcccb977c4c7a242fa857cbd4285308d5a96052bffb15aa4e45c925108daff@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d88bdvbmhui1ks",
    echo=False)
#    connect_args={'check_same_thread': False},

class Trade(Base):
    """
    SqlAlchemy ORM Trade Model
    """
    __tablename__ = 'trades'

    id = Column(String, primary_key=True)

    seller = Column(Integer)
    buyer = Column(Integer)
    price = Column(Integer)

    currency = Column(String)
    coin = Column(String)
    wallet = Column(String)

    payment_status = Column(Boolean)
    created_at = Column(String)
    is_open = Column(Boolean)

    receive_address_id = Column(String)

    def __repr__(self):
        return "<Trade(id='%s')>" % (self.id)



# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine, autoflush=False)

session = Session()

# import pdb; pdb.set_trace()

session.close()

