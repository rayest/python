import time
from datetime import datetime


def to_utc(x):
    d = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(x*0.001))

    print(d)


if __name__ == '__main__':
    to_utc(1523944499474)