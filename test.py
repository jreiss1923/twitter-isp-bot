import twitter
import speedtest

codes = open("twitter_codes.txt", "r")
ACCESS_TOKEN = codes.readline().rstrip()
ACCESS_SECRET = codes.readline().rstrip()
KEY = codes.readline().rstrip()
KEY_SECRET = codes.readline().rstrip()

api = twitter.Api(KEY, KEY_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

st = speedtest.Speedtest()
#print(st.download()/1000000)

status = api.PostUpdate("My current internet speed is " + str(st.download()/1000000) + "Mbps")








