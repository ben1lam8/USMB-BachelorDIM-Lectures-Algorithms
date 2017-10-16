#!/usr/bin/env python

## @namespace S4_queue_publish_read
# A simple script to publish or read a test message
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import imp;
import argparse;

simple_queue_publish = imp.load_source('S4_simple_queue_publish', 'assignments/Session4/S4_simple_queue_publish.py');
simple_queue_read = imp.load_source('S4_simple_queue_read', 'assignments/Session4/S4_simple_queue_read.py');


def execute():

    # Get the parser instance
    parser = argparse.ArgumentParser();
    parser.add_argument("-read", action="store_true");
    args = parser.parse_args();

    if args.read:
        simple_queue_read.read();
    else:
        simple_queue_publish.publish();


# If run from Shell, execute:
execute();