import requests
import webbrowser
from requests_toolbelt import MultipartEncoder

def openBrowser():

    client_id = "2407786039"  # App Key
    client_secret = "90d4cd8a572020ca22999daf75af3468"  # App Secret
    url_authorize = "https://api.weibo.com/oauth2/authorize"
    url_get_token = "https://api.weibo.com/oauth2/access_token"
    redirect_uri = "https://api.weibo.com/oauth2/default.html"

    webbrowser.open("{}?client_id={}&redirect_uri={}&response_type=code".format(url_authorize, client_id, redirect_uri), new=0, autoraise=True)

def get_token(code0):

    #code = input("Input the code\n")
    code = code0

    client_id = "2407786039"  # App Key
    client_secret = "90d4cd8a572020ca22999daf75af3468"  # App Secret
    url_authorize = "https://api.weibo.com/oauth2/authorize"
    url_get_token = "https://api.weibo.com/oauth2/access_token"
    redirect_uri = "https://api.weibo.com/oauth2/default.html"

    payload = {
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": redirect_uri
                 }

    r = requests.post(url_get_token, data=payload)
    if 'access_token' in r.json().keys():
        return (True, r.json()['access_token'])
    else:
        return (False, "0")
    #return r.json()['access_token']


def post_a_pic(picture, token, news="from ImageStyleTrans"):

    url_share = "https://api.weibo.com/2/statuses/share.json"
    access_token = token
    status = news + "https://github.com/"
    pic = picture

    m = MultipartEncoder(
        fields={'access_token': access_token, 'status': status, 'pic': (pic, open(pic, 'rb'))}
        )

    r = requests.post(url_share, data=m, headers={'Content-Type': m.content_type})
