
# Simple Method
# import requests
# from bs4 import BeautifulSoup
#
# url="https://www.linkedin.com/feed/"
#
# response = requests.get(url)
#
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())


from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/news")
def get_news():
    url="https://indianexpress.com/"

    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    title=[]
    for item in soup.find_all("h4",class_="o-commonList__txt"):
        title.append(item.text)

    return {
        "news":title
    }
