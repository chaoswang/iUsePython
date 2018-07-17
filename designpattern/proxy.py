#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

class SalesMan:
    def work(self):
        print("SalesMan working...")

    def talk(self):
        print("SalesMan ready to talk...")

class Proxy:
    def __init__(self):
        self.busy = "No"
        self.sales = None

    def work(self):
        print("Proxy checking for SalesMan availability...")
        if self.busy == "No":
            self.sales = SalesMan()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("SalesMan is busy")

if __name__ == '__main__':
    p = Proxy()
    p.work()
    p.busy = "Yes"
    p.work()