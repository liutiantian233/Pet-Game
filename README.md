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

These attributes are measured in the range from 0 to 10. For the ‘energy’ attribute, the ideal value is 10. For the other attributes (‘hunger’, ‘thirst’, ‘loneliness’, and ‘smell’), the ideal value is 0. When a pet object is created, his or her initial status is randomized within an acceptable range. For example, a newly created pet may have a hunger/thirst/loneliness/smell level in the range of (0, 5), and have an energy level in the range of (5, 10).

Therefore, in your pet class, you will have attributes related to each feature that we mentioned. Make them as private attributes (i.e., the attribute name should start with a single underscore, like self._name)
