from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

PASSWORD = "czk1998*#"

engine = create_engine("mysql://root:{}@localhost:3306/parking?charset=utf8".format(PASSWORD), encoding="utf8", echo=False)
BASEDB = declarative_base()

ERROR_CODE = {
    "0": "ok",
    "1001": "Invalid argument",
    "1002": "Have been registered"
}


