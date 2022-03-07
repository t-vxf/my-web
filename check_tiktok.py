from flask import *
import requests
from user_agent import generate_user_agent

app = Flask(__name__)

@app.route('/',methods=['GET'])
def login():

    email = str(request.args.get('email'))
    

    

    url = 'https://api2-16-h2.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=7.6.0&language=ar&app_name=musical_ly&vid=0E79DB92-DA95-4E99-9BA7-B088D72E5D07&app_version=7.6.0&is_my_cn=0&channel=App%20Store&mcc_mnc=&device_id=6999590732555060741&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1242&openudid=88c55f9b8678397c9c9d1d82de4fbf670c111913&os_api=18&ac=WIFI&os_version=12.5.4&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=76001&iid=7015664187839334150&device_type=iPhone7,1&idfa=20DB6089-D1C6-49EF-8943-9C310C8F1B5D&mas=0044c833f3d8474e80e76d88054fbaf69deb1c6f34df2bb0b2a281&as=a1568a75462231ca7c5236&ts=1633462822'

    head = {
        'Host': 'api2-16-h2.musical.ly',
   'Accept': '*/*',
   'Content-Type': 'application/x-www-form-urlencoded',
   'Accept-Encoding': 'gzip, deflate',
   'User-Agent': 'Musically/7.6.0 (iPhone; iOS 12.5.4; Scale/3.00)',
   'Accept-Language': 'ar-SA;q=1',
   'Content-Length':''
    }
   
    data = {
        "email": str(email),
     }

    response = requests.post(url2,headers=headers2,data=data2).text
    if '"Sorry, you sent email too often, please retry in 3 minutes later."'in response:
        return {
            'email': 'Sorry, you sent email too often, please retry in 3 minutes later.',
            'Status': 'error',
            'By': '@bbzzs',
        }
    elif '"Bind device by email failed"'in response :
        return {
            'email': email,
            'Because': 'Bind device by email failed',
            'Status': 'not linked',
            'By': '@zzaaz',
        }
    elif  "Sent successfully" in response :
        return {
            'email': email,
            'insta': '@06lme',
            'Status': 'linked',
            'By tele': '@bbzzs',
        }
    else:
        return {
            'Username': username,
            'Password': password,
            'Status': 'Wait...',
            'By': '@zzaaz',
        }



if __name__ == "__main__":
    app.run()
