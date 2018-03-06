from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc

DB_URI = 'mysql+pymysql://root:199011081108@127.0.0.1:3306/python'
# echo为True时，会有相应日志输出
engine = create_engine(DB_URI, echo=True)
# Construct a base class for declarative class definitions
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))


# 元数据，描述数据的数据：id、用户名、密码。创建表结构
Base.metadata.create_all()


def test_insert_user():
    Session = sessionmaker()
    session = Session()
    try:
        user = User(username='rayest', password='123456')
        session.add(user)
        session.commit()
    except exc.IntegrityError as e:
        session.rollback()
        print(e.__cause__)


def query_by_username(username):
    Session = sessionmaker()
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        print('user is not exist')
    else:
        print(user.username)
        print(user.password)


def create_user(username, password):
    Session = sessionmaker()
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user is not None:
        print('用户名已存在')
    else:
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        print('用户创建成功')


if __name__ == '__main__':
    create_user("lee", "123456")
