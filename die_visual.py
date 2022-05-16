from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# create a D6 + D10
#die = Die()
die_1 = Die(6)
die_2 = Die(10)

# make rolls + store results in a list
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualise the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 and one D10 50 000 times', xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6_d10.html')
