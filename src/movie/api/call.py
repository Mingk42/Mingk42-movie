import requests as reqs
import os
import pandas as pd

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
  
def req2list() -> list:
    _,data=req()
    _list = data["boxOfficeResult"]["dailyBoxOfficeList"]
    d=data["boxOfficeResult"]["showRange"]
    
    return _list,d


def list2df():
    l,d=req2list()
    df=pd.DataFrame(l)

    return df,d


def save2df():
    df,d = list2df()
    # df에 load_dt 컬럼 추가 (yyyymmdd형식으로)
    df['load_dt']=d.split("~")[0]
    # 아래 파일 저장시 load_dt기준으로 파티셔닝
    df.to_parquet("~/tmp/test_parquet/",partition_cols=['load_dt'])

    return df
