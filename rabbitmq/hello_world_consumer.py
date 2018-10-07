#!/usr/bin/env python
import pika
credentials = pika.PlainCredentials('guest', 'guest')

connection_params = pika.ConnectionParameters(host='localhost', credentials=credentials)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='hello-exchange',
                         exchange_type='direct',
                         passive=False,
                         durable=True,
                         auto_delete=False)
channel.queue_declare(queue='hello-queue')
channel.queue_bind(queue='hello-queue', exchange='hello-exchange', routing_key='hola')


def msg_consumer(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == 'quit':
        channel.basic_channel(consumer_tag='hello-consumer')
        channel.stop_consuming()

    else:
        print(body)
    print(" [x] Received %r" % body)


channel.basic_consume(msg_consumer,
                      queue='hello-queue',
                      consumer_tag='hello-consumer')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
