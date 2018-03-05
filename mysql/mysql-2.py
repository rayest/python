from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = 'mysql+pymysql://root:199011081108@127.0.0.1:3306/python'
engine = create_engine(DB_URI, echo=False)
Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))


Base.metadata.create_all()


def create_user():
    Session = sessionmaker()
    session = Session()
    user = User(username='rayest', password='123456')
    session.add(user)
    session.commit()


if __name__ == '__main__':
    create_user()