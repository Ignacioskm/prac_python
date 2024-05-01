import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

ruta_archivo_csv = r'C:\Users\SK\Desktop\Proyectos SQL\Proyectos Python\dataset_banco.csv'
data = pd.read_csv(ruta_archivo_csv)

print(data.shape)
data.head()
data.info()