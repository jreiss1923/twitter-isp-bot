import twitter
import speedtest
import mysql.connector
from datetime import datetime

codes = open("C:\\Users\\Joshua\\PycharmProjects\\Twitter\\twitter_codes.txt", "r")

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=codes.readline().rstrip(),
  database="internet_information"
)

cursor = db.cursor()


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

now = datetime.now()
now_string = now.strftime('%Y-%m-%d %H:%M:%S')

insert_statement = "INSERT INTO speed_stats (download_speed, upload_speed, time_recorded) values (" + \
                   str(dl) + "," + str(ul) + ", '" + now_string + "' )"

cursor.execute(insert_statement)
db.commit()

if ul < UPLOAD_SPEED * 0.75 or dl < DOWNLOAD_SPEED * 0.75:
    tweet_str = "@Optimum @OptimumHelp I pay for 25 download 5 upload but I'm getting " + str(dl) + " down and "\
                + str(ul) + " up mbps"
    api.PostUpdate(tweet_str)
    print(tweet_str)
else:
    print("The internet speed is currently good.")








