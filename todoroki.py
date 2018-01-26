from bs4 import BeautifulSoup
import os
import requests
import time


# プロキシ設定を書き込む。ない場合は空の辞書やNoneを入れる。
proxies = {
  "http": "202.211.8.4:8080",
  "https": "202.211.8.4:8080"
}

res = requests.get("http://www5a.biglobe.ne.jp/~todoroki/nct.htm", proxies=proxies)
soup = BeautifulSoup(res.text, "html.parser")

target = [x.get("href") for x in soup.find_all("a") \
              if isinstance(x.get("href"), str) and "data" in x.get("href")]

if not os.path.exists("Todoroki"):
    os.mkdir("Todoroki")

for url in target:
    res = requests.get("http://www5a.biglobe.ne.jp/~todoroki/" + url, proxies=proxies)
    print("download:"+"http://www5a.biglobe.ne.jp/~todoroki/" + url)
    with open("Todoroki/" + os.path.split(url)[1], "wb") as f:
        f.write(res.content)

    time.sleep(2)
