from db_config import read_data
from misc import cursor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def parse_data(dataset):
    if dataset:
        parsed_data = list()
        headers = ['year', 'population_amount', 'suicide_amount']
        for _ in dataset:
            parsed_data.append({x: y for x, y in zip(headers, _)})
        return True, parsed_data
    else:
        return False, "GBuilder: no input data"


def get_timeline():
    timeline = list()
    for _ in data:
        timeline.append(_['year'])
    return timeline


def get_suicide_amount():
    tmp_data = list()
    for _ in data:
        tmp_data.append(float(_['suicide_amount']))
    return tmp_data


def get_population_amount():
    tmp_data = list()
    for _ in data:
        tmp_data.append(float(_['population_amount']))
    return tmp_data


def two_scales(ax1i, time_data, data1, data2, c1, c2):
    ax2 = ax1.twinx()
    ax1i.plot(time_data, data1, color=c1)
    ax1i.set_xlabel('time (year)')
    ax1i.set_ylabel('Population')
    ax2.plot(time_data, data2, color=c2)
    ax2.set_ylabel('% suicide')
    return ax1, ax2


state, data = parse_data(read_data(cursor, "world"))

time = get_timeline()
p = get_population_amount()
s1 = np.asarray(get_suicide_amount(), dtype=np.float32)
tmp_s2 = list()
for i, _ in enumerate(s1):
    tmp_s2.append(float(_) * 100 / float(p[i]))
s2 = np.asarray(tmp_s2, dtype=np.float32)

fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(111)

ax1, ax1a = two_scales(ax1, time, s1, s2, 'r', 'b')


def color_y_axis(ax, color):
    for t in ax.get_yticklabels():
        t.set_color(color)


color_y_axis(ax1, 'gold')
color_y_axis(ax1a, 'limegreen')

plt.xlim([1990, 2017])
ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))

plt.show()
