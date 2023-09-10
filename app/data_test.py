from data import Database


def test_something():
    """This function tests where or not the client connects to the mongodb database"""
    test = Database()
    if test.client.is_primary:
        print('Client connected to successfully')
    else:
        print('No connection made')


if __name__ == '__main__':
    print(test_something())
