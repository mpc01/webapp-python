#coding = utf-8
#sqlalchemy

#import Column for fields; String create_engine
from sqlalchemy import Column, String, create_engine
#init DBsession
from sqlalchemy.orm import sessionmaker
#declarative base class
from sqlalchemy.ext.declarative import declarative_base

#new declarative base
Base = declarative_base()

#new table
class User(Base):
	"""sqlalchemy:table user"""
	#table name
	__tablename__ = 'user'
	#table structure
	id = Column(String(20), primary_key = True)
	name = Column(String(20))

#init database
dbconninfo = 'mysql+mysqlconnector://root:gld1989@@localhost:3306/test'
engine = create_engine(dbconninfo)

DBsession = sessionmaker(bind = engine)

if __name__ == '__main__':
	newsession = DBsession()
	newuser = User(id = '3', name = 'Sun')
	newsession.add(newuser)
	newsession.commit()
	newsession.close()