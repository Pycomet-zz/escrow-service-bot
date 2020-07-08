from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

from config import *

Base = declarative_base()
engine = create_engine(
    os.getenv("DATABASE_URL"),
    echo=False)
#connect_args={'check_same_thread': False},


class User(Base):
    """
    SqlAlchemy ORM for Users
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    chat = Column(String(9))

    def __repr__(self):
        return "<User(id='%s')>" % (self.id)

class Trade(Base):
    """
    SqlAlchemy ORM Trade Model
    """
    __tablename__ = 'trades'
    id = Column(String(16), primary_key=True)
    seller = Column(Integer)
    buyer = Column(Integer)
    price = Column(Integer)

    currency = Column(String(32))
    coin = Column(String(32))
    wallet = Column(String(50))

    payment_status = Column(Boolean)
    created_at = Column(String(32))
    updated_at = Column(String(32))
    is_open = Column(Boolean)
    affiliate_id = Column(String(39))

    receive_address_id = Column(String(50))

    dispute = relationship("Dispute", cascade="all, delete-orphan")

    def __repr__(self):
        return "<Trade(id='%s')>" % (self.id)

    def is_dispute(self):
        "Dispute Status"
        if self.dispute == []:
            return "No Dispute"
        else:
            return "%s Created on %s " % (self.dispute[-1].id, self.dispute[-1].created_on)


class Dispute(Base):
    """
    SQLAlchemy ORM Dispute Model
    """
    __tablename__ = "disputes"

    id = Column(Integer, unique=True, primary_key=True)
    user = Column(Integer)
    complaint = Column(String(162))
    created_on = Column(String(32))
    trade_id = Column(ForeignKey("trades.id", ondelete="CASCADE"))

    trade = relationship("Trade", uselist=False)


    def __repr__(self):
        return "<Dispute(id='%s')>" % (self.id)

    def is_seller(self):
        if self.user == self.trade[0].seller:
            return True
        else:
            return False

    def is_buyer(self):
        if self.user == self.trade[0].buyer:
            return True
        else:
            return False


class Affiliate(Base):
    """
    SQLAlchemy ORM Affiliate Records Table
    """
    __tablename__ = "affiliates"

    id = Column(Integer, unique=True, primary_key=True)
    btc_wallet = Column(String(40))
    eth_wallet = Column(String(40))
    ltc_wallet = Column(String(40))
    xrp_wallet = Column(String(40))
    bch_wallet = Column(String(40))
    admin = Column(Integer)

    def __repr__(self):
        return "<Group (id='%s')>" % (self.id)

    @classmethod
    def check_affiliate(cls, id):
        info = session.query(Affiliate).filter_by(id=id).first()
        if not info:
            return None
        else:
            return info

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine, autoflush=False)

session = Session()

# import pdb; pdb.set_trace()
session.close()

