import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre principal
st.title("Visualisation interactive d'une fonction affine avec Streamlit")

# Sliders pour les paramètres a et b
a = st.slider("Pente (a)", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
b = st.slider("Ordonnée à l'origine (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.5)

# Voir la doc officielle : https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
# Génération des valeurs x
x = np.linspace(-10, 10, 100)
# Calcul des valeurs y selon la fonction affine
y = a * x + b

# Création du graphique avec Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a:.2f}x + {b:.2f}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Visualisation de la fonction affine")
ax.legend()

# Affichage du graphique dans Streamlit avec st.pyplot().
st.pyplot(fig)