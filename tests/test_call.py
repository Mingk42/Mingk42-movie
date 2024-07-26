from movie.api.call import gen_url, req, get_key, req2df

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
    data=req2df()
    assert isinstance(data,list)
