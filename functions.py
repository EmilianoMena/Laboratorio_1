# Librerias
import pandas as pd
import data as d
import numpy as np

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
peso_cash_p= round(100-d.df['Peso (%)'].sum(),2)
cash_p=((peso_cash_p*ci)/100)+(ip_inicial['Efectivo'].sum())
comisiones_p=ip_inicial['Comisiones'].sum()
## df_pasiva
ip=[]
dates=d.dates
for date in dates:
    inversion=(d.precios[date].values.tolist()*ip_inicial['Titulos']).sum()
    ip.append({
        'Timestamp':date,
        'Capital':round(inversion,2)+cash_p-comisiones_p
    })
df_pasiva=pd.DataFrame(ip)
df_pasiva['Rendimiento']=df_pasiva['Capital'].pct_change().fillna(0)
df_pasiva['Rendimiento_Acumulado']=(1+df_pasiva['Rendimiento']).cumprod()-1
