import random

IP_POOL = [
              {'ip_port': '183.172.169.237:8118'},
              {'ip_port': '219.245.18.63:3128'},
              {'ip_port': '60.177.227.181:18118'},
              {'ip_port': '223.241.78.220:18118'},
              {'ip_port': '183.159.93.54:18118'},
              {'ip_port': '222.182.225.133:61234'}
          ]


def run():
    name = random.choice(IP_POOL)
    print(name)


if __name__ == '__main__':
    run()
