import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

anos=[2018,2019,2020,2021,2022]
info = ['IN_INTERNET','IN_LABORATORIO_CIENCIAS']
admDep={'MUNICIPAL':3,'ESTADUAL':2,'FEDERAL':1,'PRIVADA':4}
dados=pd.DataFrame(index=pd.MultiIndex.from_product([list(admDep.keys()),info]),columns=anos)

for ano in anos:
    csv=pd.read_csv('microdados_ed_basica_'+str(ano)+'.csv',sep=';',encoding='latin-1',low_memory=False)
    total=len(csv['NO_ENTIDADE'])
    for j in admDep.keys():
        dep=csv[csv['TP_DEPENDENCIA']==admDep[j]]
        for i in info:
            dados[ano].loc[j,i]=len(dep[dep[i]==1])
        
i=0
c=['tab:blue','tab:green','tab:red','tab:purple']
fig, ax = plt.subplots(figsize=(10.8, 10.8))
ax.grid(color='b',alpha=0.2,linestyle='dashed',linewidth=1)
plt.subplot(1,1,1)
plt.title("Escolas declaradas com acesso à internet e laboratório de ciências")
for dep in admDep.keys():
    plt.plot(dados.loc[(dep,'IN_INTERNET')].index,dados.loc[(dep,'IN_INTERNET')].values,color=c[i],marker='o',label=str(dep[0])+str(dep[1:3].lower())+'. com Internet')
    plt.plot(dados.loc[(dep,'IN_LABORATORIO_CIENCIAS')].index,dados.loc[(dep,'IN_LABORATORIO_CIENCIAS')].values,color=c[i],marker='s',linestyle='--',label=str(dep[0])+str(dep[1:3].lower())+'. com Laboratório')
    i+=1

plt.legend()
plt.savefig('Bruto.png')