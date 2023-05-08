import pickle

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from scipy.stats import multivariate_normal

import matplotlib as mpl


mpl.style.use('default')


mu1 = np.array([-1,0])
mu2 = np.array([1,0])

variance = 2 * np.eye(2)


x = np.linspace(-4,4,500)
y = np.linspace(-4,4,500)
X,Y = np.meshgrid(x,y)

pos = np.array([X.flatten(),Y.flatten()]).T



rv1 = multivariate_normal(mu1, variance)
rv2 = multivariate_normal(mu2, variance)


fig = plt.figure(figsize=(6,6))
ax0 = fig.add_subplot(111)
# ax0.contourf(X, Y, rv1.pdf(pos).reshape(500,500),alpha = 1,cmap = 'Wistia_r')
# ax0.contourf(X, Y, rv2.pdf(pos).reshape(500,500),alpha = 0.5,cmap = 'Wistia_r')

c1 = ax0.contour(X, Y, rv1.pdf(pos).reshape(500,500),cmap = 'Blues')
c2 = ax0.contour(X, Y, rv2.pdf(pos).reshape(500,500),cmap = 'Greens')
c1.collections[6].set_label('Objective f1')
c2.collections[6].set_label('Objective f2')


ax0.plot([-1,1],[0,0], c = 'tomato', lw = 3, label = 'Pareto Set', zorder = 6)
ax0.scatter([-1,1],[0,0], s = 100, c = 'tomato', label = 'Separate Solutions for f1 or f2', zorder = 6)
ax0.scatter([0],[0], s = 100, c = 'tomato', marker ='^', label = 'Trade-Off Solution for (f1+f2)/2', zorder = 6)


ax0.set_xlabel('x1', size = 16)
ax0.set_ylabel('x2', size = 16)

handles, labels = plt.gca().get_legend_handles_labels()
order = [1,2,0,3,4]

plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order])
plt.grid()
plt.show()

#fig.savefig('gaussian_twoobj_2D.pdf', format='pdf', dpi=1200,bbox_inches='tight')

