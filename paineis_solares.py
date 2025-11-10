import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns


#              Alunos                           Matrícula
# 
#     Weslley Vieira Garcia             -       1240110431
#     Giovanna da Conceição Gonçalves   -       1240207728
#     Ricardo Fernandes Sette           -       1240117297
#     Letícia Andrade dos Santos        -       1240110654
#     Vitor Hugo Marques Braga          -       1240109418




# PRIMEIRO - WESLLEY

dir = Path.cwd()

planilha = pd.read_csv(dir / 'planilha' / 'painel_solar.csv') 

potencia_em_watts_real = planilha['potencia_gerada_kw'] * 1000

rendimento = (potencia_em_watts_real / (planilha['radiacao_wm2'] * planilha['painel_solar_m2'])) * 100

planilha['Rendimento (%)'] = rendimento

planilha['Rendimento (%)'] = planilha['Rendimento (%)'].round(2)

print(planilha)

#SEGUNDO - RICARDO E GIOVANNA

temperatura = planilha['temperatura_c']
potencia_gerada = planilha['potencia_gerada_kw']

plt.scatter(temperatura, potencia_gerada, marker="v", color='red')
plt.xlabel('Temperatura ℃')
plt.ylabel('Potencia kW')
plt.title('Temperatura X Potencia (kW)')
plt.grid(True)
plt.savefig(dir/ 'graficos' /'dispersao.png')
plt.show()

#TERCEIRO - LETICIA E VITOR

sns.set_theme(style="whitegrid")
plt.figure(figsize=(6,4))

heatmap_data = planilha.pivot_table(index='hora', values='radiacao_wm2', aggfunc='mean')

sns.heatmap(data=heatmap_data, cmap='YlOrRd', annot=True, fmt='.0f')
plt.title('Mapa de calor: Hora x Radiação (W/m2)')
plt.xlabel('Radiação')
plt.ylabel('Hora')
plt.tight_layout()
plt.savefig(dir / 'graficos' / 'heatmap_hora_radiacao.png')
plt.show()