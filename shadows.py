import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la distancia mínima (sombra)
def calcular_sombra(alpha, beta, latitud):
    # Convertir grados a radianes
    beta_rad = np.radians(beta)
    latitud_rad = np.radians(latitud)
    
    # Aplicar la fórmula
    Dm = (alpha * np.cos(beta_rad)) + (alpha * np.sin(beta_rad) / np.tan(np.radians(61 - latitud))) * 1.25
    return Dm

# Titulo y descripción
st.title("Calculadora de Sombra para Panel Solar")
st.write("""
    Esta aplicación te ayudará a calcular la sombra proyectada por tu panel solar, 
    según el ángulo de inclinación y la latitud de tu ubicación.
    """)

# Inputs del usuario
alpha = st.number_input("Introduce el valor de α (longitud del panel en metros):", min_value=0.1, value=1.5)
beta = st.slider("Selecciona el ángulo de inclinación β (en grados):", min_value=0, max_value=90, value=30)
latitud = st.number_input("Introduce la latitud de tu ubicación (en grados):", min_value=-90, max_value=90, value=0)

# Calcular la sombra
dm = calcular_sombra(alpha, beta, latitud)

# Mostrar la distancia mínima
st.write(f"La distancia mínima de la sombra proyectada por el panel solar es: {dm:.2f} metros.")

# Generar gráfico
fig, ax = plt.subplots(figsize=(6, 6))

# Coordenadas del panel solar
panel_x = [0, alpha * np.cos(np.radians(beta))]
panel_y = [0, alpha * np.sin(np.radians(beta))]

# Dibujar el panel solar
ax.plot(panel_x, panel_y, label="Panel Solar", color='b', linewidth=4)

# Proyectar la sombra
shadow_x = [panel_x[1], panel_x[1] + dm]
shadow_y = [panel_y[1], 0]
ax.plot(shadow_x, shadow_y, label="Sombra proyectada", color='r', linestyle='--', linewidth=2)

# Configuración del gráfico
ax.set_xlim(-2, max(shadow_x) + 2)
ax.set_ylim(-2, alpha + 2)
ax.set_xlabel("Distancia (metros)")
ax.set_ylabel("Altura (metros)")
ax.set_title("Cálculo de Sombra de Panel Solar")
ax.legend()
ax.grid(True)

# Mostrar gráfico
st.pyplot(fig)
