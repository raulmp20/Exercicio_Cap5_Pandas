import pandas as pd

df = pd.read_csv('paises.csv', delimiter=';')
#print(df)

#Exercicio 1

oceania_countries = df[df['Region'].str.contains('OCEANIA')]

print(f"Paises que pertencem a Oceania: {oceania_countries}")

oceania_countries_num = oceania_countries.shape[0]

print(f"Numero de paises que pertencem a Oceania: {oceania_countries_num}")

#Exercicio 2

media_alfabetizacao = df["Literacy (%)"].mean()

print(f"Media das taxas de alfabetização: {media_alfabetizacao}")

#Exercicio 3

maior_populacao = df["Population"].idxmax()
pais_maior_populacao = df["Country"][maior_populacao]
regiao_maior_populacao = df["Region"][maior_populacao]

print(f"País com maior populacao: {pais_maior_populacao} pertencente a região {regiao_maior_populacao}")

#Exercicio 4

paises_sem_costa = df["Country"].loc[df["Coastline (coast/area ratio)"] == 0]

print(paises_sem_costa)

paises_sem_costa.to_csv('noCost.csv', sep=";", header=False)
