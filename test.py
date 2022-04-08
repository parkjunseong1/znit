from urllib import response
import urllib.request as req
import time
from urllib.error import HTTPError, URLError

result = open("url_list_result.txt", "w", encoding="utf8")
with open("url_list.txt", "r", encoding="utf8") as f:
    lines = f.read().splitlines()
    for i, url in enumerate(lines):
        try:
            response = req.urlopen(url)
            contents = response.read()
        except HTTPError as e:
            print(url, "   " "|실패|", e.code, file = result)
        except URLError as e:
            print(url, "   " "|검증필요|", e.reason, file = result)
        else: 
            print(url, "   " "|성공|", file = result)
f.close()
result.close()