#! python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, BigInteger, DATETIME, VARCHAR, SmallInteger, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
import contextlib

# 创建对象的基类:
Base = declarative_base()

# 定义StaticInfo对象:
class StaticInfo(Base):
    # 今天的比赛:
    __tablename__ = '310v_static_info_today'

    # 表的结构:
    MatchId = Column(BigInteger, primary_key=True)
    MatchType = Column(VARCHAR)
    MatchDate = Column(DATETIME)
    Host = Column(VARCHAR)
    Guest = Column(VARCHAR)
    HostRank = Column(SmallInteger)
    GuestRank = Column(SmallInteger)
    HostAsianOdds = Column(Float)
    InitialHostAsianOdds = Column(Float)
    Concede = Column(Float)
    InitialConcede = Column(Float)
    GuestAsianOdds = Column(Float)
    InitialGuestAsianOdds = Column(Float)
    BigOdds = Column(Float)
    InitialBigOdds = Column(Float)
    BigSmall = Column(Float)
    InitialBigSmall = Column(Float)
    SmallOdds = Column(Float)
    InitialSmallOdds = Column(Float)
    HostEuropeOdds = Column(Float)
    InitialHostEuropeOdds = Column(Float)
    DeuceEuropeOdds = Column(Float)
    InitialDeuceEuropeOdds = Column(Float)
    GuestEuropeOdds = Column(Float)
    InitialGuestEuropeOdds = Column(Float)
    HostGameTrend = Column(VARCHAR)
    GuestGameTrend = Column(VARCHAR)
    HostBetTrend = Column(VARCHAR)
    GuestBetTrend = Column(VARCHAR)
    CounterResult = Column(VARCHAR)
    MacaoRecommend = Column(SmallInteger)
    RecommendReason = Column(String)


def insertOne(list, engine, logger):
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新match对象:
    matchStr =  'MatchId='+ str(list[0]) + ',MatchType='+ str(list[1]) + ',MatchDate=' + str(list[2]) \
    + ',Host=' + str(list[3]) \
    + ',Guest=' + str(list[4]) + ',HostRank=' + str(list[5]) \
    + ',GuestRank=' + str(list[6]) + ',HostAsianOdds=' + str(list[7]) + 'InitialHostAsianOdds=' + str(list[8]) \
    + ',Concede=' + str(list[9]) + ',InitialConcede=' + str(list[10]) + ',GuestAsianOdds=' + str(list[11]) \
    + ',InitialGuestAsianOdds=' + str(list[12]) + ',BigOdds=' + str(list[13]) + ',InitialBigOdds=' + str(list[14])\
    + ',BigSmall=' + str(list[15]) + ',InitialBigSmall=' + str(list[16]) + ',SmallOdds=' + str(list[17])\
    + ',InitialSmallOdds=' + str(list[18]) + ',HostEuropeOdds=' + str(list[19]) + ',InitialHostEuropeOdds=' + str(list[20]) \
    + ',DeuceEuropeOdds=' + str(list[21]) + ',InitialDeuceEuropeOdds=' + str(list[22]) + ',GuestEuropeOdds=' + str(list[23]) \
    + ',InitialGuestEuropeOdds=' + str(list[24]) + ',HostGameTrend=' + str(list[25]) + ',GuestGameTrend=' + str(list[26]) \
    + ',HostBetTrend=' + str(list[27]) + ',GuestBetTrend=' + str(list[28]) \
    + ',CounterResult=' + str(list[29]) + ',MacaoRecommend=' + str(list[30]) \
    + ',RecommendReason=' + str(list[31])

    logger.info(matchStr)

    new_match = StaticInfo(MatchId=str(list[0]), MatchType=str(list[1]), MatchDate=str(list[2])
        ,Host=str(list[3])
        ,Guest=str(list[4]), HostRank=str(list[5])
        ,GuestRank=str(list[6]) ,HostAsianOdds=str(list[7]) ,InitialHostAsianOdds=str(list[8])
        ,Concede=str(list[9]), InitialConcede=str(list[10]) ,GuestAsianOdds=str(list[11])
        ,InitialGuestAsianOdds=str(list[12]), BigOdds=str(list[13]), InitialBigOdds=str(list[14])
        ,BigSmall=str(list[15]), InitialBigSmall=str(list[16]),SmallOdds=str(list[17])
        ,InitialSmallOdds=str(list[18]),HostEuropeOdds=str(list[19]),InitialHostEuropeOdds=str(list[20])
        ,DeuceEuropeOdds=str(list[21]),InitialDeuceEuropeOdds=str(list[22]),GuestEuropeOdds=str(list[23])
        , InitialGuestEuropeOdds=str(list[24]),HostGameTrend=str(list[25]),GuestGameTrend=str(list[26])
        ,HostBetTrend=str(list[27]),GuestBetTrend=str(list[28])
        ,CounterResult=str(list[29]),MacaoRecommend=str(list[30]),RecommendReason=str(list[31]))
    # 添加到session:
    session.add(new_match)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

def truncate_today_data(engine):
    with contextlib.closing(engine.connect()) as con:
        trans = con.begin()
        con.execute('truncate table 310v_static_info_today')
        trans.commit()

def query_filtered(logger):
    # 初始化数据库连接:
    conn = mysql.connector.connect(user='root', password='password', database='soccer', use_unicode=True)
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM (( SELECT MatchId AS id, MatchDate AS d FROM 310v_static_info_today WHERE CounterResult > 500 AND Concede =- 0.5 ) UNION ( SELECT MatchId AS id, MatchDate AS d FROM 310v_static_info_today WHERE RIGHT (CounterResult, 1) > 4 AND Concede < 0.75 AND Concede > 0 AND Concede = InitialConcede )) AS T ORDER BY d ASC')
    values = cursor.fetchall()
    matches = []
    for value in values:
        matches.append(value[0])
    logger.info('符合规则的比赛:' + str(matches))

    cursor.close()
    conn.close()
    return matches

if __name__ == '__main__':
    # insertOne('11486748','意甲','2017-12-10 19:30:00','切沃','罗马',12,4,0.9,0.9,1.00,1.00,0.98,0.98,1.01,1.01,2.75,2.75,0.85,0.85,5.4,5.4,4.3,4.3,1.58,1.58,
    #           '011310','330133','033300','330030','226','3','切禾近6輪聯賽僅獲1勝，反觀羅馬目前連續7輪聯賽保持不敗之餘贏足6場，雙方近況高下立判，實力高出一檔的羅馬此行大勝可期。')
    query_filtered()
    # truncate_today_data()

