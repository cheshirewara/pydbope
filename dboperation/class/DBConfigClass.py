# required modules import
import os
import sys

import errno
import configparser
# import const as cst


class DBConfig:
    '''
    DB connection config  class.
    '''

    def __init__(self, ini_path: str = None):
        if ini_path is None:
            ini_path = os.path.join(os.path.dirname(
                __file__), '..', '.db.ini.tmp')
        # check ini file exist
        if not os.path.exists(ini_path):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), ini_path)
        # read config file
        self.__config = configparser.ConfigParser()
        self.__config.read(ini_path, encoding='utf-8')

        # set config data
        self.__inner = self.__config._sections

    # Getter

    def get_config(self):
        return self.__config

    def get_inner(self):
        return self.__inner

    # Key Getter

    def get_user(self, sec: str, *, user: str = 'user'):
        return None if not user in self.__inner[sec] else self.__inner[sec][user]

    def get_password(self, sec: str, *, password: str = 'password'):
        return None if not password in self.__inner[sec] else self.__inner[sec][password]

    def get_server(self, sec: str, *, server: str = 'server'):
        return None if not server in self.__inner[sec] else self.__inner[sec][server]

    def get_port(self, sec: str, *, port: str = 'port'):
        return None if not port in self.__inner[sec] else self.__inner[sec][port]

    def get_database(self, sec: str, *, database: str = 'database'):
        return None if not database in self.__inner[sec] else self.__inner[sec][database]

    def get_collection(self, sec: str, *, collection: str = 'collection'):
        return None if not collection in self.__inner[sec] else self.__inner[sec][collection]

    # get connection string

    def get_con_str(self, scheme: str, sec: str, *, user: str = 'user', password: str = 'password',
                    server: str = 'server', port: str = 'port'):
        return "%s://%s:%s@%s:%s" % (
            scheme, self.__inner[sec][user], self.__inner[sec][password], self.__inner[sec][server], self.__inner[sec][port])

    def get_con_str_long(self, scheme: str, sec: str, *, user: str = 'user', password: str = 'password',
                         server: str = 'server', port: str = 'port', database: str = 'database'):
        return "%s://%s:%s@%s:%s/%s" % (
            scheme, self.__inner[sec][user], self.__inner[sec][password], self.__inner[sec][server], self.__inner[sec][port], self.__inner[sec][database])


if __name__ == '__main__':
    print(DBConfig().get_config())
    print(DBConfig().get_inner())
    print(DBConfig().get_user('MONGODB'))
    print(DBConfig().get_password('MONGODB'))
    print(DBConfig().get_server('MONGODB'))
    print(DBConfig().get_port('MONGODB'))
    print(DBConfig().get_database('MONGODB'))
    print(DBConfig().get_collection('MONGODB'))
    print(DBConfig().get_con_str_long('postgresql', sec='POSTGRESQL'))
    print(DBConfig().get_con_str('mongodb', sec='MONGODB'))
