#!/usr/bin/env python

## @namespace S4_simple_queue_read
# A simple script to read incomes from a queue
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;


def read():
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

    def callback(ch, method, properties, body):
        global count;
        count += 1;
        print("--- Incoming message (num {c}) ---".format(c=count));
        print("Content : %r" % body);

    # Define a consumer behaviour
    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True);

    # Wait for incomes
    print("Waiting for incomes ... (Ctrl+C to quit)");
    channel.start_consuming();


# If run from Shell, execute:
read();