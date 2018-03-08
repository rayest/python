import unittest

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
    session.close()


def query_by_username(username):
    Session = sessionmaker()
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user


def create_user(username, password):
    Session = sessionmaker()
    session = Session()
    found_user = session.query(User).filter_by(username=username).first()
    if found_user is not None:
        return found_user
    new_user = User(username=username, password=password)
    session.add(new_user)
    created_user = session.query(User).filter_by(username=username).first()
    session.commit()
    return created_user


def delete_by_username(username):
    Session = sessionmaker()
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        print('用户名不存在')
    else:
        session.query(User).filter(User.username == username).delete()
        print('删除成功')
    session.commit()


def update_password_by_username(username, password):
    Session = sessionmaker()
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        print('用户名不存在')
    else:
        session.query(User).filter(User.username == username).update({User.password: password})
        print('密码修改成功')
    session.commit()


class TestMysqlOrm(unittest.TestCase):
    def test_query_by_username(self):
        username = 'user_name_test_1'
        user = query_by_username(username)
        self.assertIsNotNone(user)
        self.assertEqual(user.password, 'password_test_1')
        self.assertEqual(user.username, username)

    def test_create_user(self):
        username = 'user_name_test_4'
        password = 'password_test_4'
        user = query_by_username(username)
        self.assertIsNone(user)
        created_user = create_user(username, password)
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.username, username)
        self.assertEqual(created_user.password, password)
        delete_by_username(username)
        self.assertIsNone(user)

    def test_update_password_by_username(self):
        username = 'user_name_test_1'
        new_password = 'password_test_1_1'
        update_password_by_username(username, new_password)


if __name__ == '__main__':
    unittest.main()
