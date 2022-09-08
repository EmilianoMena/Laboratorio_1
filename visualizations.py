# Librerias
import pandas as pd
import matplotlib.pyplot as plt
import functions as f
import data as d

# Inversión Pasiva
## Distribución de la Inversión Pasiva
x=f.df_pasiva['Timestamp']
y=f.df_pasiva['Capital']
ip_g1=plt.plot(x,y)
ip_g1=plt.xlabel('Fecha')
ip_g1=plt.ylabel('Capital')
ip_g1=plt.title('Serie de Tiempo del Capital en la Inversión Pasiva')
ip_g1=plt.show()
print(ip_g1)