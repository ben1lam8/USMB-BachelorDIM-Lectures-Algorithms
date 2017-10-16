#!/usr/bin/env python

## @namespace S4_simple_queue_publish
# A simple script to publish a test message
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;


def publish():

    # Configure connection and message
    instance_provider = "CloudAMQP";
    instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

    full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

    params = pika.URLParameters(full_url);
    params.socket_timeout = 5;

    queue_name = "presentation";
    message_content = raw_input("Please enter your name : ");

    # Connect
    connection = pika.BlockingConnection(params);

    # Publish
    channel = connection.channel();
    channel.basic_publish(exchange='',
                         routing_key=queue_name,
                         body=message_content);

    # Report
    print("--- Message published ---\n");
    print("Destination Queue : {ip}.{q}".format(ip=instance_provider, q=queue_name));
    print("Message content : {b}".format(b=message_content));

    # Disconnect
    connection.close();

# If run from Shell, execute:
publish();