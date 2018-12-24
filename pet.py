# Make all import
from random import randint
from edible import DogFood
from edible import CatFood
from edible import Water

###########################################################
#
# Computer Project Pet-Game
#
# Define all the functions of Pet class
#   def __init__():
#       The basic function initializes all variables.
#       No return
#   def _time_pass_by(self, t = 1):
#       Used to calculate time
#       No return
#   def get_hunger_level(self):
#       just return the self._hunger
#   def get_thirst_level(self):
#       just return the self._thirst
#   def get_energy_level(self):
#       just return the self._energy
#   def drink(self, liquid):
#       Calculate thirst level and judge whether thirsty or not.
#       No return just print
#   def feed(self, food):
#       Calculate hunger levels and determine if they are hungry.
#       No return just print
#   def shower(self):
#       Calculate the pet's physical condition after bathing.
#       No return
#   def sleep(self):
#       Calculate the pet's physical condition after sleep.
#       No return
#   def play_with(self):
#       Calculate the pet's physical condition after playing.
#       No return
#   def _reply_to_master(self, event='newborn'):
#       Outputs all pet states and expressions.
#       No return just print
#   def show_status(self):
#       partially formatted string for your guidance
#       No return just print
#   def _update_status(self):
#       Outputs all pet states and expressions.
#       No return just print
#
# class Cat(Pet):
#   inheritance the Pet class and use local class
# class Dog(Pet):
#   inheritance the Pet class and use local class
#
# Define the main function
#   Call all functions and classes.
#   use two while loop to have enough information
#   and some if and elif and else
#   No return
#      
###########################################################

# Make all The global variable
MIN, MAX = 0, 10
dog_edible_items = [DogFood]
cat_edible_items = [CatFood]
dog_drinkable_items = [Water]
cat_drinkable_items = [Water]

# Make the Pet() class
class Pet(object):
    
    def __init__(self, name = 'fluffy', species = 'dog', \
                 gender = 'male', color = 'white'):
        """
The basic function initializes all variables.
    must have self
No return
        """
        self._name = name.capitalize()
        self._species = species.capitalize()
        self._gender = gender.capitalize()
        self._color = color.capitalize()
        self._edible_items = []
        self._drinkable_items = []
        
        self._hunger = randint(0, 5)
        self._thirst = randint(0, 5)
        self._smell = randint(0, 5)
        self._loneliness = randint(0, 5)
        self._energy = randint(5, 10)
        
        self._reply_to_master('newborn')
        
    def _time_pass_by(self, t = 1):
        """
Used to calculate time
No return
        """
        self._hunger = min(MAX, self._hunger + (0.2 * t))
        self._thirst = min(MAX, self._thirst + (0.2 * t))
        self._smell = min(MAX, self._smell + (0.1 * t))
        self._loneliness = min(MAX, self._loneliness + (0.1 * t))
        self._energy = max(MIN, self._energy - (0.2 * t))
        
    def get_hunger_level(self):
        """
just return the self._hunger
        """
        return self._hunger
    
    def get_thirst_level(self):
        """
just return the self._thirst
        """
        return self._thirst
    
    def get_energy_level(self):
        """
just return the self._energy
        """
        return self._energy
    
    def drink(self, liquid):
        """
Calculate thirst level and judge whether thirsty or not.
    use two if and isinstance
No return just print
        """
        
        if isinstance(liquid, tuple(self._drinkable_items)):
            
            self._time_pass_by()
            
            if self._thirst >= liquid.get_quantity():
                self._thirst = self._thirst - liquid.get_quantity()
                
            elif self._thirst <= 0:
                print("Too much drink to finish. I will leave some for you.")
                
            else:
                self._thirst = 0
        else:
            print("Not drinkable")
        
        self._reply_to_master(event = 'drink')
        self._update_status()

    def feed(self, food):
        """
Calculate hunger levels and determine if they are hungry.
    use two if and isinstance
No return just print
        """
        
        if isinstance(food, tuple(self._edible_items)):
            
            self._time_pass_by()
            
            if self.get_hunger_level() >= 2:
                
                if self._hunger >= food.get_quantity():
                    self._hunger = self._hunger - food.get_quantity()
                
                elif self._hunger <= 0:
                    print("Too much feed to finish. I will leave some for you.")
                
                else:
                    self._hunger = 0
                    
                self._reply_to_master(event = 'feed')
            
            else:
                print("Your pet is satisfied, " + \
                      "no desire for sustenance now.")
            
        else:
            print("Not edible")
        
        self._update_status()

    def shower(self):
        """
Calculate the pet's physical condition after bathing.
    use _time_pass_by, max(), _update_status and _reply_to_master
No return
        """
        
        time = 4
        self._time_pass_by(time)

        self._smell = 0
        self._loneliness = max(MIN, self._loneliness - time)

        self._reply_to_master('shower')
        self._update_status()

    def sleep(self):
        """
Calculate the pet's physical condition after sleep.
    use _time_pass_by, min(), _update_status and _reply_to_master
No return
        """
        
        time = 7
        self._time_pass_by(time)
        
        self._energy = min(MAX, self._energy + time)
        
        self._reply_to_master('sleep')
        self._update_status()

    def play_with(self):
        """
Calculate the pet's physical condition after playing.
    use _time_pass_by, min(), max(), _update_status and _reply_to_master
No return
        """
        
        time = 4
        self._time_pass_by(time)
        
        self._energy = max(MIN, self._energy - time)
        self._loneliness = max(MIN, self._loneliness - time)
        self._smell = min(MAX, self._smell + time)
        
        self._reply_to_master('play')
        self._update_status()

    def _reply_to_master(self, event='newborn'):
        """
Outputs all pet states and expressions.
No return just print
        """
        faces = {}
        talks = {}
        
        faces['newborn'] = "(๑>◡<๑)"
        faces['feed'] = "(๑´ڡ`๑)"
        faces['drink'] = "(๑´ڡ`๑)"
        faces['play'] = "(ฅ^ω^ฅ)"
        faces['sleep'] = "୧(๑•̀⌄•́๑)૭✧"
        faces['shower'] = "( •̀ .̫ •́ )✧"

        talks['newborn'] = "Hi master, my name is {}.".format(self._name)
        talks['feed'] = "Yummy!"
        talks['drink'] = "Tasty drink ~"
        talks['play'] = "Happy to have your company ~"
        talks['sleep'] = "What a beautiful day!"
        talks['shower'] = "Thanks ~"

        s = "{} ".format(faces[event])  + ": " + talks[event]
        print(s)

    def show_status(self):
        """
partially formatted string for your guidance
    use the for loop and sort()
No return just print
        """
        list_show = [['Energy', self._energy],['Hunger', self._hunger],\
                  ['Loneliness', self._loneliness],['Smell', self._smell],\
                  ['Thirst', self._thirst]]
        list_show.sort()
        
        for show in list_show:
            print("{:<12s}: [{:<20s}]".format(show[0], 2 * round(show[1]) * \
                  '#') + "{:5.2f}/{:2d}".format(show[1], 10))
        
    def _update_status(self):
        """
Outputs all pet states and expressions.
No return just print
        """
        faces = {}
        talks = {}
        
        faces['default'] = "(๑>◡<๑)"
        faces['hunger'] = "(｡>﹏<｡)"
        faces['thirst'] = "(｡>﹏<｡)"
        faces['energy'] = "(～﹃～)~zZ"
        faces['loneliness'] = "(〃∀〃)"
        faces['smell'] = "(⁰▿⁰)"

        talks['default'] = 'I feel good.'
        talks['hunger'] = 'I am so hungry ~'
        talks['thirst'] = 'Could you give me some drinks? Alcohol-free please ~'
        talks['energy'] = 'I really need to get some sleep.'
        talks['loneliness'] = 'Could you stay with me for a little while ?'
        talks['smell'] = 'I am sweaty'

class Cat(Pet):
    """
inheritance the Pet class and use local class
    """
    def __init__(self, name = 'fluffy', gender = 'male', \
                 color = 'white', species = 'cat'):
        Pet.__init__(self, name, species, gender, color)
        self._edible_items = cat_edible_items
        self._drinkable_items = cat_drinkable_items  
        
class Dog(Pet):
    """
inheritance the Pet class and use local class
    """
    def __init__(self, name = 'fluffy', gender = 'male', \
                 color = 'white', species = 'dog'):
        Pet.__init__(self, name, species, gender, color)
        self._edible_items = dog_edible_items
        self._drinkable_items = dog_drinkable_items  

def main():
    """
Call all functions and classes.
    use two while loop to have enough information
    and some if and elif and else
No return
    """
    print("Welcome to this virtual pet game!")
    
    # error checking for user input
    while True:
        prompt = input("Please input the species (dog or cat), name, " + \
                       "gender (male / female), fur color of your pet, " + \
                       "seperated by space \n ---Example input:  [dog] " + \
                       "[fluffy] [male] [white] \n (Hit Enter " + \
                       "to use default settings): ")
        if prompt == '':
            pet = Dog()
            break
        
        if prompt != '':
            prompt_list = prompt.split()
            if prompt_list[2] == 'male' or prompt_list[2] == 'female':
                if prompt_list[0] == 'cat':
                    pet = Cat(prompt_list[1], prompt_list[2], \
                              prompt_list[3], prompt_list[0])
                    break
                
                elif prompt_list[0] == 'dog':
                    pet = Dog(prompt_list[1], prompt_list[2], \
                              prompt_list[3], prompt_list[0])
                    break
                else:
                    continue
            else:
                continue

    intro = "\nYou can let your pet eat, drink, get a shower, " + \
    "get some sleep, or play with him or her by entering each of " + \
    "the following commands:\n --- [feed] [drink] [shower] [sleep]" + \
    " [play]\n You can also check the health status of your pet by " + \
    "entering:\n --- [status]."
    print(intro)

    prompt = input("\n[feed] or [drink] or [shower] or [sleep] " + \
    "or [play] or [status] ? (q to quit): ")
    
    # use the list to make sure
    true_list = ['1','2','3','4','5','6','7','8','9','10']
    
    # use the while loop to exit
    while prompt.lower() != 'q':
        
        if prompt == 'feed':
            
            while True:
                
                quantity = input("How much food ? 1 - 10 scale: ")
                if quantity in true_list:
                    quantity = int(quantity)
                    break
                else:
                    print('Invalid input.')
                    
            if type(pet) == Cat:
                pet.feed(CatFood(quantity))
            if type(pet) == Dog:
                pet.feed(DogFood(quantity))
        
        elif prompt == 'drink':
            
            while True:
                
                quantity = input("How much drink ? 1 - 10 scale: ")
                if quantity in true_list:
                    quantity = int(quantity)
                    break
                else:
                    print('Invalid input.')
                    
            pet.drink(Water(quantity))
        
        elif prompt == 'shower':
            pet.shower()
            
        elif prompt == 'sleep':
            pet.sleep()
            
        elif prompt == 'play':
            pet.play_with()
            
        elif prompt == 'status':
            pet.show_status()
            
        elif pet.get_energy_level() >= 10:
            print("Your pet is too energetic to fall sleep.")
            
        else:
            print("Invalid command.")
            
        prompt = input("\n[feed] or [drink] or [shower] or [sleep] " + \
                       "or [play] or [status] ? (q to quit): ")

    print("Bye ~")

# just the main
if __name__ == "__main__":
    main()
