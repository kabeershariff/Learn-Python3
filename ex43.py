from sys import exit
from random import randint
from textwrap import dedent


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #printing the last scene 
        current_scene.enter()

class Scene(object):

    def enter(self):
        print("Subclass and implement enter()")
        exit(1)

class Death(Scene):

    def enter(self):
        print("GAME OVER! YOU DIDN'T MAKE IT!!")
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Aliens have invaded your ship. You are the last surviving member.
            Your Last mission is to retrieve the bomb from the weapon armoury and
            plant it on the bridge. Blow the ship after getting into an escape pod.

            You are in the central corridor now. A grim alien is blocking your path now.
        """))

        action = input("> ")

        if action == "shoot":
            print("You shoot him with your gun. Its not effective")
            return 'death'

        elif action == "dodge":
            print("You hit your head!")
            return 'death'

        elif action == "joke":
            print("Your joke kills!")
            return 'laser_weapon_armory'

        else: 
            print("Doesn't compute")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

   def enter(self):
        print("You are in the armoury. You need to enter a 3 digit code to unlock the weapon!!")
        code = f'123'
        guess = input('keypad> ')
        guesses = 0

        while guess != code and guesses < 2:
            print("NZZZZZ")
            guesses += 1
            guess = input('keypad> ')

        if guess == code:
            print("Yess! Its Open")
            return 'the_bridge'

        else:
            print("You have failed to open the mechanism !! YOU CANNOT DO ANYTHING NOW!!")
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print("You have reached the bridge! There are 5 aliens here and they are staring at you now !")
        action = input("> ")
        if action == "throw":
            print("As soon as you throw the bomb! The alien shoots you!!")
            return 'death'

        elif action == "plant":
            print("You slowly plant the bomb and point your gun towards it and slowly backoff")
            return 'escape_pod'

        else:
            print("Doesnt compute")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print("You have reached the escape pods, but there are 3 pods out of which 2 are faulty!!")
        good_pod = 2
        guess = input("Which one will you take ?")

        if int(guess) == good_pod:
            print("This pod seems to work fine!")
            return 'finished'

        else:
            print("BOOM!!")
            return 'death'

class Finished(Scene):

    def enter(self):
        print("YOU HAVE MADE IT ALIVE !! HURRAY ")
        return 'finished'
        
class Map(object):

    scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished()
            }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

