import sys
from datetime import datetime


def cnn():
    print('running cnn')
    sys.stdout = open("cnn.out", "w")
    print('running cnn')
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time of starting cnn =", current_time)
    from models import test_model
    test_model.run()
