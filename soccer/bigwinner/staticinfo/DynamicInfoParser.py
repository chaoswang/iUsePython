#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from com.github.chaoswang.soccer.bigwinner.logger.LoggingConfig import LoggingConfig
from com.github.chaoswang.soccer.bigwinner.staticinfo.DynamicInfo import insertOne

class DynamicInfoParser:
    def __init__(self):
        self.__driver = webdriver.PhantomJS(executable_path='E:\\soccer\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
        self.__driver.get('http://ny.310v.com:3389/dt/over.html?md=2018-05-15')
        self.__driver.implicitly_wait(20)
        time.sleep(2)
        # 切换到前1天的历史场次
        self.__driver.find_element_by_xpath("//td[@onclick='select_date(3,1)']").click()
        # 切换到前2天的历史场次
        # self.__driver.find_element_by_xpath("//td[@onclick='select_date(3,1)']").click()
        time.sleep(3)

    @property
    def web_driver(self):
        return self.__driver

    @property
    def match_id(self):
        page_source = self.__driver.page_source
        matches = []
        try:
            soup = BeautifulSoup(page_source, "html.parser")
            imgs = soup.findAll("img", {"src": "/images/fx2.gif"})
            for img in imgs:
                idStr = img.get("onclick")
                id = idStr[idStr.index("(") + 1:idStr.index(",")]
                matches.append(id)
        except AttributeError as e:
            print(e)
            return None
        print(matches)
        return matches


if __name__ == '__main__':
    parser = DynamicInfoParser()
    driver = parser.web_driver
    matches = parser.match_id
    log = LoggingConfig()
    logger = log.logger
    for index in range(len(matches)):
        try:
            match_url = "http://ny.310v.com:3389/match_fx/bf.html?mid=" + matches[index]
            driver.get(match_url)
            driver.implicitly_wait(3)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            Score = str(soup.find("td", {"id": "id_bf"}).get_text())
            if Score.strip():
                insertOne(matches[index], Score)
        except BaseException as e:
            logger.info(e)
            continue