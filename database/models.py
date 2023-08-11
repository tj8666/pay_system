from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


# User sheets
class User(Base):
    __tablename__ ='users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    profile_photo = Column(String)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String)
    reg_date = Column(DateTime)
    password = Column(String, nullable=False)
# card sheets
class Card(Base):
    __tablename__ ='cards'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    card_number = Column(BigInteger, nullable=False, unique=True)
    exp_date = Column(Integer, nullable=False)
    card_balance = Column(Float, default=15000)
    card_name = Column(String, default='My Card')

    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy='subquery')


# Payment sheets
class Transaction(Base):
    __tablename__ = 'user_transactions'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    card_from = Column(BigInteger, ForeignKey('cards.card_number'))
    amount = Column(Float)
    card_to = Column(BigInteger, ForeignKey('cards.card_number'))
    transfer_time = Column(DateTime)

    card_from_fk = relationship(Card, lazy='subquery')
    user_fk = relationship(Card, lazy='subquery')

# Sheets of category of payments
class PayCategory(Base):
    __tablename__ = 'pay_categories'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    category_name = Column(String, nullable=False)

    reg_date = Column(DateTime)




