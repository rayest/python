import time
from datetime import datetime


def to_utc(x):
    d = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(x * 0.001))
    print(d)


Y_M_D_H_M_S = '%Y-%m-%d %H:%M:00'
UTC = '%Y-%m-%dT%H:%M:%SZ'


def current():
    return datetime.now().strftime(UTC)


if __name__ == '__main__':
    print(current())
