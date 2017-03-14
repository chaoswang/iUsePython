#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class PetShop:
    def __init__(self, animal_factory=None):
        '''pet_factory is abstract factory'''
        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""
        pet = self.pet_factory.get_pet()
        food = self.pet_factory.get_food()
        print("This is a lovely", str(pet))
        print("It says", pet.speak())
        print("It eats", food)

class Dog:
    def speak(self):
        return "wo wo"

    def __str__(self):
        return "Dog"

class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog food"

class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat food"

def get_factory():
    return random.choice([DogFactory, CatFactory])()

if __name__ == "__main__":
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("="*20)