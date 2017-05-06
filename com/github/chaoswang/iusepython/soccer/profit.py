#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ProfitCalculator:
    def calculate(self, cost, matchCount, odds, winningPercentage):
        #matchCount场比赛能赢几场
        winCount = matchCount * winningPercentage
        loseCount = matchCount - winCount
        totalCost = cost * matchCount
        profit = winCount * odds * cost
        print("投入：" + str(totalCost))
        print("当胜率为：" + str(winningPercentage))
        print(str(matchCount) + "场比赛")
        print("收益为：" + str(profit))
        print("收益率为：" + str(profit/totalCost))


def main():
    calculator = ProfitCalculator()
    calculator.calculate(2, 10, 3, 0.4)

if __name__ == '__main__':
    main()