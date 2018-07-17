#!/usr/bin/env python3
# coding:utf-8
'''
为一组调用提供一致的接口,为一个复杂子系统提供一个简单接口
'''
import time

SLEEP = 0.5

# Complex Parts
class TC1:
    def run(self):
        print("###### In Test 1 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")

class TC2:
    def run(self):
        print("###### In Test 2 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")

class TC3:
    def run(self):
        print("###### In Test 3 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")

# Facade
class TestRunner:
    def __init__(self):
        self.tests = [TC1(), TC2(), TC3()]

    def runAll(self):
        for i in self.tests:
            i.run()

if __name__ == '__main__':
    testRunner = TestRunner()
    testRunner.runAll()