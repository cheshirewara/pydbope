class Helper:

    @staticmethod
    def is_Empty(obj):
        if not obj.strip():
            return True
        else:
            return False


if __name__ == '__main__':
    print(PyDBOpeHelper.is_Empty('password'))
