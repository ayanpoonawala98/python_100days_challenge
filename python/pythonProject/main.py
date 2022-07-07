#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters('localhost',
                                   5672,
                                            '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='ayan', durable=True)
for i in range(1000):
    channel.basic_publish(exchange='',
                  routing_key='ayan',
                  body='{"message":"dont izmmm me"}')


    print(" [x] Sent 'Hello World!'")
connection.close()