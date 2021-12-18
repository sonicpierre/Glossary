import streamlit as st
import gestion_BBD as bdd
import utils as ut

db = bdd.connexion(st.secrets["textkey"], "michelin-4180a")

ajout = ut.construction_form_sidebar()

st.markdown('# Michelin Research Glossary')

form_recherche = st.form("Recherche form")
form_recherche.text_input("Indicateur")
form_recherche.text_input("Edude")
recherche = form_recherche.form_submit_button("Rechercher")


bdd.lecture_data(db, "posts")