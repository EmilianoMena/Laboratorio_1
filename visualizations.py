# Librerias
import pandas as pd
import matplotlib.pyplot as plt
import functions as f
import data as d

# Inversión Pasiva
## 
data=f.ip_inicial['Peso (%)']
labels=f.ip_inicial['Symbols']
plt.pie(data, labels=labels, autopct='%.0f%%')
