# print('Hello')
# print('what is your name? ')
# my_name = input()
# print('it is good to meet you '+ my_name)
from datetime import datetime
import random


def time_sleep(time):
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
            21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
            41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
    for i in range(5):
        right_this_minute = datetime.today().minute
        if right_this_minute in odds:
            print('This minute is odd')
        else:
            print('Not an odd minute')


wait_time = random.randint(1, 10)
print(wait_time)
time_sleep(wait_time)
print('done processing')
