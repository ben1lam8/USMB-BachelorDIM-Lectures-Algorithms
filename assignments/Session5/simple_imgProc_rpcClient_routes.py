#!/usr/bin/env python

## @namespace S5_simple_imgProc_rpcClient_routes
# A client-side script that publish images as RPC requests
# The anonymous response queue could be disconnected if the input image leads to a long server-side process...
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE


import pika;
import os;
import uuid;
import msgpack;
import msgpack_numpy;
import cv2;
import random;


# Configure connection and message
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

exchange_name = 'imgProc';
corr_id = str(uuid.uuid4());

# --- STEP 1 : EMIT A REQUEST ON A FILTER QUEUE

# Manage filters and select one
filter_types = {
    "invert": "invert image colors",
    "threshold": "threshold an image"};
lucky_filter = random.choice(list(filter_types));
print("Lucky filter : {lf}".format(lf=lucky_filter));

# Connect to exchange, create queues and bindings
connection = pika.BlockingConnection(params);
channel = connection.channel();

channel.exchange_declare(exchange=exchange_name,
                         exchange_type='direct');

for key, value in filter_types.iteritems():
    channel.queue_bind(exchange=exchange_name,
                       queue=key,
                       routing_key=key);

# Create an anonymous queue for the server response
result = channel.queue_declare(exclusive=True);
callback_queue = result.method.queue;

# Write the request
request_content = cv2.imread('assignments/Session5/myimage2.jpeg', 1);
encoded_request = msgpack.packb(request_content, default=msgpack_numpy.encode)

# Publish on the corresponding queue
channel.basic_publish(exchange=exchange_name,
                      routing_key=lucky_filter,
                      properties=pika.BasicProperties(
                          reply_to=callback_queue,
                          correlation_id=corr_id, ),
                      body=encoded_request);

# Report he request
print("--- Image published ---\n");
print("Destination Queue : {ip}.{q}".format(ip=instance_provider, q=lucky_filter));

# --- STEP 2 : WAIT FOR A RESPONSE

decoded_response = None;


## The callback method, launched on every response consumption.
#
# @param ch the input channel
# @param method
# @param properties
# @param body unneeded body of the request
def on_response(ch, method, properties, body):
    if corr_id == properties.correlation_id:

        # Report the response
        global decoded_response;
        decoded_response = msgpack.unpackb(body, object_hook=msgpack_numpy.decode);

        print("--- Image received ---\n");
        print(decoded_response);
        print("Displaying the response...");
        cv2.imshow("Transformed image", decoded_response);
        cv2.waitKey(0);

    else:
        raise ValueError('Warning : the client received a corrupted response');


# Define a consumer behaviour for the response queue (here : automatic message deletion)
channel.basic_consume(on_response,
                      queue=callback_queue,
                      no_ack=True);

# Wait for responses
print('Wait for responses... ');

channel.basic_consume(on_response,
                      no_ack=True,
                      queue=callback_queue);

while decoded_response is None:
    connection.process_data_events();

# Disconnect
connection.close();