# from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Date
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.sql.expression import null
# import sqlite3

from datetime import datetime
from sqlalchemy import (create_engine, Table, Column, Integer, Numeric, String, DateTime, ForeignKey, JSON)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import base

Base = declarative_base()

class UserRole(Base):
    __tablename__ = 'user_roles'
    role_id = Column(Integer(), primary_key=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)    

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(16), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    password = Column(String(25), nullable=False)
    role_id = Column(Integer(), ForeignKey('user_roles.role_id'))
    role = relationship("UserRole", backref=backref('users', order_by=user_id))    
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
    

class Contest(Base):
    __tablename__ = 'contests'
    contest_id = Column(Integer(), primary_key=True)
    contestname = Column(String(255))

#
# class Contests_Documents(Base):
#     __tablename__ = 'contests_documents'
#     contests_documents_id = Column(Integer(), primary_key=True)

""

class ContestNomination(Base):
    __tablename__ = 'nominations'
    nomination_id = Column(Integer(), primary_key=True)
    nominationname = Column(String(255))
    contest_id = Column(Integer(), ForeignKey('contests.contest_id'))
    nomination = relationship("Contest", backref=backref('nominations', order_by=nomination_id))     

#
# class Nominations_Documents(Base):
#     __tablename__ = 'nominations_documents'
#     nominations_documents_id = Column(Integer(), primary_key=True)

""

class ContestStage(Base):
    __tablename__ = 'stages'
    stage_id = Column(Integer(), primary_key=True)
    stagename = Column(String(255))
    nomination_id = Column(Integer(), ForeignKey('nominations.nomination_id'))
    nomination = relationship("ContestNomination", backref=backref('stages', order_by=stage_id)) 

#
# class Stages_Documents(Base):
#     __tablename__ = 'stage_documents'
#     stages_documents_id = Column(Integer(), primary_key=True)

# class Stages_Users(Base):
#     __tablename__ = 'stages_users'
#     stages_users_id = Column(Integer(), primary_key=True)
#     rating = Column(Integer())

#     stage_id = Column(Integer(), ForeignKey('contest-stages.stage_id'))
#     user = relationship("ContestStage", backref=backref('stages_users', order_by=stages_users_id)) 
#     user_id = Column(Integer(), ForeignKey('user_roles.role_id'))
#     user = relationship("User", backref=backref('stages_users', order_by=stages_users_id)) 
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now,
#                         onupdate=datetime.now)        

""

""

class Document(Base):
    __tablename__ = 'documents'
    document_id = Column(Integer(), primary_key=True)
    documentname = Column(String(255))
    document_json = Column(JSON(), nullable=True)
    document_ref = Column(String(255), nullable=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)    


class Stages_Users_Documents(Base):
    __tablename__ = 'stages_users'
    stages_users_id = Column(Integer(), primary_key=True)
    rating = Column(Integer())

    stage_id = Column(Integer(), ForeignKey('contest-stages.stage_id'))
    user = relationship("ContestStage", backref=backref('stages_users', order_by=stages_users_id)) 
    user_id = Column(Integer(), ForeignKey('user_roles.role_id'))
    user = relationship("User", backref=backref('stages_users', order_by=stages_users_id)) 
    document_id = Column(Integer(), ForeignKey('documents.document_id'))
    document = relationship("Document", backref=backref('stages_users', order_by=stages_users_id)) 

    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)  

 
if __name__ == '__main__':
    engine = create_engine(f"sqlite:///tavolga.sqlite", echo=True, encoding='utf-8')
    Base.metadata.create_all(bind=engine)
