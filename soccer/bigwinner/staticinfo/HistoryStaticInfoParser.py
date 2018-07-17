#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from soccer.bigwinner.logger.LoggingConfig import LoggingConfig
from soccer.bigwinner.staticinfo.HistoryStaticInfo import insertOne
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import threading

class StaticInfoParser:
    def __init__(self):
        self.__driver = webdriver.PhantomJS(executable_path='E:\\soccer\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
        # self.__driver.get('http://bf2.310v.com:3389/index.html')
        self.__driver.get('http://ny.310v.com:3389/dt/over.html?md=2018-05-15')
        self.__driver.implicitly_wait(20)
        time.sleep(2)
        # 切换到前1天的历史场次
        self.__driver.find_element_by_xpath("//td[@onclick='select_date(3,1)']").click()
        # 切换到前2天的历史场次
        # self.__driver.find_element_by_xpath("//td[@onclick='select_date(4,1)']").click()
        time.sleep(3)

    @property
    def web_driver(self):
        return self.__driver

    # 获取历史比赛数据
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

def parse_html_into_db():
    parser = StaticInfoParser()
    driver = parser.web_driver
    matches = parser.match_id
    log = LoggingConfig()
    logger = log.logger
    for index in range(len(matches)):
        try:
            # 历史比赛数据
            analysis_url = 'http://ny.310v.com:3389/match_fx/fenxi_html.html?mid='+ matches[index]
            # 今日比赛数据
            # analysis_url = "http://ny.310v.com:3389/match_fx/fenxi_html.html?mid=" + matches[index][1:]
            logger.info(analysis_url)
            driver.get(analysis_url)
            driver.implicitly_wait(5)

            html = driver.page_source
            # print(html)
            soup = BeautifulSoup(html, 'html.parser')

            # 没有澳门心水跳过
            aomen = str(soup.find('table', {'id': 'bbdg_7'}))
            if aomen.strip().find('信心指數') == -1:
                continue

            odds_data_list, aomen_data_list = [], []
            for odds_td in soup.find('table', {'id': 'id_tb_dw'}).find_all('td'):
                td_text = odds_td.get_text()
                if not td_text.startswith('\n') and td_text:
                    odds_data_list.append(td_text)

            for aomen_td in soup.find('table', {'id': 'bbdg_7'}).find_all('td'):
                aomen_text = aomen_td.get_text()
                if not aomen_text.startswith('\n') and aomen_text:
                    aomen_data_list.append(aomen_text)

            # 历史比赛数据
            MatchId = matches[index]
            # logger.info(MatchId)
            MatchType = aomen_data_list[4]
            # logger.info(MatchType)
            MatchDate = odds_data_list[4]  # 比赛时间：2018-04-29  星期天  15:00:00
            splitted = re.search(r"(\d{4}-\d{1,2}-\d{1,2})\s*\S*\s*(\d{1,2}:\d{1,2}:\d{1,2})", MatchDate)
            MatchDate = splitted.group(1) + ' ' + splitted.group(2)
            # logger.info(MatchDate)

            Host = odds_data_list[1]  # [17] 大阪飞脚
            Host = re.search(r'.*\s+(\S+)', Host).group(1)
            # logger.info(Host)

            Guest = odds_data_list[3]  # 鸟栖沙根 [16]
            Guest = re.search(r'(\S+).*\s+', Guest).group(1)
            # logger.info(Guest)

            HostRank, GuestRank = 0,0
            pattern = re.compile(r'\d+')
            HostRankTmp = odds_data_list[1]
            m = pattern.search(HostRankTmp)
            if m:
                HostRank = m.group()
            # logger.info(HostRank)
            GuestRankTmp = odds_data_list[3]
            m = pattern.search(GuestRankTmp)
            if m:
                GuestRank = m.group()
            # logger.info(GuestRank)

            HostAsianOdds = odds_data_list[20]
            # logger.info(HostAsianOdds)
            InitialHostAsianOdds = odds_data_list[24]
            # logger.info(InitialHostAsianOdds)

            concede_dict = {'*七球半/八球': 7.75, '*七球半': 7.5, '*七球/七球半': 7.25, '*七球': 7,
                            '*六球半/七球': 6.75, '*六球半': 6.5, '*六球/六球半': 6.25, '*六球': 6,
                            '*五球半/六球': 5.75, '*五球半': 5.5, '*五球/五球半': 5.25, '*五球': 5,
                            '*四球半/五球': 4.75, '*四球半': 4.5, '*四球/四球半': 4.25, '*四球': 4,
                            '*三球半/四球': 3.75, '*三球半': 3.5, '*三球/三球半': 3.25, '*三球': 3,
                            '*两球半/三球': 2.75, '*两球半': 2.5, '*两球/两球半': 2.25, '*两球': 2,
                            '*球半/两球': 1.75, '*球半': 1.5, '*一球/球半': 1.25, '*一球': 1,
                            '*半球/一球': 0.75, '*半球': 0.5, '*平手/半球': 0.25, '平手': 0,
                            '半球/一球': -0.75, '半球': -0.5, '平手/半球': -0.25,
                            '球半/两球': -1.75, '球半': -1.5, '一球/球半': -1.25, '一球': -1,
                            '两球半/三球': -2.75, '两球半': -2.5, '两球/两球半': -2.25, '两球': -2,
                            '三球半/四球': -3.75, '三球半': -3.5, '三球/三球半': -3.25, '三球': -3,
                            '四球半/五球': -4.75, '四球半': -4.5, '四球/四球半': -4.25, '四球': -4,
                            '五球半/六球': -5.75, '五球半': -5.5, '五球/五球半': -5.25, '五球': -5,
                            '六球半/七球': -6.75, '六球半': -6.5, '六球/六球半': -6.25, '六球': -6,
                            '七球半/八球': -7.75, '七球半': -7.5, '七球/七球半': -7.25, '七球': -7}

            Concede = odds_data_list[21]  # 平手/半球 降
            # 有些比赛没有赔率数据，显示为'--'
            if Concede.find('--') > -1:
                continue
            if Concede.find(' ') > -1:
                Concede = Concede[:Concede.index(' ')]
            Concede = concede_dict[Concede]
            # logger.info(Concede)

            InitialConcede = odds_data_list[25]  # 平手
            InitialConcede = concede_dict[InitialConcede]
            # logger.info(InitialConcede)

            GuestAsianOdds = odds_data_list[22]
            # logger.info(GuestAsianOdds)
            InitialGuestAsianOdds = odds_data_list[26]
            # logger.info(InitialGuestAsianOdds)
            BigOdds = odds_data_list[29]
            # logger.info(BigOdds)
            InitialBigOdds = odds_data_list[33]
            # logger.info(InitialBigOdds)

            BigSmall = odds_data_list[30]  # 1.5/2 升
            if BigSmall.find(' ') > -1:
                BigSmall = BigSmall[:BigSmall.index(' ')]
            bigsmall_dict = {'1': 1, '1/1.5': 1.25, '1.5': 1.5, '1.5/2': 1.75,
                             '2': 2, '2/2.5': 2.25, '2.5': 2.5, '2.5/3': 2.75,
                             '3': 3, '3/3.5': 3.25, '3.5': 3.5, '3.5/4': 3.75,
                             '4': 4, '4/4.5': 4.25, '4.5': 4.5, '4.5/5': 4.75,
                             '5': 5, '5/5.5': 5.25, '5.5': 5.5, '5.5/6': 5.75,
                             '6': 6, '6/6.5': 6.25, '6.5': 6.5, '6.5/7': 6.75,
                             '7': 7, '7/7.5': 7.25, '7.5': 7.5, '7.5/8': 7.75,
                             '8': 8, '8/8.5': 8.25, '8.5': 8.5, '8.5/9': 8.75,
                             '9': 9, '9/9.5': 9.25, '9.5': 9.5, '9.5/10': 9.75,
                             '10': 10, '10/10.5': 10.25, '10.5': 10.5, '10.5/11': 10.75}
            BigSmall = bigsmall_dict[BigSmall]
            # logger.info(BigSmall)

            InitialBigSmall = odds_data_list[34]
            InitialBigSmall = bigsmall_dict[InitialBigSmall]
            # logger.info(InitialBigSmall)
            SmallOdds = odds_data_list[31]
            # logger.info(SmallOdds)
            InitialSmallOdds = odds_data_list[35]
            # logger.info(InitialSmallOdds)

            # 亚盘欧赔数据不全的，SB很多比赛没有初盘欧赔
            HostEuropeOdds, DeuceEuropeOdds, GuestEuropeOdds = 0, 0, 0
            if len(odds_data_list) > 38:
                HostEuropeOdds = odds_data_list[38]
                # logger.info(HostEuropeOdds)
                DeuceEuropeOdds = odds_data_list[39]
                # logger.info(DeuceEuropeOdds)
                GuestEuropeOdds = odds_data_list[40]
                # logger.info(GuestEuropeOdds)

            InitialHostEuropeOdds, InitialDeuceEuropeOdds, InitialGuestEuropeOdds = 0, 0, 0
            if len(odds_data_list) > 42:
                InitialHostEuropeOdds = odds_data_list[42]
                # logger.info(InitialHostEuropeOdds)
                InitialDeuceEuropeOdds = odds_data_list[43]
                # logger.info(InitialDeuceEuropeOdds)
                InitialGuestEuropeOdds = odds_data_list[44]
                # logger.info(InitialGuestEuropeOdds)

            HostGameTrend = aomen_data_list[6]  # 近況走勢 - WLLWWW
            trend = re.findall(r'[A-Z]', HostGameTrend)
            HostGameTrend = ''.join(trend).replace('W', '3').replace('D', '1').replace('L', '0')
            # logger.info(HostGameTrend)
            GuestGameTrend = aomen_data_list[9]
            trend = re.findall(r'[A-Z]', GuestGameTrend)
            GuestGameTrend = ''.join(trend).replace('W', '3').replace('D', '1').replace('L', '0')
            # logger.info(GuestGameTrend)
            HostBetTrend = aomen_data_list[7]
            trend = re.findall(r'[A-Z]', HostBetTrend)
            HostBetTrend = ''.join(trend).replace('W', '3').replace('D', '1').replace('L', '0')
            # logger.info(HostBetTrend)
            GuestBetTrend = aomen_data_list[10]
            trend = re.findall(r'[A-Z]', GuestBetTrend)
            GuestBetTrend = ''.join(trend).replace('W', '3').replace('D', '1').replace('L', '0')
            # logger.info(GuestBetTrend)

            CounterResult = aomen_data_list[11]  # 信心指數 - 烏法 ★★★★★          對賽成績 - 烏法 1勝 1和 0負
            splitted = re.search(r".*(\d+)勝 (\d+)和 (\d+)負", CounterResult)
            CounterResult = splitted.group(1) + splitted.group(2) + splitted.group(3)
            # logger.info(CounterResult)

            MacaoRecommend = aomen_data_list[11]
            splitted = re.findall(r"- (\w+)\s", MacaoRecommend)
            if splitted[0] == splitted[1]:
                MacaoRecommend = 3
                # logger.info(3)
            elif splitted[0] == '和局':
                MacaoRecommend = 1
                # logger.info(1)
            else:
                MacaoRecommend = 0
                # logger.info(0)

            RecommendReason = aomen_data_list[12]
            # logger.info(RecommendReason)

            insertOne(MatchId, MatchType, MatchDate, Host, Guest, HostRank, GuestRank, HostAsianOdds,
                      InitialHostAsianOdds, Concede, InitialConcede, GuestAsianOdds, InitialGuestAsianOdds,
                      BigOdds, InitialBigOdds, BigSmall, InitialBigSmall, SmallOdds,
                      InitialSmallOdds, HostEuropeOdds, InitialHostEuropeOdds, DeuceEuropeOdds,
                      InitialDeuceEuropeOdds, GuestEuropeOdds, InitialGuestEuropeOdds, HostGameTrend,
                      GuestGameTrend, HostBetTrend, GuestBetTrend, CounterResult, MacaoRecommend, RecommendReason)
        except BaseException as e:
            logger.info(e)
            continue

if __name__ == '__main__':
    parse_html_into_db()