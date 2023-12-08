import streamlit as st
import requests
import seaborn
import pandas as pd
from pydantic import BaseModel

class Item(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    #island: object
    #sex: object


st.title("PEINGOUIN APP")


X = seaborn.load_dataset("penguins")
slider_values = {}
selected_options = {}

button_penguin = st.button("Show Pingouin Columns")
if button_penguin:
    st.write("Colonnes du dataset :")
    st.write(X.columns)

num_rows = st.slider("Nombre de lignes à afficher", min_value=1, max_value=len(X), value=10)

button_penguin = st.button("Show Pingouin Head")
if button_penguin:
    st.write("Aperçu des données :")
    st.write(X.head(num_rows))





# Créer des options de choix pour les variables qualitatives dans la barre latérale
st.sidebar.header("Variables Quantitatives")
quantitative_columns = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
for col in quantitative_columns:
    slider_value = st.sidebar.slider(f"{col}", float(X[col].min()), float(X[col].max()), float(X[col].mean()))
    slider_values[col] = slider_value

# st.sidebar.header("Variables Qualitatives")
# qualitative_columns = ['island', 'sex']
# for col in qualitative_columns:
#     options = X[col].unique()
#     selected_option = st.sidebar.selectbox(f"{col}", options)
#     selected_options[col] = selected_option


predict_button = st.sidebar.button("Prédire")
if predict_button:
    # Générer les prédictions à partir des valeurs sélectionnées

    st.write("Valeurs sélectionnées:")
    st.write("Quantitatives:", slider_values)
    #st.write("Qualitatives:", selected_options)

    item = Item(
        bill_length_mm=slider_values['bill_length_mm'],
        bill_depth_mm=slider_values['bill_depth_mm'],
        flipper_length_mm=slider_values['flipper_length_mm'],
        body_mass_g=slider_values['body_mass_g']
        #island=selected_options['island'],
        #sex=selected_options['sex']
    )
    # Changez cette ligne de requests.get à requests.post
    response = requests.post("http://server:8000/predict", json=item.dict())

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response.json())

        prediction = response.json()["prediction"]
        st.write(f"Prédiction : {prediction}")
    else:
        st.error(f"FAILED Server returned {response.status_code} status.")

