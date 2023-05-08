import matplotlib.pyplot as plt
import numpy as np

# rectangular box plot
data1 = [0.0011, 0.0012, 0.0013]
data2 = [0.0013, 0.002, 0.0015]
data3 = [0.0022, 0.0023, 0.0021]
data4 = [0.0025, 0.003, 0.0031]


all_data = [data1, data2, data3, data4]
labels = ['re-30%', 're-50%', 're-70%', 're-100%']

bplot1 = plt.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels,
                     showfliers=False)  # will be used to label x-ticks

locs, labels=plt.xticks()

# plt.plot(x,y)
plt.plot(locs, np.mean(all_data, axis=1), 'o--', color='grey', alpha=0.3)
#第3步：显示图形
plt.grid(axis='x', color='0.95')
plt.show()