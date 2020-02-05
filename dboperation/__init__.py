import os
import sys
sys.path.append(os.path.dirname(__file__))
from DBConfigClass import DBConfig
from DBQueryClass import DBQuery
from DBControlClass import DBControl


def Hello():
    return "Hello dboperation"


if __name__ == '__main__':
    print(Hello())
