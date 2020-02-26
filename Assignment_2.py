import requests as rq
from bs4 import BeautifulSoup as bs


def scraper(www, maxiter):
    company = open("Company.txt", "w+")
    for i in range(maxiter):
        r = rq.get(www)
        content = bs(r.text, "html.parser")
        tags = list(content.findAll("li"))
        for tag in tags:
            tag2 = tag.text
            if "Name" in tag2:
                myname = tag2.replace("Name: ", "")
            if "Purpose" in tag2:
                mypurpose = tag2.replace("Purpose: ", "")
                company.write(f"{i}) {myname} \n {mypurpose}\n")
    company.close()


scraper(" http://18.207.92.139:8000/random_company", 50)
