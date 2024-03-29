from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
 
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	email = Column(String(80))
	
class Category(Base):
	__tablename__ = 'category'
	
	id = Column(Integer, primary_key=True)
	name = Column(String(80), nullable=False)
	
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'name'         : self.name,
			'id'           : self.id,
		}
 
class Item(Base):
	__tablename__ = 'item'
	
	name =Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	description = Column(String(250))
	created_date = Column(DateTime, default=datetime.datetime.utcnow)
	category_id = Column(Integer,ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer,ForeignKey('user.id'))
	user = relationship(User)
	
	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
           'name': self.name,
           'description': self.description,
           'id': self.id,
		   'created_date': self.created_date,
           'category_id': self.category_id,
		   'category_name': self.category_name,
           'user_id': self.user_id,
		   }


engine = create_engine('sqlite:///catalog.db')
 

Base.metadata.create_all(engine)
