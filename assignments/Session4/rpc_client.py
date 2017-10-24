## @namespace S5_rpc_client
# A client-side script that publish RPC requests
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE


import pika;
import os;
import uuid;


def request():

    # Configure connection and message
    instance_provider = "CloudAMQP";
    instance_url = "amqp://doqhhehi:Ru34cC1OhqyM3xSItAJ7qHkui68sj4KM@lark.rmq.cloudamqp.com/doqhhehi";

    full_url = os.environ.get('CLOUDAMQP_URL', instance_url);

    params = pika.URLParameters(full_url);
    params.socket_timeout = 5;

    request_queue_name="rpc_queue"
    request_content = "Hi, how are you ?";

    corr_id = str(uuid.uuid4());

    # --- STEP 1 : EMIT A REQUEST

    # Connect to request queue
    connection = pika.BlockingConnection(params);
    channel = connection.channel();

    # Create an anonymous queue for the server response
    result = channel.queue_declare(exclusive=True);
    callback_queue = result.method.queue;

    # Publish on the request queue
    channel.basic_publish(exchange='',
                          routing_key='rpc_queue',
                          properties=pika.BasicProperties(
                              reply_to=callback_queue,
                              correlation_id=corr_id, ),
                          body=request_content);

    # Report he request
    print("--- Request published ---\n");
    print("Destination Queue : {ip}.{q}".format(ip=instance_provider, q=request_queue_name));
    print("Request content : {b}".format(b=request_content));

    # --- STEP 2 : WAIT FOR A RESPONSE

    response_content = None;

    ## The callback method, launched on every response consumption.
    #
    # @param ch the input channel
    # @param method
    # @param properties
    # @param body unneeded body of the request
    def on_response(ch, method, properties, body):
        if corr_id == properties.correlation_id:

            # Report the response
            global response_content;
            response_content = str(body);

            print("--- Response received ---\n");
            print("Source queue : {ip}.{q}".format(ip=instance_provider, q=callback_queue));
            print("Response content : {b}".format(b=response_content));

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

    while response_content is None:
        connection.process_data_events();

    # Disconnect
    connection.close();

# If run from Shell, execute:
request();