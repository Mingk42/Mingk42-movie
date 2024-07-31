import requests as reqs
import os
import pandas as pd

def gen_url(dt="20120101", req_val={"multiMovieYn":"N"}):
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key=get_key()
    url=f"{base_url}?key={key}&targetDt={dt}"
    for key, value in req_val.items():
        url += f"&{key}={value}"
    print(url)
    return url


def req(dt="20120101", url_param={}):
    url=gen_url(dt,req_val=url_param)
    resp=reqs.get(url)

    code=resp.status_code
    data=resp.json()

    # print(data)

    return code, data


def get_key():
    key=os.getenv("MOVIE_API_KEY")
    return key

  
def req2list(dt="20120101", url_param={}) -> list:
    _,data=req(dt,url_param=url_param)
    _list = data["boxOfficeResult"]["dailyBoxOfficeList"]
    
    return _list


def list2df(dt="20120101", url_param={}):
    l=req2list(dt,url_param=url_param)
    df=pd.DataFrame(l)

    return df


def save2df(dt="20120101", url_param={}):
    df = list2df(dt,url_param=url_param)
    # df에 load_dt 컬럼 추가 (yyyymmdd형식으로)
    df['load_dt']=dt
    # 아래 파일 저장시 load_dt기준으로 파티셔닝
    df.to_parquet("~/tmp/test_parquet/",partition_cols=['load_dt'])

    return df

def apply_type2df(load_dt="20120101", path="~/tmp/test_parquet"):
    df = pd.read_parquet(f"{path}/load_dt={load_dt}")
    """
    df["rnum"]=df["rnum"].apply(pd.to_numeric)
    df["rank"]=df["rank"].apply(pd.to_numeric)
    df["rankInten"]=df["rankInten"].apply(pd.to_numeric)
    df["salesAmt"]=df["salesAmt"].apply(pd.to_numeric)
    df["salesShare"]=df["salesShare"].apply(pd.to_numeric)
    df["salesInten"]=df["salesInten"].apply(pd.to_numeric)
    df["salesChange"]=df["salesChange"].apply(pd.to_numeric)
    """
    for c in ["rnum", "rank", "rankInten", "salesAmt", "salesShare", "salesInten", "salesChange", "salesAcc", "audiCnt", "audiInten", "audiChange", "audiAcc", "scrnCnt", "showCnt"]:
        df[c] = df[c].apply(pd.to_numeric)

    return df

def echo(yaho):
    return yaho
