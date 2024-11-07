from objects.entities.enemies.blue_slime import Blue_Slime
from objects.entities.enemies.green_slime import Green_Slime
from objects.entities.enemies.black_slime import Black_Slime
from objects.entities.enemies.pink_slime import Pink_Slime
import random

class Controller():

    def __init__(self, spawn_function, get_enemy_count_function, enemy_types : list, boss_types = []):
        self.wave = 0
        self.enemies = 0
        self.enemy_types = enemy_types
        self.boss_types = boss_types
        self.spawn_boss = False
        self.spawn_wave = True
        self.spawn_function = spawn_function
        self.get_enemy_count_function = get_enemy_count_function
        self.update_wave = None

    def spawn(self): # The function that runs each frame to check if it should spawn and if how many.
        if self.get_enemy_count_function() <= 0:
            self.wave += 1
            self.spawn_wave = True
            self.update_wave(self.wave)

        if self.spawn_wave:
            self.spawn_wave = False
            count = self.get_enemy_count()
            print(count)
            for enemy in self.enemy_types:
                print(enemy)
                for i in range(count[self.enemy_types.index(enemy)]):
                    spawned_enemy = None
                    if enemy.get_tags().count("blue_slime") > 0:
                        spawned_enemy = Blue_Slime(3, (random.randint(0,500), random.randint(0,500)))
                    elif enemy.get_tags().count("green_slime") > 0:
                        spawned_enemy = Green_Slime(3, (random.randint(0,500), random.randint(0,500)))
                    elif enemy.get_tags().count("black_slime") > 0:
                        spawned_enemy = Black_Slime(3, (random.randint(0,500), random.randint(0,500)))
                    elif enemy.get_tags().count("pink_slime") > 0:
                        spawned_enemy = Pink_Slime(3, (random.randint(0,500), random.randint(0,500)))
                    self.spawn_function(spawned_enemy)


    def get_enemy_count(self): # This function return a list that looks like the self.enemy_types list but instead of an object it is the amount of that object that should be spawned each wave. It calculates this using some algoritm
        # Sort enemies by their damage in ascending order
        sorted_by_damage = sorted(self.enemy_types, key=lambda obj: (obj.get_damage() + (obj.get_health() % 8)))
        count = self.enemy_types.copy()

        # Calculate spawn amount for each enemy type, prioritizing low-damage enemies
        for obj in sorted_by_damage:
            index = self.enemy_types.index(obj)
            
            # Spawn more enemies for low-damage types and increase with wave number
            base_amount = (sorted_by_damage.index(obj) + 1)
            wave_multiplier = (self.wave + 1)
            
            # Calculate the final amount with a limit based on wave
            amount = min(base_amount * wave_multiplier, max(8, wave_multiplier)) // 3  # Set a max per wave
            
            count[index] = amount

        return count

    def set_update_wave(self,function):
        self.update_wave = function