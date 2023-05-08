import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()


def plot_quadratic(x_offset=0, y_offset=0, scale=1):

    x = np.linspace(-5, 5, 100)
    y = scale * (x - x_offset) ** 2 + y_offset
    plt.plot(x, y)

plot_quadratic()

plt.show()


# # draw solution line
# u = np.linspace(-5, 5, 1000)
# x = u
# y = [0] * len(u)
# ax.plot(x, y, zs=0, zdir='z', label=r'Solution Curve in plane ($x_1$, $x_2$)')


# def draw_plot2(center_x, center_y, z_offset, radius, scale, color, alpha=1):
#     u = np.linspace(0, 2 * np.pi, 100)
#     v = np.linspace(0, np.pi, 100)
#     x = np.outer(np.cos(u), np.sin(v))
#     y = np.outer(np.sin(u), np.sin(v))
#     z = scale * x ** 2 + scale * y ** 2 + z_offset
#     ax.plot_surface(x + center_x, y + center_y, z,
#                     color=color, rstride=1, alpha=alpha)

#     # shared solution
#     ax.scatter(center_x, 0, 0, color="red", label='Feasible Optimal Solution')

#     ax.plot([center_x, center_x], [center_y, center_y],
#             [z_offset, 0], 'g--', lw=1)

#     # draw solutions
#     ax.scatter(center_x, center_y, 0, s=10,
#                color="black", label='Optimal Solution')

#     # draw arrow，第二组坐标是一个差值
#     # ax.quiver(center_x, center_y, 0, 0, -center_y, 0, arrow_length_ratio=0.08, color='b', linestyle='--')
#     ax.plot([center_x, center_x], [center_y, 0], 'b--', lw=1)


# def draw_plot1(center_x, center_y, z_offset, radius, scale, color, alpha):
#     x = np.linspace(center_x - radius, center_x + radius, 100)
#     y = np.linspace(center_y - radius, center_y + radius, 100)
#     x, y = np.meshgrid(x, y)
#     z = scale * (x - center_x)**2 + scale * (y - center_y)**2 + z_offset
#     ax.plot_surface(x, y, z, color=color, rstride=1, alpha=alpha)


# # parameter = [center_x, center_y, z_offset, radius, scale, color, alpha]
# draw_plot2(-4, -1, 0.1, 1, 0.7, 'tomato', 0.1)
# draw_plot2(-3, 3, 0.2, 1, 0.5, 'blue', 0.1)
# draw_plot2(2, -1, 0, 1, 1, 'lime', 0.1)
# draw_plot2(4, 1, 0.3, 1, 0.3, 'cyan', 0.1)

# # 合并图例
# handles, labels = ax.get_legend_handles_labels()
# ax.legend([handles[0], tuple(handles[1:6:2]),
#           tuple(handles[2:7:2])], labels[0:3])

# ax.text(-4, -1, 0.9, r'$f_1$')
# ax.text(-3, 3, 0.8, r'$f_2$')
# ax.text(2, -1, 1.1, r'$f_3$')
# ax.text(4, 1, 0.7, r'$f_4$')

# ax.text(-4, 0.1, 0, r'$x^1$')
# ax.text(-3.2, 0.1, 0, r'$x^2$')
# ax.text(2, 0.1, 0, r'$x^3$')
# ax.text(4.2, 0.1, 0, r'$x^4$')

# # 设置坐标轴
# ax.set_xlim(-5, 5)
# ax.set_ylim(-5, 5)
# ax.set_zlim(0, 1)
# ax.set_zticks([])
# ax.set_xlabel(r'$x_1$', fontsize=14)
# ax.set_ylabel(r'$x_2$ (shared)', fontsize=14)
# ax.set_zlabel(r'$f$', fontsize=14)
# ax.grid(False)
plt.show()

# ax.figure.savefig('WP2.pdf', format='pdf', dpi=1200, bbox_inches='tight')
