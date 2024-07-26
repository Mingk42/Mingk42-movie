

def req(dt="20120101"):
    base_url="http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key="a9e30c07ca970246b988e9857af2f1a4"

    url=f"{base_url}?key={key}&targetDt={dt}"

    print(url)
