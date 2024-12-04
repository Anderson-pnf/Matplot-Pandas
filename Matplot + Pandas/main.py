import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dados.csv')
print(df)

#primeiras linhas

print(df.head())

#Verificação de dados Ausentes

df.isnull().sum()

#Eliminar as linhas ausentes

df = df.dropna()

#Verificar se estão corretos

print(df.dtypes)

#Estatistica

print(df.describe())

#Agrupar dados por produtos e somar a venda

vendas_por_produto = df.groupby('produto')['total_vendas'].sum()

print(vendas_por_produto)


#Criar gráfico

var = df['preco_unitario']*df['total_vendas']

#BAR

plt.bar(df['produto'],df['total_vendas'],color = 'blue')
plt.title('Vendas de produtos')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.show()

plt.bar(df['produto'],var, color = 'blue')
plt.title('Total vendido por produto')
plt.xlabel('Produto')
plt.ylabel('Valores')
plt.show()

#PLOT

plt.plot(df['produto'],df['total_vendas'],color = 'blue')
plt.title('Vendas de produtos')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.show()

plt.plot(df['produto'],var, color = 'blue')
plt.title('Total vendido por produto')
plt.xlabel('Produto')
plt.ylabel('Valores')
plt.show()

#Dispersão - Scatter - Mostra a relação entre duas variaveis

plt.scatter(df['produto'],df['total_vendas'],color = 'blue')
plt.title('Vendas de produtos')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.show()

plt.scatter(df['produto'],var, color = 'blue')
plt.title('Total vendido por produto')
plt.xlabel('Produto')
plt.ylabel('Valores')
plt.show()

#PIE

plt.pie(df['total_vendas'], labels=df['produto'])
plt.title('Vendas de produtos')
plt.show()

plt.pie(var, labels=df['produto'])
plt.title('Total vendido por produto')
plt.show()


#Perguntas para analise

#Quais produtos tem as maiores vendas totais

#As vendam aumentam com o tempo?

#Existe a relação entre o preço unitario e o total de venda?

#Quais os dias da semana tem as maiores vendas?
