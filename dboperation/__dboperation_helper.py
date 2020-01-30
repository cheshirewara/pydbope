class Helper:

    @staticmethod
    def is_Empty(obj):
        flag = False
        if obj is None:
            flag = True
        elif not obj.strip():
            flag = True
        else:
            flag = False
        return flag


if __name__ == '__main__':
    print(Helper.is_Empty(None))
