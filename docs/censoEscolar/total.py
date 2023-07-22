import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

anos=[2018,2019,2020,2021,2022]
total={2018:0,2019:0,2020:0,2021:0,2022:0}
info = ['IN_INTERNET','IN_LABORATORIO_CIENCIAS']
dadosT=pd.DataFrame(index=info,columns=anos)
dadosP=pd.DataFrame(index=info,columns=anos)

for ano in anos:
    csv=pd.read_csv('microdados_ed_basica_'+str(ano)+'.csv',sep=';',encoding='latin-1',low_memory=False)
    csv=csv[csv['TP_SITUACAO_FUNCIONAMENTO']==1]
    csv=csv[csv['IN_INTERNET']!='']
    #csv=csv[csv['IN_MED']==1]
    total[ano]=len(csv['NO_ENTIDADE'])
    for i in info:
        dadosT[ano].loc[i]=len(csv[csv[i]==1])

fig, ax = plt.subplots(figsize=(10.8, 10.8))
plt.title('Acesso a Internet e/ou Laboratório',size=20)
plt.subplot(1,1,1)
ax.grid(color='b',alpha=0.2,linestyle='dashed',linewidth=1)
x=anos
yi=np.round(list(100*dadosT.loc['IN_INTERNET'].values/np.array(list(total.values()))),2)
yl=np.round(list(100*dadosT.loc['IN_LABORATORIO_CIENCIAS'].values/np.array(list(total.values()))),2)
plt.ylabel('Percentual de escolas declarantes com acesso',size=16)
plt.xlabel('Ano',size=16)
plt.plot(x,yi,marker='v',color='b',linestyle='--',label='Todos os Níveis de Ensino com Internet')
plt.plot(x,yl,marker='x',color='c',linestyle='--',label='Todos os Níveis de Ensino com Laboratório')
plt.xticks(x)
for i in range(len(x)):
  ax.text(x[i],yi[i]-3.5,"{:.2f}%".format(yi[i]),ha='center', size=16)
  ax.text(x[i],yl[i]-3.5,"{:.2f}%".format(yl[i]),ha='center', size=16)


anos=[2018,2019,2020,2021,2022]
total={2018:0,2019:0,2020:0,2021:0,2022:0}
info = ['IN_INTERNET','IN_LABORATORIO_CIENCIAS']
dadosT=pd.DataFrame(index=info,columns=anos)
dadosP=pd.DataFrame(index=info,columns=anos)

for ano in anos:
    csv=pd.read_csv('microdados_ed_basica_'+str(ano)+'.csv',sep=';',encoding='latin-1',low_memory=False)
    csv=csv[csv['TP_SITUACAO_FUNCIONAMENTO']==1]
    csv=csv[csv['IN_INTERNET']!='']
    csv=csv[csv['IN_MED']==1]
    total[ano]=len(csv['NO_ENTIDADE'])
    for i in info:
        dadosT[ano].loc[i]=len(csv[csv[i]==1])

x=anos
yi=np.round(list(100*dadosT.loc['IN_INTERNET'].values/np.array(list(total.values()))),2)
yl=np.round(list(100*dadosT.loc['IN_LABORATORIO_CIENCIAS'].values/np.array(list(total.values()))),2)
plt.plot(x,yi,marker='o',color='g',label='Ensino Médio com Internet')
plt.plot(x,yl,marker='s',color='m',label='Ensino Médio com Laboratório')
plt.xticks(x)
for i in range(len(x)):
  ax.text(x[i],yi[i]-3.5,"{:.2f}%".format(yi[i]),ha='center', size=16)
  ax.text(x[i],yl[i]-3.5,"{:.2f}%".format(yl[i]),ha='center', size=16)

plt.legend()
plt.savefig('Total.png')