#! python3
# -*- coding: utf-8 -*-
from soccer.bigwinner.logger.LoggingConfig import LoggingConfig
from sqlalchemy import Column, BigInteger, VARCHAR, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()

# 定义StaticInfo对象:
class StaticInfo(Base):
    # 表的名字:
    __tablename__ = '310v_dynamic_info'

    # 表的结构:
    MatchId = Column(BigInteger, primary_key=True)
    Score = Column(VARCHAR)

def insertOne(*list):
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/soccer')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新match对象:
    matchStr =  'MatchId='+ str(list[0]) + ',Score='+ str(list[1])
    log = LoggingConfig()
    logger = log.logger
    logger.info(matchStr)

    new_match = StaticInfo(MatchId=str(list[0]), Score=str(list[1]))
    # 添加到session:
    session.add(new_match)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

if __name__ == '__main__':
    insertOne('11486748','2 - 2')



