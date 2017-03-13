#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver


def get_tr_id(html_):
    matches = []
    try:
        soup = BeautifulSoup(html_, "html.parser")
        trs = soup.findAll("tr", {"id": re.compile("d[0-9]+")})
        for tr in trs:
            if tr.find("span", {"class": "hot"}):
                matches.append(tr.get("id"))
    except AttributeError as e:
        print(e)
        return None
    return matches


driver = webdriver.Firefox(executable_path='D:\\Program Files (x86)\\Mozilla Firefox\\geckodriver.exe')
driver.get('http://bf2.310v.com:3389/index.html')
driver.implicitly_wait(5)
html = driver.page_source
matches = get_tr_id(html)

output_html = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n"

for index in range(len(matches)):
    # match_url = "http://ny.310v.com:3389/match_fx/bf.html?mid=" + matches[index][1:]
    # print(match_url)
    # driver.get(match_url)
    # driver.implicitly_wait(5)
    # html = driver.page_source
    # soup = BeautifulSoup(html, "html.parser")
    #
    # host = str(soup.find("td", {"id":"id_tx"}))
    # guest = str(soup.find("td", {"id":"id_ty"}))
    # score = str(soup.find("td", {"id":"id_bf"}))
    # odds_time = str(soup.find("td", {"id":"odds_time"}))
    # bet_odds = str(soup.find("td", {"id":"bet_odds"}))

    # output_html += "<table><tr>"+host+score+guest+"</tr>"+"<tr>"+odds_time+"</tr>"+"<tr>"+bet_odds+"</tr></table>\r\n"

    fenxi_url = "http://ny.310v.com:3389/match_fx/fenxi_html.html?mid=" + matches[index][1:]
    print(fenxi_url)
    driver.get(fenxi_url)
    driver.implicitly_wait(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    odds = str(soup.find("table", {"id":"id_tb_dw"}))
    aomen = str(soup.find("table", {"id":"bbdg_7"}))
    output_html += odds+"\r\n"+aomen

print(output_html)

file_object = codecs.open("E:/tools/hot.htm", "w", "utf-8")
file_object.write(output_html)
file_object.close( )
