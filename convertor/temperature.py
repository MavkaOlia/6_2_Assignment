def cel_to_fahr(cels):
    fahrenheit = (cels * 1.8) + 32
    return fahrenheit


def fahr_to_cel(fahr):
    celsius = (fahr - 32) / 1.8
    return celsius

print(cel_to_fahr(7))
print(fahr_to_cel(70))
