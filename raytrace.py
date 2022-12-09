import tweepy
import requests
import os
import random
from io import BytesIO

from decouple import config
from PIL import Image

from links import links

def send_tweet():
    CONSUMER_KEY = config('CONSUMER_KEY')
    CONSUMER_SECRET = config('CONSUMER_SECRET')
    ACCESS_TOKEN = config('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')
    BEARER_TOKEN = config('BEARER_TOKEN')

    # For v2 auth:
    # client = tweepy.Client(
    #    BEARER_TOKEN, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    # )
    # client.create_tweet(text="Hello, world.")

    v1_auth = auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    )

    def image_to_byte_array(image: Image) -> bytes:
        # BytesIO is a fake file stored in memory
        image_byte_array = BytesIO()
        # image.save expects a file as a argument, passing a bytes io ins
        image.save(image_byte_array, format='PNG')
        # Turn the BytesIO object back into a bytes object
        image_byte_array = image_byte_array.getvalue()
        return image_byte_array

    v1_api = tweepy.API(v1_auth)

    url = random.choice(links)

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    resizedImage = img.resize((img.size[0] * 2, img.size[1] * 2), Image.Resampling.NEAREST)
    img_bytes = image_to_byte_array(resizedImage)

    path_end = os.path.basename(os.path.normpath(url))
    v1_api.update_status_with_media(status=path_end, filename=path_end, file=img_bytes)
