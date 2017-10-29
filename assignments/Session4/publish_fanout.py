#!/usr/bin/env python

## @namespace S4_publish_fanout
# A simple script to publish and push message to multiple queues of an exchange
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;
import argparse;

# Parse command line arguments
parser = argparse.ArgumentParser();
parser.add_argument('-n', '-number', type=int, default=1, help='Amount of test messages to send');
args = parser.parse_args();

# Configure connection and message
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

exchange_name = "posts";
message_content = raw_input("Please enter the volatile content (it will be repeated {n} time(s)) : ".format(n=args.n));

# Connect
connection = pika.BlockingConnection(params);

# Publish
channel = connection.channel();
channel.exchange_declare(exchange=exchange_name, exchange_type='fanout');

i = 1;
while i <= args.n:
    ith_message_content = "#{i} - {mc}".format(i=i, mc=message_content);

    channel.basic_publish(exchange=exchange_name,
                          routing_key='',
                          body=ith_message_content);

    # Report
    print("--- Message published ---\n");
    print("Destination Exchange : {ip}.{e}".format(ip=instance_provider, e=exchange_name));
    print("Message content : {b}".format(b=ith_message_content));

    i += 1;


# Disconnect
connection.close();