a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
def Sorensen_Dice(a, b):
    _a = set(a)
    _b = set(b)
    return (2 * len(_a.intersection(_b))) / (len(_a) + len(_b))
Sorensen_Dice(a, b)