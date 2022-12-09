import tweepy
import requests
import os
from io import BytesIO

from decouple import config
from PIL import Image

from links import links

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
  imgByteArr = BytesIO()
  # image.save expects a file as a argument, passing a bytes io ins
  image.save(imgByteArr, format=image.format)
  # Turn the BytesIO object back into a bytes object
  imgByteArr = imgByteArr.getvalue()
  return imgByteArr

v1_api = tweepy.API(v1_auth)

url = random.choice(list)
path_end = os.path.basename(os.path.normpath(url))

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img_bytes = image_to_byte_array(img)

v1_api.update_status_with_media(status=path_end, filename=path_end, file=img_bytes)
