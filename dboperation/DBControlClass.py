import os
import errno
# import psycopg2 as pg
# import pandas.io.sql as psql


class DBControl:
    '''
    DB control  class.
    '''

    def __init__(self, con_str: str = None):
        if con_str is None:
            raise ValueError(
                errno.EINVAL, os.strerror(errno.EINVAL), 'con_str')
        self.__con_str = con_str

    # Getter

    def get_con_str(self):
        return self.__con_str

    def set_con_str(self, con_str: str = None):
        if con_str is None:
            raise ValueError(
                errno.EINVAL, os.strerror(errno.EINVAL), 'con_str')
        self.__con_str = con_str
        return self

    # private method

    def __get_connection(self):
        import psycopg2 as pg
        return pg.connect(self.get_con_str())

    # public method

    def get_db_dataframe(self, sql: str = None):
        import pandas.io.sql as psql
        if sql is None:
            raise ValueError(
                errno.EINVAL, os.strerror(errno.EINVAL), 'sql')
        with self.__get_connection() as con:
            df = psql.read_sql(sql, con)
        return df


if __name__ == '__main__':
    print()
