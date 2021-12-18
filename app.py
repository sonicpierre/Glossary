import streamlit as st
import gestion_BBD as bdd
import utils as ut

db = bdd.connexion(st.secrets["textkey"], "michelin-4180a")

ajout, dico_entree = ut.construction_form_sidebar()

if ajout:
    if (dico_entree['Name']!= ""):
        bdd.ecriture_data(db, 'Indicateur', dico_entree)
    else :
        st.sidebar.error("Please enter the name of an indicator !")

st.markdown('# Macro indicator research glossary')

st.write('''We are doing more and more studies to understand and visualize the different economic macro indicators. 
However, in order to avoid doing the same research several times and facing unnecessary problems this small application 
has been set up to list everything that has been done on this subject.''')

form_recherche = st.form("Recherche form")
texte_a_chercher = form_recherche.text_input("What do you want")
recherche = form_recherche.form_submit_button("Rechercher")

if not recherche:
    bdd.lecture_data(db, "Indicateur")

if recherche:
    docs = db.collection(u'Indicateur').where(u'Name', u'==', texte_a_chercher).stream()

    for doc in docs:
        bdd.presentation_indicateur(doc.to_dict())

    if(texte_a_chercher == ""):
        bdd.lecture_data(db, "Indicateur")