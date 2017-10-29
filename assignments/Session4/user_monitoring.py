#!/usr/bin/env python

## @namespace S4_user_monitoring
# A simple script to read presentation posts in an exchange
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;
import time;

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

count = 0;
users_in_channel = {};

## The callback behaviour for a busy reader
#
# @param ch
# @param method
# @param properties
# @param body
def callback(ch, method, properties, body):

    global users_in_channel;

    content = body.split('>>');
    calling_user = content[0];
    called_channel = content[1];

    if called_channel not in users_in_channel or calling_user not in users_in_channel[called_channel]:
        users_in_channel[called_channel] = calling_user;

        print("--- {u} joined the \"{c}\" channel ---".format(u=calling_user, c=called_channel));


# Define a consumer behaviour
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True);

# Wait for incomes
print("Waiting for incomes ... (Ctrl+C to quit)");
channel.start_consuming();