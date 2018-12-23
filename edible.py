class Food(object):
    
    def __init__(self, quantity):
        self.__quantity__ = quantity
        
    def get_quantity(self):
        return self.__quantity__

class DogFood(Food):
    
    def __init__(self, quantity=1):
        Food.__init__(self, quantity)

class CatFood(Food):
    
    def __init__(self, quantity=1):
        Food.__init__(self, quantity)

class Chocolate(Food):
    
    def __init__(self, quantity=1):
        Food.__init__(self, quantity)

class Drinkable(object):
    
    def __init__(self, quantity):
        self.__quantity__ = quantity
        
    def get_quantity(self):
        return self.__quantity__

class Water(Drinkable):
    
    def __init__(self, quantity=1):
        Drinkable.__init__(self, quantity)

class Milk(Drinkable):
    
    def __init__(self, quantity=1):
        Drinkable.__init__(self, quantity)