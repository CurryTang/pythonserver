from conf.base import BASEDB, engine
import sys
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)


class Users(BASEDB):
    """
        Table for users
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    phone = Column(String(50), nullable=False)
    createTime = Column(DateTime, nullable=False)

    def __init__(self, phone, createTime):
        self.createTime = createTime
        self.phone = phone


def initDB():
    BASEDB.metadata.create_all(engine)


if __name__ == '__main__':
    print("Initialize DB")
    initDB()


