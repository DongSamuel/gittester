# import packages
import pandas as pd
import pyodbc
from typing import TypedDict
import json

class Costs(TypedDict):
    food: int
    rent: int
    sharesies: int
    clothes: int

#this is so crazy bro
class Budgetter():
    def __init__(self, total_cash, costs: Costs):
        self.total_cash = total_cash
        self.costs = costs
    
    def getCategories(self):
        return [x for x in self.costs.keys()]
    
    def getSum(self):
        return [self.costs[x] for x in self.costs.keys()]
    
    def getFood(self):
        foodstuff =  self.costs['food']
        print(foodstuff)
        return foodstuff
    

#hi whats up with you
if __name__ == "__main__":
    mycosts1: Costs = {'food' : 200, 'rent': 300, 'sharesies': 100, 'clothes': 50}
    myBudget = Budgetter(20, mycosts1)
    food_price = myBudget.getFood()
    cats = myBudget.getSum()
    print(cats)

        