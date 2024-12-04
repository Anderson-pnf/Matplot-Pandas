import pandas as pd
import matplotlib.pyplot as plt

arq = 'train_and_test2.csv'

dados = pd.read_csv(arq)

colunas_irrelevantes = [col for col in dados.columns if dados[col].nunique() == 1 ]

data_limpo = dados.drop(columns=colunas_irrelevantes)

data_limpo['Embarked'].fillna(data_limpo['Embarked'].mode()[0], inplace=True)

print('Estastistica')

print(data_limpo.describe())

plt.figure(figsize=(12,5))


#Distribuição por idade
plt.subplot(1,2,1)
plt.hist(data_limpo['Age'], bins = 20, color = 'blue',edgecolor = 'black')
plt.title('Distribuição de idade')
plt.xlabel('Idade')
plt.ylabel('Frequencia')

#Distribuição de tarifa
plt.subplot(1,2,2)
plt.hist(data_limpo['Fare'], bins = 20, color = 'red',edgecolor = 'black')
plt.title('Distribuição de Tarifa')
plt.xlabel('Tarifa')
plt.ylabel('Frequencia')


#Quantidade de sobreviventes por sexo
sobreviventes_por_sexo = data_limpo.groupby('Sex')['2urvived'].mean()
labels = ['M','F']
plt.figure(figsize=(6,6))
plt.bar(labels, sobreviventes_por_sexo, color =['blue','pink'], edgecolor = 'black')
plt.xlabel('Taxa de sobreviventes por sexo')
plt.ylabel('Taxa de sobrevivencia')

#Quantidade de sobreviventes por Classe
sobreviventes_por_classe = data_limpo.groupby('Pclass')['2urvived'].mean()
plt.figure(figsize=(6,6))
plt.bar(sobreviventes_por_classe.index,sobreviventes_por_classe , color =['orange','purple'], edgecolor = 'black')
plt.xlabel('Taxa de sobreviventes por classe')
plt.ylabel('Taxa de sobrevivencia')

#Quantidade de passageiros que embarcaram por porto

Porto = ['Chebourg','QuensTown','Southampton']
data_limpo['Embarked'] = data_limpo['Embarked'].map({0.0:'Chebourng',1.0:'QuensTown',2.0:'Southampton'})
embarked_count = data_limpo['Embarked'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(embarked_count,labels=embarked_count.index,autopct='%1.1f%%', colors = ['brown','green','blue'])
plt.title('Distribuição de embarque')

plt.tight_layout()
plt.show()