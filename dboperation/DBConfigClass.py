import os
import errno
import configparser
# import sys
# sys.path.append(os.path.dirname(__file__))
from __dboperation_helper import Helper


class DBConfig:
    '''
    DB connection config  class.
    '''

    def __init__(self, ini_path: str = None):
        if ini_path is None:
            ini_path = os.path.join(os.path.dirname(__file__), '.db.ini.tmp')
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
    def __get_con_str_min(self, scheme: str, sec: str, *,
                          server: str = 'server', port: str = 'port'):
        return "%s://%s:%s" % (
            scheme, self.get_server(sec, server=server), self.get_port(sec, port=port))

    def __get_con_str_short(self, scheme: str, sec: str, *,
                            user: str = 'user', server: str = 'server', port: str = 'port'):
        if Helper.is_Empty(self.get_user(sec, user=user)):
            return self.__get_con_str_min(
                scheme, sec, server=server, port=port)
        else:
            return "%s://%s@%s:%s" % (
                scheme, self.get_user(sec, user=user),
                self.get_server(sec, server=server),
                self.get_port(sec, port=port))

    def get_con_str(self, scheme: str, sec: str, *,
                    user: str = 'user', password: str = 'password', server: str = 'server',
                    port: str = 'port'):
        if Helper.is_Empty(self.get_password(sec, password=password)):
            return self.__get_con_str_short(
                scheme, sec, user=user, server=server, port=port)
        else:
            return "%s://%s:%s@%s:%s" % (
                scheme, self.get_user(sec, user=user),
                self.get_password(sec, password=password),
                self.get_server(sec, server=server),
                self.get_port(sec, port=port))

    def get_con_str_long(self, scheme: str, sec: str, *,
                         user: str = 'user', password: str = 'password', server: str = 'server',
                         port: str = 'port', database: str = 'database'):
        return "%s://%s:%s@%s:%s/%s" % (
            scheme, self.get_user(sec, user=user),
            self.get_password(sec, password=password),
            self.get_server(sec, server=server), self.get_port(sec, port=port),
            self.get_database(sec, database=database))


if __name__ == '__main__':
    print(DBConfig().get_config())
    print(DBConfig().get_inner())
    print(DBConfig().get_con_str_long('mongodb', sec='MONGODB'))
    print(DBConfig().get_con_str('mongodb', sec='MONGODB'))
