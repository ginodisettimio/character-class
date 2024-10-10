import random


class Character:
    # Al menos 1 Atributo de clase
    characters_dict = {
        'name': 'Luke Skywalker',
        'armor_class': 45,
        'strength': 55,
        'hp': 250
    }

    # Al menos 3 atributos de objeto
    def __init__(self, name, strength, armor_class, hp):
        self.name = name
        self.strength = strength
        self.armor_class = armor_class
        self.hp = hp

    # Al menos 1 método estático
    @staticmethod
    def roll_d20():
        throw = random.randint(1, 20)
        print(f'Ha salido {throw}')
        return throw

    # Al menos 1 método de clase
    @classmethod
    def from_dict(cls, character_dict):
        return cls(
            name=character_dict['name'],
            strength=character_dict['strength'],
            armor_class=character_dict['armor_class'],
            hp=character_dict['hp']
        )

    # 1 campo calculado (@property)
    @property
    def alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    # Al menos 1 método de objeto
    def attack(self, enemy):
        print(f'{self.name} ha atacado a {enemy.name}')
        if enemy.armor_class < (self.strength + Character.roll_d20()):
            enemy.take_damage(self.strength)  # Actualiza la vida del enemigo
            if enemy.alive:
                print(f'La vida de {enemy.name} ahora es {enemy.hp}')
            else:
                print(f'{enemy.name} ha muerto')
        else:
            print('El ataque falló')


# Creación de personajes
Protagonist = Character('Obi-wan', 100, 12, 100)
Antagonist = Character('Darth Vader', 10, 15, 200)


# Ejemplo de ataque
print(f'{Protagonist.name} vs {Antagonist.name}')
Protagonist.attack(Antagonist)
print()

# Aplicacion de metodo estatico
Character.roll_d20()
print()

# Aplicación de metodo de clase
Luke = Character.from_dict(Character.characters_dict)
print(f'Nombre: {Luke.name}, Fuerza: {Luke.strength}, Clase de armadura: {
      Luke.armor_class}, Puntos de vida: {Luke.hp}')
Luke.attack(Antagonist)
