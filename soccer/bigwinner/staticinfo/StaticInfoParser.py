#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from com.github.chaoswang.soccer.bigwinner.logger.LoggingConfig import LoggingConfig
from com.github.chaoswang.soccer.bigwinner.staticinfo.StaticInfo import insertOne, query_filtered, truncate_today_data
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import threading
from sqlalchemy import create_engine

class StaticInfoParser:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')  # 无头参数
        options.add_argument('--disable-gpu')  
        # self.__driver = webdriver.Chrome(chrome_options=options)
        self.__driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=options)
        self.__driver.get('http://bf2.310v.com:3389/index.html')
        # self.__driver.get('http://ny.310v.com:3389/dt/over.html?md=2018-05-04')
        self.__driver.implicitly_wait(20)
        time.sleep(2)

    @property
    def web_driver(self):
        return self.__driver

    # 获取今日比赛数据
    @property
    def match_id(self):
        page_source = self.__driver.page_source
        matches = []
        try:
            soup = BeautifulSoup(page_source, "html.parser")
            trs = soup.findAll("tr", {"id": re.compile("d[0-9]+")})
            for tr in trs:
                # if tr.find("span", {"class": "hot"}):
                matches.append(tr.get("id"))
        except AttributeError as e:
            print(e)
            return None
        print(matches)
        return matches

def parse_html_into_db(driver, matches, engine, logger):
    for index in range(len(matches)):
        try:
            # 历史比赛数据
            # analysis_url = 'http://ny.310v.com:3389/match_fx/fenxi_html.html?mid='+ matches[index]
            # 今日比赛数据
            analysis_url = "http://ny.310v.com:3389/match_fx/fenxi_html.html?mid=" + matches[index][1:]
            logger.info(analysis_url)
            driver.get(analysis_url)
            driver.implicitly_wait(5)

            html = driver.page_source
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
            # MatchId = matches[index]
            # 今日比赛数据
            MatchId = matches[index][1:]
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

            list = [MatchId, MatchType, MatchDate, Host, Guest, HostRank, GuestRank, HostAsianOdds,
                      InitialHostAsianOdds, Concede, InitialConcede, GuestAsianOdds, InitialGuestAsianOdds,
                      BigOdds, InitialBigOdds, BigSmall, InitialBigSmall, SmallOdds,
                      InitialSmallOdds, HostEuropeOdds, InitialHostEuropeOdds, DeuceEuropeOdds,
                      InitialDeuceEuropeOdds, GuestEuropeOdds, InitialGuestEuropeOdds, HostGameTrend,
                      GuestGameTrend, HostBetTrend, GuestBetTrend, CounterResult, MacaoRecommend, RecommendReason]
            insertOne(list, engine, logger)
        except BaseException as e:
            logger.exception(e)
            continue

def query_filtered_match(driver, logger):
    matches = query_filtered(logger)
    if len(matches) < 1:
        return None

    output_html = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\r\n"
    for index in range(len(matches)):
        fenxi_url = "http://ny.310v.com:3389/match_fx/fenxi_html.html?mid=" + str(matches[index])
        logger.info(fenxi_url)
        driver.get(fenxi_url)
        driver.implicitly_wait(5)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        odds = str(soup.find("table", {"id": "id_tb_dw"}))
        aomen = str(soup.find("table", {"id": "bbdg_7"}))
        output_html += odds + "\r\n" + aomen
    return output_html

def send_mail(html_to_send, logger):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "263050006@qq.com"  # 用户名
    mail_pass = "ryrzjgjtphqvcaaj"  #  口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

    sender = '263050006@qq.com'
    receivers = '263050006@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(html_to_send, 'html', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] = Header(receivers, 'utf-8')
    message['Subject'] = Header('今日热点', 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        logger.info("邮件发送成功")
        smtpObj.quit()
    except smtplib.SMTPException as e:
        logger.info("无法发送邮件", e)


def main_timer():
    parser = StaticInfoParser()
    logger = LoggingConfig().logger
    logger.info('启动定时器')
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/soccer')
    try:
        truncate_today_data(engine)
        parse_html_into_db(parser.web_driver, parser.match_id, engine, logger)
        output_html = query_filtered_match(parser.web_driver, logger)
        if output_html:
            send_mail(output_html, logger)
    except BaseException as e:
        logger.warn('主方法定时器异常', e)

    global timer  # 定义变量
    timer = threading.Timer(60 * 60, main_timer)  # 60分钟调用一次函数
    # 定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
    timer.start()  # 启用定时器

if __name__ == '__main__':
    main_timer()