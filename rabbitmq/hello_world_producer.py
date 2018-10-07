#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters) # 建立到代理服务器的连接 rabbitMQ

# connection = pika.BlockingConnection(pika.connectionParameters(host='localhost'))
channel = connection.channel() # 获得信道

# 声明交换器
channel.exchange_declare(exchange='hello-exchange',
                         exchange_type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)

# 创建纯文本消息
msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = 'text/plain'

# 发布消息
channel.basic_publish(exchange='hello-exchange',
                      routing_key='hola',
                      body=msg,
                      properties=msg_props)
print(" [x] Sent 'Hello World!'")
connection.close()
