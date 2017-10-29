#!/usr/bin/env python

## @namespace S4_simple_queue_read
# A simple script to read incomes from a queue
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;

count = 0;

# Configure connection
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

connection = pika.BlockingConnection(params);

exchange_name = "posts";
channel = connection.channel();
channel.exchange_declare(exchange=exchange_name, exchange_type='fanout');

result = channel.queue_declare(exclusive=True);
queue_name = result.method.queue;

channel.queue_bind(exchange=exchange_name, queue=queue_name);

# Define a callback


## The callback behaviour for a busy reader
#
# @param ch
# @param method
# @param properties
# @param body
def callback(ch, method, properties, body):

    global count;
    count += 1;
    print("--- Message #{c} received ---".format(c=count));
    print("Content : %r \n" % body);


# Define a consumer behaviour

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True);

# Wait for incomes
print("Waiting for incomes ... (Ctrl+C to quit)");
channel.start_consuming();