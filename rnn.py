import sys
from datetime import datetime


def rnn():
    print('running rnn')
    sys.stdout = open("rnn.out", "w")
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time to start rnn =", current_time)
    print('running rnn')
    from models import rnn