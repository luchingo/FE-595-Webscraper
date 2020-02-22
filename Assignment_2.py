import requests as rq
from bs4 import BeautifulSoup as bs


def scraper(www, maxiter):
    Company = open("Company.txt", "w+")
    for i in range(maxiter):
        r = rq.get(www)
        content = bs(r.text, "html.parser")
        tags = list(content.findAll("li"))
        for tag in tags:
            tag2 = tag.text
            if "Name" in tag2:
                mytag = tag2.replace("Name: ", "")
                Company.write(str(i) + ")" + mytag + "\n")
            if "Purpose" in tag2:
                mytag = tag2.replace("Purpose: ", "")
                Company.write("  " + mytag + "\n")


scraper(" http://18.207.92.139:8000/random_company", 50)
