#!/usr/bin/env python

## @namespace S4_simple_queue_publish
# A simple script to publish a test message
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;
import argparse;

# Parse command line arguments
parser = argparse.ArgumentParser();
parser.add_argument('-c', '-concurrency', action='store_true', help='Enable message persistence');
parser.add_argument('-n', '-number', type=int, default=1, help='Amount of test messages to send');
args = parser.parse_args();

# Configure connection and message
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

queue_name = "presentation";
message_content = raw_input(
    "Please enter the persistent content (it will be repeated {n} time(s)) : ".format(n=args.n)
    if args.c
    else "Please enter the volatile content (it will be repeated {n} time(s)) : ".format(n=args.n));

# Connect
connection = pika.BlockingConnection(params);

# Publish
channel = connection.channel();

i = 1;
while i <= args.n:
    ith_message_content = "#{i} - {mc}".format(i=i, mc=message_content);
    if args.c:
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=ith_message_content,
                              properties=pika.BasicProperties(
                                  delivery_mode = 2 #persistant message
                              ));

    else:
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message_content);

    # Report
    print("--- Message published ---\n");
    print("Destination Queue : {ip}.{q}".format(ip=instance_provider, q=queue_name));
    print("Message content : {b}".format(b=ith_message_content));

    i += 1;


# Disconnect
connection.close();