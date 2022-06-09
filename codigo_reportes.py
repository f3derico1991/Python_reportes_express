#                 PANDAS PROFILING

#descarga del paquete (jupiter notebook). En colab tbm en requerida la descarga pero es otro el modo de realizarlo
!pip3 install pandas-profiling[notebook]

#de carga la libreria a usar
from pandas_profiling import ProfileReport
import pandas as pd # solo para crear el dataframe

#DataFrame de ejemplo 
df=pd.read_csv('population_total.csv')

#se instancia con el DataFrame como argumento,  el reporte se guarda en una variable
reporte_cpandas = ProfileReport(df, title="Pandas Profiling Report")

#se descarga el informe en html
reporte_cpandas.to_file("your_report.html")



#                    SWEETVIZ

#se instala la libreria (en colab tambien es necesario)
!pip install sweetviz

#libreria que hace el report
import sweetviz as sv 

# al instanciar pasamos como primer argumento el DataFrame
reporte_df=sv.analyze(df)

# se descarga el informe, en este caso se pide q los datos se muestren de forma vertical
reporte_df.show_html(layout='vertical') 
