import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'class'))
from DBConfigClass import DBConfigBase
from DBQueryClass import DBQueryBase


class DBConfig(DBConfigBase):
    pass


class DBQuery(DBQueryBase):
    pass


if __name__ == '__main__':
    print(DBConfig().get_inner())
