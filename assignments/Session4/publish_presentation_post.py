#!/usr/bin/env python

## @namespace S4_publish_presentation_post
# A simple script to publish a presentation post to the caramail exchange
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;
import argparse;

# Parse command line arguments
parser = argparse.ArgumentParser();
parser.add_argument('-s', '-signin', action='store_true', help='Notify yourself as connected to a channel');
parser.add_argument('-c', '-channel', action='store', dest='selected_channel', default='general', help='The channel you want to post to');
parser.add_argument('-n', '-nickname', action='store', dest='nickname', default='anonymous', help='The nickname you want to use');
parser.add_argument('-m', '-message', action='store', dest='message', default='- silent -', help='The message you want to post');
args = parser.parse_args();

# Configure connection and message
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

exchange_name = "caramail";

# Connect
connection = pika.BlockingConnection(params);

# Publish
channel = connection.channel();
channel.exchange_declare(exchange=exchange_name, exchange_type='direct');

if args.s:
    channel.basic_publish(exchange=exchange_name,
                          routing_key='presentation',
                          body=args.nickname+">>"+args.selected_channel);

    # Report
    print("--- Connecting to {ip} > {e} > {c} ---\n".format(ip=instance_provider, e=exchange_name, c=args.selected_channel));

else:
    channel.basic_publish(exchange=exchange_name,
                          routing_key=args.selected_channel,
                          body=args.nickname+" : "+args.message);

    # Report
    print("--- Sending to {ip} > {e} > {c} ---\n".format(ip=instance_provider, e=exchange_name, c=args.selected_channel));
    print("--- Content : %r \n" % args.message);


# Disconnect
connection.close();