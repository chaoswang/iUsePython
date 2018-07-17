#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import codecs
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def get_match_id(html_):
    matchids = []
    try:
        soup = BeautifulSoup(html_, "html.parser")
        imgs = soup.findAll("img", {"src":"/images/fx2.gif"})
        for img in imgs:
            idStr = img.get("onclick")
            id = idStr[idStr.index("(") + 1:idStr.index(",")]
            matchids.append(id)
    except AttributeError as e:
        print(e)
        return None
    print(matchids)
    return matchids

driver = webdriver.PhantomJS(executable_path="E:\\soccer\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get('http://ny.310v.com:3389/dt/over.html?md=2017-04-21')
driver.implicitly_wait(20)
time.sleep(3)
#切换到2017-04-20的历史场次
driver.find_element_by_xpath("//td[@onclick='select_date(5,1)']").click()
time.sleep(3)
html = driver.page_source
matchids = get_match_id(html)
print ("开始时间：" + time.strftime("%H:%M:%S"))

output_html = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n"
for index in range(len(matchids)):
    fenxi_url = "http://ny.310v.com:3389/match_fx/fenxi_html.html?mid=" + matchids[index]
    driver.get(fenxi_url)
    driver.implicitly_wait(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    odds = str(soup.find("table", {"id":"id_tb_dw"}))
    aomen = str(soup.find("table", {"id":"bbdg_7"}))
    #没有澳门心水直接跳过
    if aomen.strip().find("信心指數") == -1:
        continue

    match_url = "http://ny.310v.com:3389/match_fx/bf.html?mid=" + matchids[index]
    print(match_url)
    driver.get(match_url)
    driver.implicitly_wait(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    host = str(soup.find("td", {"id":"id_tx"}))
    guest = str(soup.find("td", {"id":"id_ty"}))
    score = str(soup.find("td", {"id":"id_bf"}))

    output_html += "<table><tr>"+host+score+guest+"</tr></table>\r\n"
    output_html += odds+"\r\n"+aomen

file_object = codecs.open("E:/soccer/review/history_2017-04-16.htm", "w", "utf-8")
file_object.write(output_html)
file_object.close( )
