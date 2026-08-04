from time import sleep
from random import randint

class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon    
    
    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon)

    def strike(self, enemy):
        min_damage = int(self.power * 0.5)
        max_damage = self.power + 10
        random_power = randint(min_damage, max_damage)
        
        if random_power >= max_damage - 2:
            print('!!! КРИТИЧЕСКИЙ УРОН !!!')
            
        print(
            '-> УДАР! ' + self.name + ' атакует ' + enemy.name +
            ' с силой ' + str(random_power) + ', используя ' + self.weapon + '\n'
        )
        
        enemy.armor -= random_power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
            
        print(
            enemy.name + ' покачнулся.\nКласс его брони упал до '
            + str(enemy.armor) + ', а уровень здоровья до '
            + str(enemy.health) + '\n'
        )
        print('----------------------------------------')

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'Пал в этом нелёгком бою\n')
                break
            sleep(3)
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в этом нелёгком бою\n')
                break
            sleep(3)
