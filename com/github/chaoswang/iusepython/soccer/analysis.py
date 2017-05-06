#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def get_tr_id(html_):
    matches = []
    try:
        soup = BeautifulSoup(html_, "html.parser")
        trs = soup.findAll("tr", {"id": re.compile("d[0-9]+")})
        for tr in trs:
            # if tr.find("span", {"class": "hot"}):
            matches.append(tr.get("id"))
    except AttributeError as e:
        print(e)
        return None
    return matches


driver = webdriver.PhantomJS(executable_path="E:\\tools\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get('http://bf2.310v.com:3389/index.html')
driver.implicitly_wait(5)
time.sleep(2)
html = driver.page_source
matches = get_tr_id(html)

output_html = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n"

for index in range(len(matches)):
    fenxi_url = "http://ny.310v.com:3389/match_fx/fenxi_html.html?mid=" + matches[index][1:]
    print(fenxi_url)
    driver.get(fenxi_url)
    driver.implicitly_wait(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    odds = str(soup.find("table", {"id":"id_tb_dw"}))
    aomen = str(soup.find("table", {"id":"bbdg_7"}))
    if aomen.strip().find("信心指數") == -1:
        continue

    match_url = "http://ny.310v.com:3389/match_fx/bf.html?mid=" + matches[index][1:]
    driver.get(match_url)
    driver.implicitly_wait(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    host = str(soup.find("td", {"id":"id_tx"}))
    guest = str(soup.find("td", {"id":"id_ty"}))
    score = str(soup.find("td", {"id":"id_bf"}))

    output_html += "<table><tr>"+host+score+guest+"</tr></table>\r\n"
    output_html += odds+"\r\n"+aomen

file_object = codecs.open("E:/足球分析/复盘/hot_"+ time.strftime('%Y-%m-%d',time.localtime(time.time())) +".htm", "w", "utf-8")
file_object.write(output_html)
file_object.close( )
