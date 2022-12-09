# -*- coding: utf-8 -*-
from raytrace import send_tweet

def handler(event, context):
    # Your code goes here!
    send_tweet()
    # e = event.get("e")
    # pi = event.get("pi")
    # return e + pi
    return "tweet sent"
