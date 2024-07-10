# cubes_of_odds()

def cubes_of_odds(iterable):
    return (num**3 for num in iterable if num % 2 != 0)