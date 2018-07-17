#!/usr/bin/env python3
# coding:utf-8

# 项目经理
class Director:
    def __init__(self):
        self.builder = None


    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building

# 抽象的建造者
class Builder:
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

# 建筑物
class Building:
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: %s | Size: %s' % (self.floor, self.size)

# 具体的建造者，房屋建造者
class HouseBuilder(Builder):
    def build_floor(self):
        self.building.floor = "One"

    def build_size(self):
        self.building.size = "Big"

# 公寓建造者
class FlatBuilder(Builder):
    def build_floor(self):
        self.building.floor = "More than one"

    def build_size(self):
        self.building.size = "Small"

if __name__ == '__main__':
    director = Director()
    director.builder = HouseBuilder()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = FlatBuilder()
    director.construct_building()
    building = director.get_building()
    print(building)



