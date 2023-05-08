import pickle

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from scipy.stats import multivariate_normal

from matplotlib.patches import Circle, Wedge, Polygon

import matplotlib as mpl


mpl.style.use('default')


mu1 = np.array([-1,0])
mu2 = np.array([1,0])
mu3 = np.array([0,np.sqrt(3)])

variance = 2 * np.eye(2)


x = np.linspace(-2,2,500)
y = np.linspace(-1.5,2.5,500)
X,Y = np.meshgrid(x,y)

pos = np.array([X.flatten(),Y.flatten()]).T



rv1 = multivariate_normal(mu1, variance)
rv2 = multivariate_normal(mu2, variance)
rv3 = multivariate_normal(mu3, variance)


fig = plt.figure(figsize=(6,6))
#ax0 = fig.add_subplot(111)
# ax0.contourf(X, Y, rv1.pdf(pos).reshape(500,500),alpha = 1,cmap = 'Wistia_r')
# ax0.contourf(X, Y, rv2.pdf(pos).reshape(500,500),alpha = 0.5,cmap = 'Wistia_r')

c1 = plt.contour(X, Y, rv1.pdf(pos).reshape(500,500),cmap = 'Blues',alpha = 0.5)
c2 = plt.contour(X, Y, rv2.pdf(pos).reshape(500,500),cmap = 'Greens',alpha = 0.5)
c3 = plt.contour(X, Y, rv3.pdf(pos).reshape(500,500),cmap = 'Purples',alpha = 0.5)
#c4 = ax0.contour(X, Y, rv1.pdf(pos).reshape(500,500) + rv2.pdf(pos).reshape(500,500) + rv3.pdf(pos).reshape(500,500),cmap = 'Oranges')
c1.collections[6].set_label('Objective f1')
c2.collections[6].set_label('Objective f2')
c3.collections[6].set_label('Objective f3')


plt.plot([-1,1,0,-1],[0,0,np.sqrt(3),0], c = 'tomato', lw = 3, label = 'Pareto SubSet', zorder = 6)
plt.plot([0,0],[0,np.sqrt(3)], c = 'purple', lw = 3, label = 'Pareto SubSet', zorder = 3)
t1 = plt.Polygon(np.array([[-1,1,0],[0,0,np.sqrt(3)]]).T, color='orange', alpha = 0.3, label = 'Pareto Set')
plt.gca().add_patch(t1)
plt.scatter([-1,1,0],[0,0,np.sqrt(3)], s = 100, c = 'tomato', label = 'Separate Solutions for f1 or f2 of f3', zorder = 6)
plt.scatter([0],[np.sqrt(3)/3], s = 100, c = 'purple', marker ='^', label = 'Trade-Off Solution for (f1+f2+f3)/3', zorder = 6)


plt.xlabel('x1', size = 16)
plt.ylabel('x2', size = 16)

handles, labels = plt.gca().get_legend_handles_labels()
order = [3,4,5, 2,0,1,6,7]

plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order],bbox_to_anchor = (1, 1.015))
plt.grid()
plt.show()

#fig.savefig('gaussian_3obj_2D.pdf', format='pdf', dpi=1200,bbox_inches='tight')
