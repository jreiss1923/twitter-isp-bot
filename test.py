import twitter
import speedtest
import time

codes = open("twitter_codes.txt", "r")
ACCESS_TOKEN = codes.readline().rstrip()
ACCESS_SECRET = codes.readline().rstrip()
KEY = codes.readline().rstrip()
KEY_SECRET = codes.readline().rstrip()

api = twitter.Api(KEY, KEY_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

st = speedtest.Speedtest()

while True:
    print(api.PostUpdate("My current internet speed is " + str(round(st.download()/1000000, 2)) + " Mbps"))
    time.sleep(3600)








