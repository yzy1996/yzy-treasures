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
x = np.linspace(-1, 1, 1000)

f1 = 1 * stats.norm.pdf(x, -1, sigma)
f2 = 1 * stats.norm.pdf(x, 1, sigma)
f3 = (f1 + f2) / 2


fig = plt.figure(figsize=(6,6))



plt.plot(f1,f2, c = 'tomato', lw = 3, label = 'Pareto Front', zorder = 3)
plt.scatter([f1[0],f2[0]],[f1[-1],f2[-1]], s = 80, c = 'tomato', label = 'Separate Solutions for f1 or f2', zorder = 6)
plt.scatter([f1[500]],[f2[500]], s = 80, c = 'tomato', marker ='^', label = 'Trade-Off Solution for (f1+f2)/2', zorder = 6)

#plt.ylim(-0.02, 1)
plt.xlabel('f1(x)', size = 16)
plt.ylabel('f2(x)', size = 16)

plt.legend(loc = 1, scatterpoints=1,markerscale = 1)
plt.grid()
plt.show()


#fig.savefig('gaussian_twoobj_pf.pdf', format='pdf', dpi=1200,bbox_inches='tight')