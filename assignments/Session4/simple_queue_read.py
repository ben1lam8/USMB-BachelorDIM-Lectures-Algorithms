#!/usr/bin/env python

## @namespace S4_simple_queue_read
# A simple script to read incomes from a queue
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE
import argparse;
import pika;
import os;
import time;

count = 0;

# Parse command line arguments
parser = argparse.ArgumentParser();
parser.add_argument('-c', '-concurrency', action='store_true', help='Enable concurrent reading');
args = parser.parse_args();

# Configure connection
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

queue_name = "presentation";

connection = pika.BlockingConnection(params);

channel = connection.channel();
channel.queue_declare(queue=queue_name);

# Define a callback

## The callback behaviour for a busy reader
#
# @param ch
# @param method
# @param properties
# @param body
def callback(ch, method, properties, body):

    global count;
    global args;
    count += 1;
    print("--- Message #{c} received ---".format(c=count));
    print("Content : %r \n" % body);

    #Act as a laborious reader
    time.sleep(1);

    if args.c:
        ch.basic_ack(delivery_tag=method.delivery_tag);


# Define a consumer behaviour
if args.c:
    channel.basic_qos(prefetch_count=1);

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=not args.c);

# Wait for incomes
print("Waiting for incomes ... (Ctrl+C to quit)");
channel.start_consuming();