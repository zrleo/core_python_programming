# -*- coding:utf-8 -*-


from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):

    # 表名字
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


engine = create_engine('mysql+mysqldb://root:123456@127.0.0.1:3306/test')
DBsession = sessionmaker(bind=engine)
# session = DBsession()
# new_user = User(id='6', name='bob')
# session.add(new_user)
# session.commit()
# session.close()

session = DBsession()
user = session.query(User).filter(User.id == '6').one()
print 'type:', type(user)
print 'name:', user.name
session.close()
