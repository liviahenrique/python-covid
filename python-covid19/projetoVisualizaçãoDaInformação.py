import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv')

fig = go.Figure(
    data=go.Choropleth(
        locations=df['countriesAndTerritories'],  # Nome do país
        z=df['cases'],  # Dados para o Choropleth
        locationmode='country names',  # Tipo de identificção geográfica
        autocolorscale=True,
        colorbar_title="Casos",
    ))
fig.update_layout(
    title_text='Distribuição dos casos de COVID-19 na América do sul',
    geo_scope='south america',  # Limita escopo para a América do Sul
)
fig.show()

brasil = df[df.countriesAndTerritories.eq('Brazil')]
totaisBra = brasil.sum(axis=0, skipna=True)

colunas = ('Casos', 'Mortes')
indice = np.arange(len(colunas))
valores = [totaisBra["cases"], totaisBra["deaths"]]
plt.bar(indice, valores)
plt.xticks(indice, colunas)
plt.ylabel('Notificações')
plt.title('Resumo do COVID-19 no Brasil')
plt.show()

esp = df[df.countriesAndTerritories.eq('Spain')]
totaisEsp = esp.sum(axis=0, skipna=True)

ita = df[df.countriesAndTerritories.eq('Italy')]
totaisIta = ita.sum(axis=0, skipna=True)

uk = df[df.countriesAndTerritories.eq('United_Kingdom')]
totaisUk = uk.sum(axis=0, skipna=True)

usa = df[df.countriesAndTerritories.eq('United_States_of_America')]
totaisUsa = usa.sum(axis=0, skipna=True)

labels = ('Brasil', 'Estados Unidos', 'Espanha', 'Reino Unido', 'Itália')
indice = np.arange(len(labels))

sizes = [totaisBra["cases"] / brasil["popData2019"].iloc[0] * 100,
           totaisUsa["cases"] / usa["popData2019"].iloc[0] * 100,
           totaisEsp["cases"] / esp["popData2019"].iloc[0] * 100,
           totaisUk["cases"] / uk["popData2019"].iloc[0] * 100,
           totaisIta["cases"] / ita["popData2019"].iloc[0] * 100]

colors = ['gold', 'yellowgreen', 'coral',
          'lightskyblue', 'red']

patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%',
                                    startangle=90)
plt.legend(patches, labels, loc="lower right")
plt.axis('equal')
plt.title('Proporção da População sobre Números de casos COVID-19')
plt.show()
