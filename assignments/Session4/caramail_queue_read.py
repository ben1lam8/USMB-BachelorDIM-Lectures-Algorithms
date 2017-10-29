#!/usr/bin/env python

## @namespace S4_caramail_queue_read
# A simple script to read incomes from a cumstom queue
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE
import argparse;
import pika;
import os;
import time;

# Parse command line arguments
parser = argparse.ArgumentParser();
parser.add_argument('-c', '-channel', action='store', dest='queue_name', default='general', help='The channel you want to post to');
args = parser.parse_args();

# Configure connection
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

connection = pika.BlockingConnection(params);

exchange_name = "caramail";
channel = connection.channel();
channel.exchange_declare(exchange=exchange_name, exchange_type='direct');

queue_name = args.queue_name;

channel.queue_bind(exchange=exchange_name, queue=queue_name);

# TODO : Handle multiple connections to one channel

print("--- WELCOME TO THE CHANNEL {c} ---\n".format(c=args.queue_name.upper()));

# Define a callback

## The callback behaviour for a busy reader
#
# @param ch
# @param method
# @param properties
# @param body
def callback(ch, method, properties, body):

    global args;
    print("%r" % body);


# Define a consumer behaviour

channel.basic_consume(callback,
                      queue=args.queue_name,
                      no_ack=True);

# Wait for incomes
print("Waiting for incomes ... (Ctrl+C to quit)");
channel.start_consuming();