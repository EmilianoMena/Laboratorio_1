# Librerias 
import pandas as pd
import yfinance as yf

# Leer todos los datos necesarios de los archivos NAFTRAC
## Tickers
### NAFTRAC 31/01/2020
tickers_1=pd.read_csv('files/NAFTRAC_20200131.csv',skiprows=2)['Ticker']
### NAFTRAC 28/02/2020
tickers_2=pd.read_csv('files/NAFTRAC_20200228.csv',skiprows=2)['Ticker']
### NAFTRAC 31/03/2020
tickers_3=pd.read_csv('files/NAFTRAC_20200331.csv',skiprows=2)['Ticker']
### NAFTRAC 30/04/2020
tickers_4=pd.read_csv('files/NAFTRAC_20200430.csv',skiprows=2)['Ticker']
### NAFTRAC 29/05/2020
tickers_5=pd.read_csv('files/NAFTRAC_20200529.csv',skiprows=2)['Ticker']
### NAFTRAC 30/06/2020
tickers_6=pd.read_csv('files/NAFTRAC_20200630.csv',skiprows=2)['Ticker']
### NAFTRAC 31/07/2020
tickers_7=pd.read_csv('files/NAFTRAC_20200731.csv',skiprows=2)['Ticker']
### NAFTRAC 31/08/2020
tickers_8=pd.read_csv('files/NAFTRAC_20200831.csv',skiprows=2)['Ticker']
### NAFTRAC 30/09/2020
tickers_9=pd.read_csv('files/NAFTRAC_20200930.csv',skiprows=2)['Ticker']
### NAFTRAC 30/10/2020
tickers_10=pd.read_csv('files/NAFTRAC_20201030.csv',skiprows=2)['Ticker']
### NAFTRAC 30/11/2020
tickers_11=pd.read_csv('files/NAFTRAC_20201130.csv',skiprows=2)['Ticker']
### NAFTRAC 31/12/2020
tickers_12=pd.read_csv('files/NAFTRAC_20201231.csv',skiprows=2)['Ticker']
### NAFTRAC 29/01/2021
tickers_13=pd.read_csv('files/NAFTRAC_20210129.csv',skiprows=2)['Ticker']
### NAFTRAC 26/02/2021
tickers_14=pd.read_csv('files/NAFTRAC_20210226.csv',skiprows=2)['Ticker']
### NAFTRAC 31/03/2021
tickers_15=pd.read_csv('files/NAFTRAC_20210331.csv',skiprows=2)['Ticker']
### NAFTRAC 30/04/2021
tickers_16=pd.read_csv('files/NAFTRAC_20210430.csv',skiprows=2)['Ticker']
### NAFTRAC 31/05/2021
tickers_17=pd.read_csv('files/NAFTRAC_20210531.csv',skiprows=2)['Ticker']
### NAFTRAC 30/06/2021
tickers_18=pd.read_csv('files/NAFTRAC_20210630.csv',skiprows=2)['Ticker']
### NAFTRAC 30/07/2021
tickers_19=pd.read_csv('files/NAFTRAC_20210730.csv',skiprows=2)['Ticker']
### NAFTRAC 31/08/2021
tickers_20=pd.read_csv('files/NAFTRAC_20210831.csv',skiprows=2)['Ticker']
### NAFTRAC 30/09/2021
tickers_21=pd.read_csv('files/NAFTRAC_20210930.csv',skiprows=2)['Ticker']
### NAFTRAC 26/10/2021
tickers_22=pd.read_csv('files/NAFTRAC_20211026.csv',skiprows=2)['Ticker']
### NAFTRAC 30/11/2021
tickers_23=pd.read_csv('files/NAFTRAC_20211130.csv',skiprows=2)['Ticker']
### NAFTRAC 31/12/2021
tickers_24=pd.read_csv('files/NAFTRAC_20211231.csv',skiprows=2)['Ticker']
### NAFTRAC 26/01/2022
tickers_25=pd.read_csv('files/NAFTRAC_20220126.csv',skiprows=2)['Ticker']
### NAFTRAC 28/02/2022
tickers_26=pd.read_csv('files/NAFTRAC_20220228.csv',skiprows=2)['Ticker']
### NAFTRAC 31/03/2022
tickers_27=pd.read_csv('files/NAFTRAC_20220331.csv',skiprows=2)['Ticker']
### NAFTRAC 29/04/2022
tickers_28=pd.read_csv('files/NAFTRAC_20220429.csv',skiprows=2)['Ticker']
### NAFTRAC 31/05/2022
tickers_29=pd.read_csv('files/NAFTRAC_20220531.csv',skiprows=2)['Ticker']
### NAFTRAC 30/06/2022
tickers_30=pd.read_csv('files/NAFTRAC_20220630.csv',skiprows=2)['Ticker']
### NAFTRAC 29/07/2022
tickers_31=pd.read_csv('files/NAFTRAC_20220729.csv',skiprows=2)['Ticker']
## Pesos 
### NAFTRAC 31/01/2020
pesos_1=pd.read_csv('files/NAFTRAC_20200131.csv',skiprows=2)[['Ticker','Peso (%)']].dropna()

# Elegir los tickers con presencia en todos los archivos
## Juntar archivos de Tickers
naftrac=[tickers_1, tickers_2, tickers_3, tickers_4, tickers_5, tickers_6, tickers_7, tickers_8, tickers_9,
tickers_10, tickers_11, tickers_12, tickers_13, tickers_14, tickers_15, tickers_16, tickers_17, tickers_18,
tickers_19, tickers_20, tickers_21, tickers_22, tickers_23, tickers_24, tickers_25, tickers_26, tickers_27,
tickers_28, tickers_29, tickers_30, tickers_31]
tickers_ip=pd.concat(naftrac, axis=0).T
## Evaluar cuales Tickers cumplen con la presencia en los 31 archivos
tickers_ip=tickers_ip.value_counts()>=31
tickers_ip=pd.DataFrame(tickers_ip[tickers_ip==True]).reset_index()
tickers_ip=tickers_ip.rename(columns={'index':'Ticker','Ticker':'Ocurrence'})
## Eliminar los datos en blanco y el ticker MXN que cuenta como CASH
tickers_ip=tickers_ip.drop([2,3]).reset_index().drop('index', axis=1)
## Tickers elegidos con sus pesos del primer archivo
df=pd.merge(tickers_ip,pesos_1,on='Ticker',how='left').dropna().reset_index()
df=df.drop(['index','Ocurrence'], axis=1)
df=df.sort_values('Ticker').reset_index().drop('index', axis=1)

# Obtener los precios de cierre diarios 
## Tickers para el portafolio
tickers= ['AC.MX', 'ALFAA.MX', 'ALSEA.MX', 'AMXL.MX', 'ASURB.MX', 'BBAJIOO.MX', 'BIMBOA.MX', 'BOLSAA.MX', 
'CEMEXCPO.MX', 'CUERVO.MX', 'ELEKTRA.MX', 'FEMSAUBD.MX', 'GAPB.MX', 'GCARSOA1.MX', 'GFINBURO.MX', 'GFNORTEO.MX', 
'GMEXICOB.MX', 'GRUMAB.MX', 'KIMBERA.MX', 'KOFUBL.MX', 'LABB.MX', 'LIVEPOLC-1.MX', 'MEGACPO.MX', 
'OMAB.MX', 'ORBIA.MX', 'PE&OLES.MX', 'PINFRA.MX', 'TLEVISACPO.MX', 'WALMEX.MX']
## Fechas de Archivos NAFTRAC
dates=['2020-01-31','2020-02-28','2020-03-31','2020-04-30','2020-05-29','2020-06-30','2020-07-31','2020-08-31',
'2020-09-30','2020-10-30','2020-11-30','2020-12-31','2021-01-29','2021-02-26','2021-03-31','2021-04-30',
'2021-05-31','2021-06-30','2021-07-30','2021-08-31','2021-09-30','2021-10-26','2021-11-30','2021-12-31',
'2022-01-26','2022-02-28','2022-03-31','2022-04-29','2022-05-31','2022-06-30','2022-07-29']
## Peso correspondiente a los diferentes Tickers
pesos=df['Peso (%)'].values.tolist()
## Fechas de inicio y fin del periodo
start= '2020-01-31'
end='2022-07-30'
## Funcion de yahoo finance para descargar los precios
precios=yf.download(tickers=tickers, start=start, end=end, interval='1d')
precios=precios['Close'].T