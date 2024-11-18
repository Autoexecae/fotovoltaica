import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Cálculo de Temperatura de Célula (Tc) y Potencia (P)")

# Descripción
st.write("""
Esta aplicación calcula:
1. La **temperatura de célula (Tc)** utilizando la fórmula:
   \\[
   Tc = Ta + \\frac{G \cdot (\text{TONC} - 20)}{800}
   \\]
2. La **potencia (P)** de un panel solar con la fórmula:
   \\[
   P = Pmp \\cdot \\left(1 + \\frac{Cp}{100} \\cdot (Tc - 25)\\right) \\cdot \\frac{G}{1000}
   \\]

Ingrese los parámetros necesarios en la barra lateral y observe los resultados y el gráfico generado.
""")

# Entradas en la barra lateral
st.sidebar.header("Entradas de Usuario")
# Parámetros para Tc
Ta = st.sidebar.number_input("Temperatura Ambiente (Ta, °C)", value=25.0, step=0.1)
G_min = st.sidebar.number_input("Irradiancia mínima (G, W/m²)", value=200.0, step=50.0)
G_max = st.sidebar.number_input("Irradiancia máxima (G, W/m²)", value=1200.0, step=50.0)
TONC = st.sidebar.number_input("TONC (°C)", value=45.0, step=0.1)

# Parámetros para P
Pmp = st.sidebar.number_input("Potencia nominal del panel (Pmp, W)", value=400.0, step=1.0)
Cp = st.sidebar.number_input("Coeficiente de potencia (Cp, %/°C)", value=-0.4, step=0.1)

# Crear un rango de irradiancias
G_values = np.linspace(G_min, G_max, 100)

# Cálculo de Tc
Tc_values = Ta + (G_values * (TONC - 20) / 800)

# Cálculo de P
P_values = Pmp * (1 + (Cp / 100) * (Tc_values - 25)) * (G_values / 1000)

# Mostrar el resultado para el valor máximo de irradiancia
st.subheader("Resultados")
Tc_max = Tc_values[-1]
P_max = P_values[-1]
st.write(f"Para G = {G_max} W/m²:")
st.write(f"- La **temperatura de célula (Tc)** es: **{Tc_max:.2f} °C**")
st.write(f"- La **potencia (P)** es: **{P_max:.2f} W**")

# Gráfico del cálculo
st.subheader("Gráfico de Tc y P en función de G")
fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de Tc
ax1.plot(G_values, Tc_values, label="Tc (Temperatura de Célula)", color="blue")
ax1.set_xlabel("Irradiancia (G, W/m²)")
ax1.set_ylabel("Temperatura de Célula (Tc, °C)", color="blue")
ax1.tick_params(axis='y', labelcolor="blue")
ax1.grid(True)

# Gráfico de P
ax2 = ax1.twinx()
ax2.plot(G_values, P_values, label="P (Potencia)", color="green")
ax2.set_ylabel("Potencia (P, W)", color="green")
ax2.tick_params(axis='y', labelcolor="green")

# Títulos y leyendas
fig.suptitle("Relación entre Irradiancia (G), Tc y P")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# Mostrar el gráfico
st.pyplot(fig)
