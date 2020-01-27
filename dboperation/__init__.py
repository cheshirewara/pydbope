import os
import sys
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'class'))
from DBConfigClass import DBConfig
from DBQueryClass import DBQuery


def Hello():
    print("Hello dboperation")


if __name__ == '__main__':
    print(DBConfig().get_inner())
    print(DBQuery().get_lines())
