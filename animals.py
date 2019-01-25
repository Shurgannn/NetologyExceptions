class Animals:
    satiety = 0  # сытость
    max_satiety = 100

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight  # kg

    def feed(self, satiety):  # кормление
        if self.satiety + satiety > self.max_satiety:
            self.satiety = self.max_satiety
            print('Наелся')
        else:
            self.satiety += satiety

    def __lt__(self, other):
        return self.weight < other.weight


class Goose(Animals):
    voice = 'га-га-га'
    max_satiety = 50
    state = 'Яйца не собраны'

    def collect_eggs(self):
        self.state = 'Яйца собраны'
        print('Яйца собраны')

Goose1 = Goose('Серый', 2)
print(Goose1.name, ':', '"', Goose.voice, '"')
print('Сытость 1 гуся:', Goose1.satiety)
Goose1.feed(10)
print('Сытость 1 гуся:', Goose1.satiety)
Goose1.feed(100)
print('Сытость 1 гуся:', Goose1.satiety)
Goose1.collect_eggs()
Goose2 = Goose('Белый', 3)
print(Goose2.name, ':', '"', Goose.voice, '"')
print(Goose2.satiety)
Goose2.feed(60)
print('Сытость 2 гуся:', Goose2.satiety)
Goose1.collect_eggs()
Goose2.collect_eggs()

class Cow(Animals):
    voice = 'му-му'
    state1 = 'молоко не подоено'

    def milk(self):
        self.state1 = 'молоко подоено'
        print('молоко подоено')

Cow1 = Cow('Манька', 100)
print('\n',Cow1.name, ':', '"', Cow.voice, '"')
print('Сытость коровы:', Cow1.satiety)
Cow1.feed(110)
print('Сытость коровы:', Cow1.satiety)
Cow1.milk()

class Sheep(Animals):
    voice = 'бе-бе'
    state2 = 'овца не стрижена'

    def shear(self):
        self.state2 = 'овца стрижена'
        print('овца стрижена')

Sheep1 = Sheep('Барашек', 10)
print('\n',Sheep1.name, ':', '"', Sheep.voice, '"')
print('Сытость овцы 1:', Sheep1.satiety)
Sheep1.feed(110)
print('Сытость овцы 1:', Sheep1.satiety)
Sheep1.shear()
Sheep2 = Sheep('Кудрявый', 20)
print(Sheep2.name, ':', '"', Sheep.voice, '"')
print('Сытость овцы 2:', Sheep2.satiety)
Sheep2.feed(110)
print('Сытость овцы 2:', Sheep2.satiety)
Sheep2.shear()

class Chiken(Goose):
    voice = 'ку-ка-реку'

Chiken1 = Chiken('Ко-Ко', 1.5)
print('\n',Chiken1.name, ':', '"', Chiken.voice, '"')
print('Сытость курицы 1:', Chiken.satiety)
Chiken1.feed(110)
print('Сытость курицы 1:', Chiken1.satiety)
Chiken1.collect_eggs()
Chiken2 = Chiken('Кукареку', 1)
print(Chiken2.name, ':', '"', Chiken.voice, '"')
print('Сытость курицы 2:', Chiken2.satiety)
Chiken2.feed(110)
print('Сытость курицы 2:', Chiken2.satiety)
Chiken2.collect_eggs()

class Goat(Cow):
    voice = 'ме-ме'

Goat1 = Goat('Рога', 5)
print('\n',Goat1.name, ':', '"', Goat.voice, '"')
print('Сытость козы 1:', Goat1.satiety)
Goat1.feed(110)
print('Сытость козы 1:', Goat1.satiety)
Goat1.milk()
Goat2 = Goat('Копыта', 6)
print(Goat2.name, ':', '"', Goat.voice, '"')
print('Сытость козы 1:', Goat2.satiety)
Goat2.feed(110)
print('Сытость козы 1:', Goat2.satiety)
Goat2.milk()

class Duck(Goose):
    voice = 'кря-кря'

Duck1 = Duck('Кряква', 4)
print('\n',Duck1.name, ':', '"', Duck1.voice, '"')
print('Сытость утки:', Duck1.satiety)
Duck1.feed(110)
print('Сытость утки:', Duck1.satiety)
Duck1.collect_eggs()

print('Общий вес всех животных:', sum([Goose1.weight, Goose2.weight, Cow1.weight, Sheep1.weight, Sheep2.weight, Chiken1.weight, Chiken2.weight, Goat1.weight, Goat2.weight, Duck1.weight]), 'кг')

max_weight = Goose1.weight
max_weight_name = Goose1.name
if max_weight > Goose2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Goose2.weight
    max_weight_name = Goose2.name
if max_weight > Cow1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Cow1.weight
    max_weight_name = Cow1.name
if max_weight > Sheep1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Sheep1.weight
    max_weight_name = Sheep1.name
if max_weight > Sheep2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Sheep2.weight
    max_weight_name = Sheep2.name
if max_weight > Chiken1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Chiken1.weight
    max_weight_name = Chiken1.name
if max_weight > Chiken2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Chiken2.weight
    max_weight_name = Chiken2.name
if max_weight > Goat1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Goat1.weight
    max_weight_name = Goat1.name
if max_weight > Goat2.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Goat2.weight
    max_weight_name = Goat2.name
if max_weight > Duck1.weight:
    max_weight = max_weight
    max_weight_name = max_weight_name
else:
    max_weight = Duck1.weight
    max_weight_name = Duck1.name
print('Имя самого тяжелого животного:', max_weight_name)

# print(goose1.__dict__)
# print(goose2.__dict__)
# print(goose.__dict__)
