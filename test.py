import twitter
import speedtest

codes = open("C:\\Users\\Joshua\\PycharmProjects\\Twitter\\twitter_codes.txt", "r")
ACCESS_TOKEN = codes.readline().rstrip()
ACCESS_SECRET = codes.readline().rstrip()
KEY = codes.readline().rstrip()
KEY_SECRET = codes.readline().rstrip()

UPLOAD_SPEED = 5.0
DOWNLOAD_SPEED = 25.0

api = twitter.Api(KEY, KEY_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

st = speedtest.Speedtest()
dl = round(st.download()/1000000, 2)
ul = round(st.upload()/1000000, 2)

if ul < UPLOAD_SPEED * 0.75 or dl < DOWNLOAD_SPEED * 0.75:
    print(api.PostUpdate("@Optimum @OptimumHelp I pay for 25 download 5 upload but I'm getting " +
                         str(dl) + " down and " + str(ul) + " up mbps"))
else:
    print("The internet speed is currently good.")








