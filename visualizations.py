# Librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import functions as f
import data as d

# Inversión Pasiva
## Distribución de la Inversión Pasiva
ip_g1=plt.plot(f.df_pasiva['Timestamp'],f.df_pasiva['Capital'])
ip_g1=plt.xlabel('Fecha')
ip_g1=plt.ylabel('Capital')
ip_g1=plt.title('Serie de Tiempo del Capital en la Inversión Pasiva')
ip_g1=plt.show()
ip_g2=plt.plot(f.df_pasiva['Timestamp'],f.df_pasiva['Rendimiento'])
ip_g2=plt.xlabel('Fecha')
ip_g2=plt.ylabel('Rendimiento')
ip_g2=plt.title('Serie de Tiempo del Capital en la Inversión Pasiva')
ip_g2=plt.show()
ip_g3=plt.plot(f.df_pasiva['Timestamp'],f.df_pasiva['Rendimiento_Acumulado'])
ip_g3=plt.xlabel('Fecha')
ip_g3=plt.ylabel('Rendimiento Acumulado')
ip_g3=plt.title('Serie de Tiempo del Capital en la Inversión Pasiva')
ip_g3=plt.show()
sns.barplot(f.df_pasiva['Capital'])
