from movie.api.call import gen_url, req, get_key, req2list, list2df, save2df, apply_type2df, echo
import pandas as pd

def test_비밀키가소스코드에중복되면안됨():
    key=get_key()
    assert key

def test_gen_url():
    url = gen_url()
    assert True
    assert "http" in url

    d = {"multiMovieYn":"N"}
    url = gen_url(req_val=d)




def test_req():
    code, data=req()
    assert code==200

    code,data=req(20240725)
    assert code==200


def test_resp():
    data=req2list()
    assert isinstance(data,list)

def test_df():
    df=list2df()
    assert "rnum" in df.columns
    assert "openDt" in df.columns
    assert "movieNm" in df.columns
    assert "audiAcc" in df.columns

def test_save():
    df=save2df()
    assert isinstance(df,pd.DataFrame)
    assert "load_dt" in df.columns
    assert len(df) == 10


def test_apply_type2df():
    df=apply_type2df()
    assert isinstance(df,pd.DataFrame)
    df2=apply_type2df(20240724)
    assert isinstance(df2,pd.DataFrame)
    print()
    print(df)
    for c in ["rnum", "rank", "rankInten", "salesAmt", "salesShare", "salesInten", "salesChange", "salesAcc", "audiCnt", "audiInten", "audiChange", "audiAcc", "scrnCnt", "showCnt"]:
        assert df2[c].dtype in ["int64", "float64"]
    print(df.dtypes)

def test_echo():
    msg="test"
    e_rst=echo(msg)
    assert e_rst==msg
