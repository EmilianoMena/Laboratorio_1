# Librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions as f
import data as d

# Inversión Pasiva
## Distribución de la Inversión Pasiva
ip_g1=f.df_pasiva['Capital'].plot(figsize=(12,7))
ip_g1=plt.xlabel('Fecha')
ip_g1=plt.ylabel('Capital')
ip_g1=plt.title('Serie de Tiempo del Capital en la Inversión Pasiva')
ip_g2=f.df_pasiva['Rendimiento'].plot(figsize=(12,7))
ip_g2=plt.xlabel('Fecha')
ip_g2=plt.ylabel('Rendimiento')
ip_g2=plt.title('Serie de Tiempo del Capital en la Inversión Pasiva')
ip_g3=f.df_pasiva['Rendimiento_Acumulado'].plot(figsize=(12,7))
ip_g3=plt.xlabel('Fecha')
ip_g3=plt.ylabel('Rendimiento Acumulado')
ip_g3=plt.title('Serie de Tiempo del Capital en la Inversión Pasiva')
ip_g4=plt.pie(f.ip_activos['Peso (%)'],labels=f.ip_activos['Activos'],autopct='%0.1f %%')