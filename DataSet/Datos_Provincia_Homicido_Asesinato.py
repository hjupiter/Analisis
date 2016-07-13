import csv
import pandas as pd

data = pd.read_csv("dataCSV.csv")

d =  data[["Provincia","tipo_muert_matriz"]]

c = d.groupby("Provincia").count()

c.to_csv("Datos_Provincia_Homicidio_Asesinato.csv")