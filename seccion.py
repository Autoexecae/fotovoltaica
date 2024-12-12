import streamlit as st

def calcular_seccion(I, L, valor, caida_tension, conductividad):
    """
    Calcula la sección del cable según la fórmula dada.
    """
    S = 2 * I * L / ((valor * caida_tension / 100) * conductividad)
    return S

# Propiedades de conductividad
CONDUCTIVIDAD_COBRE = 56  # En m/(Ohm*mm2) a 45°C
CONDUCTIVIDAD_ALUMINIO = 35  # En m/(Ohm*mm2) a 27.8°C

def main():
    st.title("Calculadora de Sección de Cable")
    st.write("Esta aplicación calcula la sección del cable en m².")
    
    # Inicializar session state para almacenar resultados
    if "resultados" not in st.session_state:
        st.session_state.resultados = []
    
    # Entrada de datos
    nombre_tramo = st.text_input("Nombre del tramo:", "Tramo 1")
    
    # Selección de material
    material = st.selectbox("Selecciona el material del cable:", ["Cobre", "Aluminio"])
    
    # Definir la conductividad según el material
    if material == "Cobre":
        conductividad = CONDUCTIVIDAD_COBRE
    else:
        conductividad = CONDUCTIVIDAD_ALUMINIO
    
    # Entradas numéricas
    I = st.number_input("Intensidad (I) en Amperios:", min_value=0.0, step=0.1)
    L = st.number_input("Longitud del tramo (L) en metros:", min_value=0.0, step=0.1)
    valor = st.number_input("Valor de la Tension en Voltios:", min_value=0.0, step=0.1)
    caida_tension = st.number_input("Caída de tensión (%):", min_value=0.0, step=0.1)
    
    # Botón para calcular
    if st.button("Calcular Sección"):
        if caida_tension > 0 and conductividad > 0:
            S = calcular_seccion(I, L, valor, caida_tension, conductividad)
            resultado = f"{nombre_tramo}: La sección calculada es: {S:.4f} m²"
            st.success(resultado)
            st.session_state.resultados.append(resultado)
        else:
            st.error("Por favor, asegúrate de que la caída de tensión y la conductividad sean mayores a 0.")
    
    # Botón para reiniciar
    if st.button("Reiniciar"):
        st.session_state.resultados = []
        st.experimental_rerun()
    
    # Mostrar resultados guardados
    if st.session_state.resultados:
        st.write("### Resultados Guardados")
        for res in st.session_state.resultados:
            st.write(res)

if __name__ == "__main__":
    main()
