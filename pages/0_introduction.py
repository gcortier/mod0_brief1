import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Chargement des données
df = pd.read_csv("./sales_data_sample.csv")



st.title("Exploration des données de ventes")
st.write(" Obligé de réenregistrer le csv en UTF-8 pour éviter les problèmes d'encodage.")



col1, col2 = st.columns(2)

# Afficher les premières lignes du DataFrame à l'aide de 
# data = st.dataframe(df.head())


# col1.header("Filtrer les données par pays")
# country = col1.selectbox("Sélectionner un pays", df["COUNTRY"].unique())
# filtered_df = df[df["COUNTRY"] == country]
# col1.dataframe(filtered_df)



col1.header("Filtrer les données par produit")
products = col1.selectbox("Sélectionner un produit", df["PRODUCTLINE"].unique())
filtered_df_products = df[df["PRODUCTLINE"] == products]
col1.dataframe(filtered_df_products)


fig, ax = plt.subplots(figsize=(10, 6))
grouped = (
    filtered_df_products
    .groupby(['CUSTOMERNAME'])['SALES'].sum()
    .sort_values(ascending=False)
    .reset_index()
    .head(10)
)

grouped.plot(kind='bar', x='CUSTOMERNAME', y='SALES', ax=ax)
col2.header("Visualisation de données")
col2.subheader(f"Ventes par client pour le produit {products}")
col2.pyplot(fig)

st.header("graphique linéaire montrant l'évolution des ventes au fil du temps")

# convert dates to datetime format
df['ORDERDATE'] = pd.to_datetime(filtered_df_products['ORDERDATE'])


sales_per_date = (
    df
    .groupby('ORDERDATE')['SALES'].sum()
    .reset_index()
)

# Plotly express pour interaction ? 
fig = px.line(
    sales_per_date,
    x='ORDERDATE',
    y='SALES',
    title="Évolution des ventes dans le temps",
    labels={"ORDERDATE": "Date", "SALES": "Volume de Ventes"}
)

# Afficher dans Streamlit
st.plotly_chart(fig, use_container_width=True)



# st.button("Download Dataset", key="download_button")
st.download_button(
    label="Télécharger le dataset",
    data=sales_per_date.to_csv(index=False).encode('utf-8'),
    file_name='sales_data_sample_v2.csv',
    mime='text/csv'
)