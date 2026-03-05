import matplotlib.pyplot as plt


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

vendas = [120, 90, 150, 80, 200, 52, 85, 96, 41, 546, 84, 514]


plt.bar(meses, vendas, color='royalblue')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.ylim(0, 550)
plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550,])
plt.yticks(fontsize=10)
plt.grid(True, color='black')
plt.tight_layout()


plt.xticks(rotation=50)


plt.title('Vendas mensais')


plt.show()
