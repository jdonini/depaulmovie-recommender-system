import numpy as np

DATA_PATH = '../dataset/Movie_DePaulMovie/ratings.txt'

with open(DATA_PATH, 'rt') as lines:
    for line in lines:
        if line[0] == 'u':
            pass
        else:
            (user_id, item_id, rating, time, location, companion) = line.strip().split(',')
            print('User: {}'.format(user_id))
            print('Item: {}'.format(item_id))
            print('Rating: {}'.format(rating))
            print('Time: {}'.format(time))
            print('Location: {}'.format(location))
            print('Companion: {}'.format(companion))
            print('--' * 50)
