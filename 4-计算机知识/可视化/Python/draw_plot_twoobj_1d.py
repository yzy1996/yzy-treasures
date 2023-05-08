import pickle

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

import matplotlib as mpl


mpl.style.use('default')

mu = 0
variance = 2
sigma = math.sqrt(variance)
x = np.linspace(-4, 4, 1000)

f1 =  stats.norm.pdf(x, -1, sigma)
f2 =  stats.norm.pdf(x, 1, sigma)
f3 = (f1 + f2) / 2


fig = plt.figure(figsize=(6,6))

plt.plot(x, f1,label='Objective f1')
plt.plot(x, f2,label='Objective f2',c = 'g')

plt.plot([-1,1],[0.,0], c = 'tomato', lw = 3, label = 'Pareto Set', zorder = 6)
plt.scatter([-1,1],[0,0], s = 80, c = 'tomato', label = 'Separate Solutions for f1 or f2', zorder = 6)
plt.scatter(0,0, s = 80, c = 'tomato', marker ='^', label = 'Trade-Off Solution for (f1+f2)/2', zorder = 6)

plt.ylim(-0.02, 0.4)
plt.xlabel('x', size = 16)
plt.ylabel('f(x)', size = 16)

plt.legend(loc = 1, scatterpoints=1,markerscale = 1)
plt.grid()
plt.show()


#fig.savefig('gaussian_twoobj_1D.pdf', format='pdf', dpi=1200,bbox_inches='tight')