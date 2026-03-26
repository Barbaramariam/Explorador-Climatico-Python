import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  

st.set_page_config(
    page_title="Explorador Climático",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("🌍 Explorador de Datos Climáticos")

class ExploradorClimatico:
    def __init__(self):
        self.datos = []
        self.datos_cargados = False  
    
    def cargar_datos_csv(self, uploaded_file):
        try:    
            self.datos = pd.read_csv(uploaded_file).to_dict('records')
            self.datos_cargados = True
            return True, "¡Datos cargados correctamente! 😊"
        except Exception as e:
            return False, f"Error al cargar: {str(e)}"
    
    # Calcular temperatura promedio
    def calcular_promedio(self):
        if not self.datos_cargados:
            return False, "Carga datos primero"
        
        try:
            temps = [r['AvgTemperature'] for r in self.datos]
            promedio = sum(temps) / len(temps)
            return True, round(promedio, 2)
        except:
            return False, "Error en el cálculo"

    # Encontrar temperaturas máximas y mínimas
    def temperaturas_extremas(self):
        if not self.datos_cargados:
            return False, "Carga datos primero"
        
        try:
            temps = [r['AvgTemperature'] for r in self.datos]
            max_temp = max(temps)
            min_temp = min(temps)
            
            max_reg = [r for r in self.datos if r['AvgTemperature'] == max_temp]
            min_reg = [r for r in self.datos if r['AvgTemperature'] == min_temp]
            
            return True, (max_temp, min_temp, max_reg, min_reg)
        except Exception as e:
            return False, f"Algo falló: {str(e)}"

    # Filtrar registros 
    def filtrar_registros(self, valor, operacion):
        if not self.datos_cargados:
            return False, "Carga datos primero"
        
        try:
            valor = float(valor)
            resultados = []
            
            for registro in self.datos:
                temp = registro['AvgTemperature']
                if operacion == "mayor" and temp > valor:
                    resultados.append(registro)
                elif operacion == "menor" and temp < valor:
                    resultados.append(registro)
            
            return True, resultados
        except:
            return False, "Error al filtrar"

    # Gráficos
    def generar_graficos(self):
        if not self.datos_cargados:
            return False, "Carga datos primero"
        
        try:
            fig, axs = plt.subplots(1, 2, figsize=(15, 5))
            
            # Histograma
            temps = [r['AvgTemperature'] for r in self.datos]
            axs[0].hist(temps, bins=15, color='blue')
            axs[0].set_title("Distribución de Temperaturas")
            axs[0].set_xlabel("Temperatura (°F)")
            axs[0].grid(True)
            
            # Gráfico de dispersión
            dias = [r['Day'] for r in self.datos]
            axs[1].scatter(dias, temps, color='green')
            
            try:
                coef = np.polyfit(dias, temps, 1)
                trend = np.poly1d(coef)
                axs[1].plot(dias, trend(dias), color='red', linestyle='--')
            except:
                pass

            axs[1].set_title("Temperatura por Día")
            axs[1].set_xlabel("Día del mes")
            axs[1].grid(True)
            
            plt.tight_layout()
            return True, fig
        except Exception as e:
            return False, f"Error con los gráficos: {str(e)}"

if 'app_data' not in st.session_state:
    st.session_state.app_data = ExploradorClimatico()

# Menú principal
opcion = st.sidebar.selectbox(
    "Menú Principal",
    [
        "Cargar datos",
        "Estadísticas",
        "Filtrar datos",
        "Gráficos",
        "Ver datos completos",
        "Salir"
    ]
)

if opcion == "Cargar datos":
    st.header("📤 Subir archivo CSV")
    archivo = st.file_uploader("Selecciona tu archivo de datos climáticos", type="csv")
    if archivo is not None:
        ok, mensaje = st.session_state.app_data.cargar_datos_csv(archivo)
        if ok:
            st.success(mensaje)
        else:
            st.error(mensaje)

elif not st.session_state.app_data.datos_cargados:
    st.warning("⚠️ Primero carga un archivo CSV")

elif opcion == "Estadísticas":
    st.header("📊 Estadísticas Básicas")
    
    ok, promedio = st.session_state.app_data.calcular_promedio()
    if ok:
        st.metric("Temperatura Promedio", f"{promedio} °F")
    else:
        st.error(promedio)
    
    ok, datos_extremos = st.session_state.app_data.temperaturas_extremas()
    if ok:
        col1, col2 = st.columns(2)
        col1.metric("Temperatura Máxima", f"{datos_extremos[0]} °F")
        col2.metric("Temperatura Mínima", f"{datos_extremos[1]} °F")
    else:
        st.error(datos_extremos)

elif opcion == "Filtrar datos":
    st.header("🔎 Filtrar Registros")
    
    temps = [r['AvgTemperature'] for r in st.session_state.app_data.datos]
    valor_umbral = st.slider(
        "Selecciona temperatura:",
        min_value=min(temps),
        max_value=max(temps),
        value=(min(temps) + max(temps)) / 2
    )
    
    tipo_filtro = st.radio(
        "Filtrar registros:",
        ["Mayores a", "Menores a"],
        horizontal=True
    )
    
    if st.button("Aplicar filtro"):
        operacion = "mayor" if tipo_filtro == "Mayores a" else "menor"
        ok, resultados = st.session_state.app_data.filtrar_registros(valor_umbral, operacion)
        
        if ok:
            st.dataframe(resultados)
        else:
            st.error(resultados)

elif opcion == "Gráficos":
    st.header("📈 Visualización")
    ok, fig = st.session_state.app_data.generar_graficos()
    if ok:
        st.pyplot(fig)
    else:
        st.error(fig)

elif opcion == "Ver datos completos":
    st.header("📋 Datos Completos")
    if st.session_state.app_data.datos_cargados:
        st.dataframe(st.session_state.app_data.datos)
    else:
        st.warning("Primero carga los datos")

elif opcion == "Salir":
    st.info("¡Vuelva pronto! 👋")
    st.session_state.app_data = ExploradorClimatico()
    
st.sidebar.markdown("---")
st.markdown("---")
# Línea modificada:
st.caption("Proyecto Final - Introducción a la Computación | Estudiante: Bárbara Fernández")