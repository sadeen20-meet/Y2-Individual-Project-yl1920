from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   Id = Column(Integer, primary_key=True)
   firstname = Column(String)
   lastname = Column(String)
   password = Column(String)
   email = Column(String)
 
class Product(Base):
   __tablename__ = 'products'
   Id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(String)
   description = Column(String)
   picture_link = Column(String)

# class Cart(Base):
# 	 __tablename__ = 'cart'
# 	 Id = Column(Integer, primary_key=True)
# 	 productID = Column(Integer)