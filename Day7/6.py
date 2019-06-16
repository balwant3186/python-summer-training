def kelvinToFahrenheit(Temperature):
    assert(Temperature >= 0), 'Colder than absolute zero!.'
    res = ((Temperature - 273) * 1.8) + 32
    return res

try:
    print(kelvinToFahrenheit(273))
    print(kelvinToFahrenheit(505.78))
    print(kelvinToFahrenheit(-5))

except AssertionError as ob:
    print(ob)

print('Thank You')
