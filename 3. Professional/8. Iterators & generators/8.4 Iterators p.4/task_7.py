# CardDeck
# Итератор класса CardDeck должен генерировать последовательность из 
# 52 игральных карт, а после возбуждать исключение StopIteration. Каждая карта должна представлять собой строку в следующем формате:

class CardDeck:
    def __init__(self):
        self.cards = iter([('2', 'пик'), ('3', 'пик'), ('4', 'пик'), ('5', 'пик'), ('6', 'пик'), ('7', 'пик'), ('8', 'пик'), ('9', 'пик'), ('10', 'пик'), ('валет', 'пик'), ('дама', 'пик'), ('король', 'пик'), ('туз', 'пик'), ('2', 'треф'), ('3', 'треф'), ('4', 'треф'), ('5', 'треф'), ('6', 'треф'), ('7', 'треф'), ('8', 'треф'), ('9', 'треф'), ('10', 'треф'), ('валет', 'треф'), ('дама', 'треф'), ('король', 'треф'), ('туз', 'треф'), ('2', 'бубен'), ('3', 'бубен'), ('4', 'бубен'), ('5', 'бубен'), ('6', 'бубен'), ('7', 'бубен'), ('8', 'бубен'), ('9', 'бубен'), ('10', 'бубен'), ('валет', 'бубен'), ('дама', 'бубен'), ('король', 'бубен'), ('туз', 'бубен'), ('2', 'червей'), ('3', 'червей'), ('4', 'червей'), ('5', 'червей'), ('6', 'червей'), ('7', 'червей'), ('8', 'червей'), ('9', 'червей'), ('10', 'червей'), ('валет', 'червей'), ('дама', 'червей'), ('король', 'червей'), ('туз', 'червей')])
        self.index = 0
        self.value = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1

        if self.index > 52:
            raise StopIteration
        else:
            self.value = next(self.cards)
            return " ".join(self.value)
