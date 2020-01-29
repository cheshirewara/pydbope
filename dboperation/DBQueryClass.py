import os
import errno


class DBQuery:
    '''
    DB query setup  class.
    '''

    def __init__(self, query_path: str = None):
        if query_path is None:
            query_path = os.path.join(os.path.dirname(
                __file__), 'sample_query.sql')
        # check sql file exist
        if not os.path.exists(query_path):
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), query_path)
        # read file
        with open(query_path) as f:
            self.__lines = f.readlines()

    # Getter

    def get_lines(self):
        return self.__lines

    # get query string

    def get_query_string(self):
        return ''.join(map(str, self.__lines))


if __name__ == '__main__':
    print(DBQuery().get_lines())
    print(DBQuery().get_query_string())
