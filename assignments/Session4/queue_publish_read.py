#!/usr/bin/env python

## @namespace S4_queue_publish_read
# A simple script to publish or read a test message
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import argparse;
import subprocess;

# Parse command line arguments
parser = argparse.ArgumentParser();
parser.add_argument("-r", "-read", action="store_true", help="Start a reader");
parser.add_argument("-t", "-test", action="store_true", help="Play a concurrency test scenario");
args = parser.parse_args();

if args.t:
    # FIX : Find a better way to launch subprocesses and print their outputs
    # Launch 1 provider (don't forget to provide a message content ...)
    subprocess.check_output("python simple_queue_publish.py -c -n 25", shell=True);

    # Launch 2 readers
    subprocess.check_output("python simple_queue_read.py -c", shell=True);
    subprocess.check_output("python simple_queue_read.py -c", shell=True);

elif args.r:
    execfile('simple_queue_read.py');
else:
    execfile('simple_queue_publish.py');