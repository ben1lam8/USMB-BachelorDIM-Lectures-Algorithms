#!/usr/bin/env python

## @namespace S5_rpc_server
# A server-side script that handles RPC requests
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;
import msgpack;
import msgpack_numpy;

# Configure connection
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

queue_name = "rpc_queue";

connection = pika.BlockingConnection(params);

channel = connection.channel();
channel.queue_declare(queue=queue_name);


## The callback method, launched on every request consumption. Publishes a response.
#
# @param ch the input channel
# @param method
# @param properties
# @param body unneeded body of the request
def on_request(ch, method, properties, body):

    print("Request Received. Reading...");
    decoded_request = msgpack.unpackb(body, object_hook=msgpack_numpy.decode);
    print("Request content : %r" % decoded_request);

    response_content = {'type': 1, 'value': 'Fine and you ?'};
    encoded_response = msgpack.packb(response_content, default=msgpack_numpy.encode);
    print("Response content : %r" % response_content);

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=properties.correlation_id),
                     body=encoded_response);
    ch.basic_ack(delivery_tag=method.delivery_tag); #Acknowledge

    print("Response sent.");


# Define a consumer behaviour (here : automatic message deletion)
channel.basic_qos(prefetch_count=1);
channel.basic_consume(on_request, queue=queue_name);

# Wait for requests
print('Wait for requests... ');
channel.start_consuming();
