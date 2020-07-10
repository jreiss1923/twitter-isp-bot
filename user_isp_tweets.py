import twitter
import speedtest

text_file = input("Put the name of your text file here")
codes = open(text_file, "r")

ACCESS_TOKEN = codes.readline().rstrip()
ACCESS_SECRET = codes.readline().rstrip()
KEY = codes.readline().rstrip()
KEY_SECRET = codes.readline().rstrip()
UPLOAD_SPEED = float(codes.readline().rstrip())
DOWNLOAD_SPEED = float(codes.readline().rstrip())
ISP_HANDLE = codes.readline().rstrip()

api = twitter.Api(KEY, KEY_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

st = speedtest.Speedtest()
dl = st.download()/1000000
ul = st.upload()/1000000

if ul < UPLOAD_SPEED * 0.75 or dl < DOWNLOAD_SPEED * 0.75:
    tweet_str = ISP_HANDLE + " I pay for 25 download 5 upload but I'm getting " + str(dl) + " down and "\
                + str(ul) + " up mbps"
    api.PostUpdate(tweet_str)
    print(tweet_str)
else:
    print("The internet speed is currently good.")