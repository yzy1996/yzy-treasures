import pickle

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

import matplotlib as mpl


mpl.style.use('default')

mu = 0
variance = 16
sigma = math.sqrt(variance)
x = np.linspace(-20, 30, 1000)

f1 = stats.norm.pdf(x, 0, sigma)
f2 = stats.norm.pdf(x, -6, 0.5 * sigma)
f3 = stats.norm.pdf(x, 6, 2 * sigma)

f4 = (f1 + f2 + f3)  / 3


fig = plt.figure()

plt.plot(x, f1,label='Objective f1')
plt.plot(x, f2,label='Objective f2')
plt.plot(x, f3,label='Objective f3')

#plt.plot(x, f4, ls = '--',label='(f1 + f2 + f3) / 3')
#plt.scatter(-6,0, s = 60, c = 'r', label = 'Single Solution', zorder = 6)

plt.scatter([-6,0,6],[0,0,0], s = 60, c = 'r', label = 'Multiple Solutions', zorder = 6)


plt.ylim(-0.01, 0.2)

plt.xlabel('x', size = 16)
plt.ylabel('f(x)', size = 16)

plt.legend(scatterpoints=1,markerscale = 0.5)
plt.grid()
plt.show()


#fig.savefig('gaussian_problem_multiple_point.pdf', format='pdf', dpi=1200,bbox_inches='tight')



