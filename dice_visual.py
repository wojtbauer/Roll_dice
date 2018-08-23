import pygal

from die import Die

# kość D6 x2
die_1 = Die()
die_2 = Die()

# Wykonanie rzutów i umieszczenie na liście
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# analiza wyników
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print("\t")
print(frequencies)

# Wizualizacja danych
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik tysiąckrotnego rzutu dwoma kościami D6"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Wynik wyrzucony"
hist.y_title = "Częstotliwość wystepowania wartości"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
