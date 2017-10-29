#!/usr/bin/env python

## @namespace S4_concurrent_publish_read_routine
# A simple script to publish a bunch of messages and test AMQP concurrency
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import argparse;
import subprocess;
import sys;

parser = argparse.ArgumentParser();
parser.add_argument('-n', '-number', type=int, default=1, help='Amount of test messages to send');
parser.add_argument('-r', '-readers', type=int, default=2, help='Amount of concurrent readers to create');
args = parser.parse_args()

print("--- [Launching {n} messages from 1 provider to {r} readers] ---".format(n=args.n, r=args.r));

# Launch 1 provider
processes = [
    subprocess.Popen("python simple_queue_publish.py -c -n {n}".format(n=args.n),
                     stdout=subprocess.PIPE,
                     stdin=sys.stdin,
                     shell=True)];

# Launch r readers
i = 0;
while i < args.r:
    processes.append(subprocess.Popen("python simple_queue_read.py -c", stdout=subprocess.PIPE, shell=True));
    i += 1;

# Ugly IPC... Please provide message content input, even if not displayed...
# CloudAMQP dashboard shows a correct behaviour
# FIX: find a (better) way to display (every) subprocess output
while True:
    for process in processes:
        print(process.stdout.read());
