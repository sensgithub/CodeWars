# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
def litres(time):
    time=int(time)
    litres=0
    for x in range(time):
        litres=litres+0.5
    return int(litres)