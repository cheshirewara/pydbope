import os
import sys
sys.path.append(os.path.dirname(__file__))
from DBConfigClass import DBConfig
from DBQueryClass import DBQuery


def Hello():
    return "Hello dboperation"


if __name__ == '__main__':
    print(Hello())
    print(DBQuery().get_query_string())
    print(DBConfig().get_con_str('mongo', 'MONGODB'))
