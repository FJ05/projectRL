from pygame.examples.cursors import image

from objects.entities.enemies.blue_slime import Blue_Slime
from objects.entities.enemies.green_slime import Green_Slime
from objects.entities.enemies.black_slime import Black_Slime
from objects.entities.enemies.pink_slime import Pink_Slime
from objects.entities.enemies.boss.boss_slime import Boss_Slime
from objects.entities.enemies.boss.final_boss_slime import Final_Boss_Slime
import random
import pygame
class Controller():

    def __init__(self, spawn_function, get_enemy_count_function, enemy_types : list, boss_types = []):
        self.wave = 0
        self.enemies = 0
        self.enemy_types = enemy_types
        self.boss_types = boss_types
        self.spawn_final_boss = False
        self.spawn_mini_boss = False
        self.spawn_wave = True
        self.spawn_function = spawn_function
        self.get_enemy_count_function = get_enemy_count_function
        self.update_wave = None
        self.screen_size = pygame.display.get_window_size() # Get screen size



    def spawn(self):
        # Check if a new wave or boss spawn is needed
        if self.get_enemy_count_function() <= 0:
            if self.wave == 0:
                self.spawn_final_boss = True
            # Boss spawns on every 5th wave, except wave 0
            elif self.wave % 5 == 0 and not self.spawn_mini_boss and self.wave != 0:
                self.spawn_mini_boss = True
            else:
                self.spawn_wave = True
            
            # Increment wave and update wave tracker
            self.wave += 1
            self.update_wave(self.wave)

        if self.spawn_final_boss:
            self.spawn_final_boss = False
            boss = Final_Boss_Slime(3, (100, self.screen_size[1] / 2))
            boss.set_spawn_function(self.spawn_function)
            self.spawn_function(boss)

        # Spawn mini boss
        if self.spawn_mini_boss:
            self.spawn_mini_boss = False
            boss = Boss_Slime(3, (100, self.screen_size[1] / 2), 10 + 1.5 * self.wave, 300 + 2 * self.wave, 10 + 0.2 * self.wave, self.wave)
            boss.set_spawn_function(self.spawn_function)

            self.spawn_function(boss)

        # Spawn wave of enemies if needed
        elif self.spawn_wave:
            self.spawn_wave = False
            count = self.get_enemy_count()
            
            # Define corners for spawning enemies outside the screen
            corners = [
                (-50, -50),  # Top-left corner
                (self.screen_size[0] + 50, -50),  # Top-right corner
                (-50, self.screen_size[1] + 50),  # Bottom-left corner
                (self.screen_size[0] + 50, self.screen_size[1] + 50)  # Bottom-right corner
            ]

            for enemy in self.enemy_types:
                spawn_count = count[self.enemy_types.index(enemy)]
                
                for i in range(spawn_count):
                    corner = random.choice(corners)  # Randomly choose a corner to spawn

                    # Spawn based on enemy type tags
                    if "blue_slime" in enemy.get_tags():
                        spawned_enemy = Blue_Slime(3, corner)
                    elif "green_slime" in enemy.get_tags():
                        spawned_enemy = Green_Slime(3, corner)
                    elif "black_slime" in enemy.get_tags():
                        spawned_enemy = Black_Slime(3, corner)
                    elif "pink_slime" in enemy.get_tags():
                        spawned_enemy = Pink_Slime(3, corner)
                    else:
                        continue  # Skip if the enemy type tag is unrecognized
                    
                    # Use spawn function to place the enemy in the game
                    self.spawn_function(spawned_enemy)




    def get_enemy_count(self): # This function return a list that looks like the self.enemy_types list but instead of an object it is the amount of that object that should be spawned each wave. It calculates this using some algoritm
        # Sort enemies by their damage in ascending order
        sorted_by_damage = sorted(self.enemy_types, key=lambda obj: (obj.get_damage() + obj.get_health() + obj.get_reach() + obj.get_speed()*3)//4)
        sorted_by_damage.reverse()
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
