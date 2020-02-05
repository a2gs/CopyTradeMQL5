#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)
import sys
import zmq

port = "5563"

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from server...")
socket.connect (f"tcp://localhost:{port}")

while True:
    print("Waiting...")
    topicfilter = b"10101"
    socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

    msg = socket.recv()

    print(f"Recv: [{msg}]")

print("Pausa.")
input()
