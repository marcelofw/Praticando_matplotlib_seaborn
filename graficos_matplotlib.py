import matplotlib as mpl

print(mpl.__version__)

import matplotlib.pyplot as plt

# plt.plot([1, 3, 5], [2, 4, 7])
# plt.show()

# x = [2, 3, 5]
# y = [3, 5, 7]
# plt.plot(x, y)
# plt.xlabel("Variável 1")
# plt.ylabel("Variável 2")
# plt.title("Teste plot")
# plt.show()

# x2 = [1, 2, 3]
# y2 = [11, 12, 15]
# plt.plot(x2, y2, label = "Gráfico com Matplotlib")
# plt.legend()
# plt.show()

# x1 = [2, 4, 6, 8, 10]
# y1 = [6, 7, 8, 2, 4]

# plt.bar(x1, y1, label = "Barras", color = "green")
# plt.legend()
# plt.show()

# x2 = [1, 3, 5, 7, 9]
# y2 = [7, 8, 2, 4, 2]

# plt.bar(x1, y1, label = "Listas1", color = "blue")
# plt.bar(x2, y2, label = "Listas2", color = "red")
# plt.legend()
# plt.show()

# idades = [22, 65, 45, 55, 21, 22, 34, 42, 41, 4, 99, 101, 120, 122, 130, 111, 115, 80, 75, 54, 44, 64, 13, 18, 48]
# ids = [x for x in range(len(idades))]
# plt.bar(ids, idades)
# plt.show()
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
# plt.hist(idades, bins, histtype = "bar", rwidth = 0.8)
# plt.show()
# plt.hist(idades, bins, histtype = "stepfilled", rwidth = 0.8)
# plt.show()

# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [5, 2, 4, 5, 6, 8, 4, 8]

# plt.scatter(x, y, label = "Pontos", color = "black", marker = "o")
# plt.legend()
# plt.show()

# dias = [1, 2, 3, 4, 5]
# dormir = [7, 8, 6, 77, 7]
# comer = [2, 3, 4, 5, 3]
# trabalhar = [7, 8, 7, 2, 2]
# passear = [8, 5, 7, 8, 13]

# plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m', 'c', 'r', 'k', 'b'])
# plt.show()

# fatias = [7, 2, 2, 13]
# atividades = ["dormir", "comer", "passear", "trabalhar"]
# cores = ["olive", "lime", "violet", "royalblue"]
# plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode = (0, 0.2, 0, 0))
# plt.show()

from pylab import *
# x = linspace(0, 5, 10)
# y = x ** 2
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y, "r")
# axes.set_xlabel("x")
# axes.set_ylabel("y")
# axes.set_title("Gráfico de Linha")
# plt.show()

# x = linspace(0, 5, 10)
# y = x ** 2
# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# axes1.plot(x, y, "r")
# axes1.set_xlabel("x")
# axes1.set_ylabel("y")
# axes1.set_title("Figura Principal")
# axes2.plot(y, x, "g")
# axes2.set_xlabel("x")
# axes2.set_ylabel("y")
# axes2.set_title("Figura Secundária")
# plt.show()

# x = linspace(0, 5, 10)
# y = x ** 2
# fig, axes = plt.subplots(nrows = 1, ncols = 3)
# for ax in axes:
#     ax.plot(x, y, "r")
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     ax.set_title("Título")
# fig.tight_layout()
# plt.show()

# x = linspace(0, 5, 10)
# y = x ** 2
# fig, axes = plt.subplots(1, 2, figsize = (10,4))
# axes[0].plot(x, x**2, x, exp(x))
# axes[0].set_title("Escala Padrão")
# axes[1].plot(x, x**2, x, exp(x))
# axes[1].set_yscale("log")
# axes[1].set_title("Escala Logaritmica (y)")
# plt.show()

# x = linspace(0, 5, 10)
# y = x ** 2
# fig, axes = plt.subplots(1, 2, figsize = (10, 3))
# axes[0].plot(x, x**2, x, x**3, lw = 2)
# axes[0].grid(True)
# axes[1].plot(x, x**2, x, x**3, lw = 2)
# axes[1].grid(color = "b", alpha = 0.7, linestyle = "dashed", linewidth = 0.8)
# plt.show()

# xx = np.linspace(-0.75, 1., 100)
# n = np.array([0, 1, 2, 3, 4, 5])
# fig, axes = plt.subplots(1, 4, figsize = (12, 3))
# axes[0].scatter(xx, xx + 0.25 * randn(len(xx)), color = "black")
# axes[0].set_title("scatter")
# axes[1].step(n, n**2, lw = 2, color = "blue")
# axes[1].set_title("step")
# axes[2].bar(n, n**2, align = "center", width = 0.5, alpha = 0.5, color = "magenta")
# axes[2].set_title("bar")
# axes[3].fill_between(xx, xx**2, xx**3, alpha = 0.5, color = "green")
# axes[3].set_title("fill_between")
# plt.show()

# n = np.random.randn(100000)
# fig, axes = plt.subplots(1, 2, figsize = (12, 4))
# axes[0].hist(n)
# axes[0].set_title("Histograma Padrão")
# axes[0].set_xlim((min(n), max(n)))
# axes[1].hist(n, cumulative = True, bins = 50)
# axes[1].set_title("Histograma Cumulativo")
# axes[1].set_xlim((min(n), max(n)))
# plt.show()



from mpl_toolkits.mplot3d.axes3d import Axes3D
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def ColorMap(phi_m, phi_p):
    return ( + alpha - 2 * np.cos(phi_p)*cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p))

phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(X,Y).T

fig = plt.figure(figsize = (14, 6))
ax = fig.add_subplot(1, 2, 1, projection = "3d")
p = ax.plot_surface(X, Y, Z, rstride = 4, cstride = 4, linewidth = 0)

ax = fig.add_subplot(1, 2, 2, projection = "3d")
p = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.coolwarm, linewidth = 0, antialiased = False)

cb = fig.colorbar(p, shrink = 0.5)
plt.show()
































