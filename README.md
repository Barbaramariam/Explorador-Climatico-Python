# Explorador de Datos Climaticos

Este proyecto es una aplicacion web interactiva desarrollada con Python. Su objetivo es permitir la carga, analisis y visualizacion de datos historicos de temperatura de manera eficiente a traves de una interfaz grafica funcional.

El sistema fue desarrollado como proyecto final para la asignatura Introduccion a la Computacion en la Universidad Central de Venezuela (UCV).

## Caracteristicas
* Carga de Datos: Interfaz para subir archivos en formato CSV con registros climaticos.
* Analisis Estadistico: Calculo automatico de promedios, temperaturas maximas y minimas.
* Filtrado de Datos: Herramientas para segmentar registros segun umbrales especificos de temperatura.
* Visualizacion: Generacion de histogramas de distribucion y graficos de dispersion con lineas de tendencia.

## Tecnologias Utilizadas
* Python
* Streamlit
* Pandas
* Matplotlib
* NumPy

## Instalacion y Uso

Para ejecutar este proyecto en un entorno local:

1. **Preparacion de archivos:**
   Asegurese de tener en una misma carpeta los archivos `explorador_climatico.py`, el dataset `archivoTemperaturas.csv` y el archivo `requirements.txt`.

2. **Instalacion de librerias:**
   Abra una terminal (CMD o PowerShell) en la ruta de dicha carpeta y ejecute el siguiente comando para instalar las herramientas necesarias:
   
   pip install -r requirements.txt

3. **Ejecucion de la aplicacion:**
   Inicie el servidor de la aplicacion con el siguiente comando:
   
   streamlit run explorador_climatico.py

   Luego de ejecutarlo, la interfaz se abrira automaticamente en su navegador web.

## Estructura del Repositorio
* `explorador_climatico.py`: Codigo fuente principal con la logica de la aplicacion.
* `archivoTemperaturas.csv`: Dataset de ejemplo utilizado para validar las funciones del sistema.
* `requirements.txt`: Archivo de configuracion con las librerias y versiones requeridas.

