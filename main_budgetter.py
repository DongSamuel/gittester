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
    
    def getFood(self):
        return self.costs['food']
    
    def getSum(self):
        return 

#hi whats up with you
if __name__ == "__main__":
    mycosts1: Costs = {'food' : 200, 'rent': 300, 'sharesies': 100, 'clothes': 50}
    myBudget = Budgetter(20, mycosts1)
    food_price = myBudget.getFood()
    print(food_price)

        