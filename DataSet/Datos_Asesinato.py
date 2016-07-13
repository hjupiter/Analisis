import csv
import pandas as pd
import provincias as pr

data = pd.read_csv("dataCSV.csv")

data = data[['Provincia','Hora Infraccion','tipo_muert_matriz']]

data = data.replace({'null':'2015-12-02T00:00:00'},regex=True)

c = data.groupby('Provincia')

row =['PROVINCIA','00:00-6:00','6:01-12:00','12:01-18:00','18:01-23:59']

with open('Asesinatos.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(row)
    madrugada = 0
    manana = 0
    tarde = 0
    noche = 0
    for nombre, datos in c:
    	for a,b in zip(datos['Hora Infraccion'],datos['tipo_muert_matriz']):
    		if (a > '2015-12-02T00:00:00') & (a <= '2015-12-02T06:00:00') & (b=='Asesinatos'):
    			madrugada = madrugada +1
    		if (a > '2015-12-02T06:00:00') & (a <= '2015-12-02T12:00:00') & (b=='Asesinatos'):
    			manana = manana +1
    		if (a > '2015-12-02T12:00:00') & (a <= '2015-12-02T18:00:00') & (b=='Asesinatos'):
    			tarde = tarde +1
    		if (a > '2015-12-02T18:00:00') & (a <= '2015-12-02T23:59:59') & (b=='Asesinatos'):
    			noche = noche +1 
    	row[0]=pr.nombre_prov(nombre)
    	row[1]=madrugada
    	row[2]=manana
    	row[3]=tarde
    	row[4]=noche
    	wr.writerow(row)
    	madrugada = 0
    	manana = 0
    	tarde = 0
    	noche = 0