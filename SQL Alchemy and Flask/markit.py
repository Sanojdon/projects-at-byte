from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from datetime import datetime

Base = declarative_base()

class User(Base):
	__tablename__ = "Users"
	usr_id = Column(Integer, primary_key=True)
	usr_name = Column(String)
	usr_amount = Column(Float, default=10000.00)
	usr_stocks = Column(Integer)
	usr_age = Column(Integer)
	usr_address = Column(String)
	usr_phone = Column(Integer)
	usr_email = Column(String)
	usr_user_name = Column(String)	
	usr_password = Column(String)
	usr_status = Column(String, default="user")
	usr_created_on = Column(DateTime, default=datetime.now())

class Transaction(Base):
	__tablename__ = "Transactions"
	trn_id = Column(Integer, primary_key=True)
	trn_user_id = Column(Integer, ForeignKey('Users.usr_id'))
	trn_symbol = Column(String)
	trn_stocks = Column(Integer)
	trn_stock_last_price = Column(Float)
	trn_total = Column(Float)
	trn_timestamp = Column(DateTime, default=datetime.now())
	trn_status = Column(String)
	user = relationship(User, backref=backref('transaction',uselist=True,cascade='delete,all')) 
	
class Stock(Base):
	__tablename__ = "Stocks"
	stk_id = Column(Integer, primary_key=True)
	stk_user_id = Column(Integer, ForeignKey('Users.usr_id'))
	stk_symbol = Column(String)
	stk_stocks = Column(Integer)
	user = relationship(User, backref=backref('stock',uselist=True,cascade='delete,all'))

engine = create_engine('sqlite:///db/markit.db')
 
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()


def add_user(name, age, phone, addr, email, uname, pword):
	u = User(usr_name=name, usr_age=age, usr_address=addr, usr_phone=phone, usr_email=email, usr_user_name=uname, usr_password=pword)
	s.add(u)
	s.commit()
	return(True)

def get_username(uname):
	query = s.query(User).filter(User.usr_user_name == uname).all()
	return query

def portfolio(uid):
	user_details = s.query(User.usr_name, User.usr_amount).filter(User.usr_id == uid).first()
	trans_details = s.query(Transaction).filter(Transaction.trn_user_id == uid).all()
	stock_details = s.query(Stock).filter(Stock.stk_user_id == uid).all()
	return user_details, trans_details, stock_details

def get_details(uname):
	user_details = s.query(User).filter(User.usr_user_name == uname).first()
	return user_details

def buy_shares(sym, no, last, total, uid):
	user = s.query(User).filter(User.usr_id == uid).first()
	transaction = Transaction(trn_user_id=uid, trn_symbol=sym, trn_stocks=no, trn_stock_last_price=last, trn_total=total, trn_status="BUY")
	stock = Stock(stk_user_id=uid, stk_symbol=sym, stk_stocks=no)
	user.usr_amount = user.usr_amount - total
	s.add(transaction)
	s.add(stock)
	s.commit() 
	return "Done"

def sell_shares(sym, no, last, total, uid):
	user = s.query(User).filter(User.usr_id == uid).first()
	transaction = Transaction(trn_user_id=uid, trn_symbol=sym, trn_stocks=no, trn_stock_last_price=last, trn_total=total, trn_status="SELL")
	stock = s.query(Stock).filter(Stock.stk_user_id == uid, Stock.stk_symbol == sym).first()
	user.usr_amount = user.usr_amount + total
	stock.stk_stocks = stock.stk_stocks - no
	s.add(transaction)
	s.commit() 
	return "Done"