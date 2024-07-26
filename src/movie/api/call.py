import requests as reqs
import os

def gen_url(dt="20120101"):
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key=get_key()
    url=f"{base_url}?key={key}&targetDt={dt}"

    return url


def req(dt="20120101"):
    url=gen_url(dt)
    resp=reqs.get(url)

    code=resp.status_code
    data=resp.json()

    # print(data)

    return code, data


def get_key():
    key=os.getenv("MOVIE_API_KEY")
    return key



def req2df():
    _,data=req()
    _list = data["boxOfficeResult"]["dailyBoxOfficeList"]
    return _list
