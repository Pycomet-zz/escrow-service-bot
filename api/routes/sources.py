from model import session, User, Trade, Dispute, Affiliate

users = session.query(User).all()

trades = session.query(Trade).all()

disputes = session.query(Dispute).all()

affiliates = session.query(Affiliate).all()