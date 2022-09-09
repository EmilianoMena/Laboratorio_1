# Librerias
from pydoc import render_doc
import pandas as pd
import data as d
import numpy as np
import random

# Datos generales para la creación de ambas estrategias (Pasiva y Activa)
## Capital inicial
ci=1000000
## Comisión por rebalanceo
comision=0.00125
## Tasa Libre de Riesgo
rf=0.0429

## Inversión Pasiva
## Inicio de Inversión Pasiva 
ip_inicial=pd.DataFrame()
ip_inicial['Symbols']=d.tickers
ip_inicial['Peso (%)']=d.pesos
ip_inicial['Precios']=round(d.precios['2020-01-31'],2).values.tolist()
ip_inicial['Posturas']=((ci*ip_inicial['Peso (%)'])/100)
ip_inicial['Titulos']=(ip_inicial['Posturas']/((ip_inicial['Precios'])*(1+comision))).apply(np.floor)
ip_inicial['Comisiones']=round(ip_inicial['Titulos']*ip_inicial['Precios']*comision,2)
ip_inicial['Capital']=round(ip_inicial['Titulos']*ip_inicial['Precios']-ip_inicial['Comisiones'],2)
ip_inicial['Efectivo']=ip_inicial['Posturas']-ip_inicial['Capital']-ip_inicial['Comisiones']
## Cash
ip_pc= round(100-d.df['Peso (%)'].sum(),2)
ip_cash=((ip_pc*ci)/100)+(ip_inicial['Efectivo'].sum())
ip_efectivo=pd.DataFrame()
ip_efectivo['Peso (%)']=ip_pc
ip_efectivo['Cash de Capital Inicial']=(ip_pc*ci)/100
ip_efectivo['Cash Sobrante de Activos']=(ip_inicial['Efectivo'].sum())
ip_efectivo['Cash Total']=ip_cash
## Distribución Inversion Pasiva
ip_activos=pd.DataFrame({'Activos':d.tickers+['CASH'],'Peso (%)':d.pesos+[ip_pc]})
## df_pasiva
ip=[]
ip_comisiones=ip_inicial['Comisiones'].sum()
dates=d.dates
for date in dates:
    inversion=(d.precios[date].values.tolist()*ip_inicial['Titulos']).sum()
    ip.append({
        'Timestamp':date,
        'Capital':round(inversion,2)+ip_pc-ip_comisiones
    })
df_pasiva=pd.DataFrame(ip)
df_pasiva['Rendimiento']=df_pasiva['Capital'].pct_change().fillna(0)
df_pasiva['Rendimiento_Acumulado']=(1+df_pasiva['Rendimiento']).cumprod()-1
