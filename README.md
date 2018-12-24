# Pet-Game
**Use The Class Build Pet Development Game**

In this project, will write a Python program to **implement a virtual pet**. You can decide the species, name, and gender of your pet. You can also interact with your pet by feeding your pet, playing with your pet, bathing your pet, etc. Will design a user-defined Class called ‘Pet’ to achieve that.

I think a lot of people have played this kind of game like cultivation. It may be a web version, a game console or even a mobile version. So this is my goal, just the initial implementation, without too much optimization and modification.

### Graphical and desktop (Mac Windows Android)
Refer to the Tk part of the python basic manual to program and desktop the program, but for personal reasons will temporarily learn the C++ language. If you are willing to participate or just have this idea and energy, please contact me. I am very happy to work with you.

If you want to develop Android programs you can use Qpython, which is a new supplement package for python.

Perhaps there are still undiscovered problems and errors in the program. If you are lucky enough to be discovered by you, please give me feedback and correct the error. I am very happy to accept.

A pet has the following basic attributes:
- Species (we assume two species: dog and cat)
- Name
- Gender (we assume two genders: male and female)
- Fur color

As well as some other attributes that are related to physical or mental health status:
- Energy
- Hunger
- Thirst
- Loneliness
- Smell

-------------------

These attributes are measured in the range from 0 to 10. For the ‘energy’ attribute, the ideal value is 10. For the other attributes (‘hunger’, ‘thirst’, ‘loneliness’, and ‘smell’), the ideal value is 0. When a pet object is created, his or her initial status is randomized within an acceptable range. For example, a newly created pet may have a hunger/thirst/loneliness/smell level in the range of (0, 5), and have an energy level in the range of (5, 10).

**Therefore, in your pet class, you will have attributes related to each feature that we mentioned. Make them as private attributes (i.e., the attribute name should start with a single underscore)**

**Learning Objectives**
- Class

-------------------

The goal of this game is to take care of your pet by keeping your pet in a good status (i.e., lower hunger/thirst/loneliness/smell level, and higher energy level). You can take care of your pet by taking each of the following actions:
- Let your pet get some sleep
- Feed your pet some food
- Feed your pet some water
- Play with your pet
- Bathe your pet

The health status of your pet will be updated each time you take a certain action:
- After you feed your pet food, his/her hunger level will be decreased.
- After you feed your pet water, his/her thirst level will be decreased.
- After you play with your pet, the loneliness level will be decreased, but the hunger level, thirst level, and smell level will be increased.
- After you bathe your pet, the smell level will be decreased.
- After your pet gets some sleep, the energy level will be increased.

After you take an action, your pet will give you feedback about the specific action you took. Next, your pet will report his/her status if some attributes are too low or too high. For example, after you play with your pet, your pet will first say ‘Thanks for your company’. Next, if the hunger level of your pet is lower than a threshold (say 5), your pet will say ‘I am hungry’. Please note that multiple attributes may need to be reported after an action. If your pet is both hungry and thirsty after playing with you, he/she will say two sentences: ‘I am hungry,’ and then ‘I am thirsty’.

The game begins by prompting you to entering the species, name, gender, and fur color of your pet, each feature separated by a space. Once those inputs are validated, a pet object will be created. Then the program will prompt you to enter a command. Your command will either lead to an action taken or lead to a table that shows you the health status of your pet. The program will repeatedly prompt you to input a command, until you enter ‘q’ and then you will quit this game.

