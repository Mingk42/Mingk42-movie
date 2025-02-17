from movie.api.call import gen_url, req, get_key, req2list, list2df, save2df
import pandas as pd

def test_비밀키가소스코드에중복되면안됨():
    key=get_key()
    assert key

def test_gen_url():
    url = gen_url()
    assert True
    assert "http" in url



def test_req():
    code, data=req()
    assert code==200

    code,data=req(20240725)
    assert code==200


def test_resp():
    data,date=req2list()
    assert isinstance(data,list)

def test_df():
    df,dt=list2df()
    print(df)
    print(dt.split("~")[0])
    assert "rnum" in df.columns
    assert "openDt" in df.columns
    assert "movieNm" in df.columns
    assert "audiAcc" in df.columns

def test_save():
    df=save2df()
    assert isinstance(df,pd.DataFrame)