import pygal

from die import Die

#kość D6
die = Die() 

#Wykonanie rzutów i umieszczenie na liście
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
print(results)

#analiza wyników
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print("\t")
print(frequencies)

#Wizualizacja danych
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik tysiąckrotnego rzutu kością D6"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Wynik wyrzucony"
hist.y_title = "Częstotliwość wystepowania wartości"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
