import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
datas={74,75,77,78,79}

for data in datas:
    csv=pd.read_csv('data ('+str(data)+').csv')
    csv=csv[csv['dist']!=0]
    poly=np.polyfit(0.001*csv['tempo'].values,csv['dist'].values,2)
    m = 99
    min=1000
    r=5.3/2
    g=980
    rho=2.7
    h=4.9
    theta=math.sin(math.radians(2.75))
    acm=poly[0]*2
    i=-1.0*m*r*((g*theta/acm)+1)
    print('Momento de Inércia = '+str(i))
    print('Sendo cilindro maciço com raio '+str(r)+' : massa ='+str(math.sqrt(i*2)))
    print('Sendo cilindro oco com raio externo '+str(r)+' e massa 0.1kg : raio interno'+str(math.sqrt(((i*2)/m)-r**2)))
    for a in range(1000):
        aux=i-(rho*math.pi/2)*(h*(r**4-(r-a/1000)**4)+2.0*(a/1000)*r**4)
        if(aux<min and aux >=0):
            min=aux
            d=a/1000
    print('Sendo cilindro oco com, com tampas, raio externo '+str(r)+' e densidade de 2.7 g/cm³ : espessura = '+str(d))
