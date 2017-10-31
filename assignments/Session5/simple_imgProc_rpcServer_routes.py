#!/usr/bin/env python

## @namespace S5_simple_imgProc_rpcServer_routes
# A server-side script that handles images as RPC requests and process them
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pika;
import os;
import msgpack;
import msgpack_numpy;
import argparse;
import imp;
imgproc_tools = imp.load_source('S3_imgproc_tools', 'assignments/Session3/S3_imgproc_tools.py');

# Parse command line arguments
parser = argparse.ArgumentParser();
parser.add_argument('-q', '-queue', action='store', dest='queue', help='The queue to subscribe to');
args = parser.parse_args();

# Configure connection
instance_provider = "CloudAMQP";
instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

params = pika.URLParameters(full_url);
params.socket_timeout = 5;

request_queue_name = args.queue;

connection = pika.BlockingConnection(params);

channel = connection.channel();
channel.queue_declare(queue=request_queue_name);


## The callback method, launched on every request consumption. Publishes a response.
#
# @param ch the input channel
# @param method
# @param properties
# @param body unneeded body of the request
def on_request(ch, method, properties, body):

    print("Request Received. Reading...");
    decoded_request = msgpack.unpackb(body, object_hook=msgpack_numpy.decode);

    print("Processing the image...")

    if request_queue_name == "invert":
        response_content = imgproc_tools.invert_colors_manual(decoded_request);
    elif request_queue_name == "threshold":
        response_content = imgproc_tools.threshold_colors_opencv(decoded_request)[1];
    else:
        raise ValueError('Route not supported yet');

    print("Image processed. Writing response...");
    encoded_response = msgpack.packb(response_content, default=msgpack_numpy.encode);

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=properties.correlation_id),
                     body=encoded_response);
    ch.basic_ack(delivery_tag=method.delivery_tag); #Acknowledge

    print("Response sent.");


# Define a consumer behaviour (here : automatic message deletion)
channel.basic_qos(prefetch_count=1);
channel.basic_consume(on_request, queue=request_queue_name);

# Wait for requests
print('Wait for requests... ');
channel.start_consuming();