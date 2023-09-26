from data import Database
from sklearn.model_selection import train_test_split
import numpy as np


def test_something():
    """This function tests where or not the client connects to the mongodb database"""
    test = Database()
    if test.client.is_primary:
        print('Client connected to successfully')
    else:
        print('No connection made')


def test_shape():
    df = Database()
    df = df.dataframe()
    target = 'Rarity'
    x = df.drop(columns=target)
    y = df[target]
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        shuffle=True,
                                                        random_state=42)
    print(f'{x.shape}, {y.shape}')
    print(f'{x_train.shape}, {x_test.shape}')
    print(f'{y_train.shape}, {y_test.shape}')
    for column in df:
        print(column)
        print(type(column))


if __name__ == '__main__':
    print(test_something())
    test_shape()
