#!/usr/bin/env python

import pika
import splunklib.client as client

service = client.connect(host='localhost',port=8089,username='admin',password='Admin@123')

index = service.indexes["rabbit"]

mysocket = index.attach(sourcetype='json',host='rabbitmq')

host = 'localhost'
queue = 'hello'


def on_message(ch, method, properties, body):
    message = body.decode('UTF-8')
    print(message)


def main():
    credentials = pika.PlainCredentials('user', 'password')
    parameters = pika.ConnectionParameters('192.168.1.225',
                                           5672,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=queue, durable=True)

    channel.basic_consume(queue=queue, on_message_callback=on_message, auto_ack=True)

    mysocket.send(channel)
    print('Subscribed to ' + queue + ', waiting for messages...')
    channel.start_consuming()

if __name__ == '__main__':
    main()