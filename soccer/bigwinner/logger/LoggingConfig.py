#! python3
# encoding=utf-8
# @Time    : 2018/4/29 11:50
# @Author  : chaoswang
# @File    : LoggingConfig.py

import logging.config
import yaml


class LoggingConfig:
    def __init__(self):
        with open('/home/soccer/pyLearning/prj_soccer/com/github/chaoswang/soccer/bigwinner/logger/logging.yml', 'r') as f_conf:
            dict_conf = yaml.load(f_conf)
        logging.config.dictConfig(dict_conf)

    @property
    def logger(self):
        return logging.getLogger('Soccer168')


if __name__ == '__main__':
    log = LoggingConfig()
    logger = log.logger
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
