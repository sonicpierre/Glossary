import streamlit as st

def construction_form_sidebar():
    
    dico_entrees = {}

    st.sidebar.image('image/michelin_logo.png')
    form = st.sidebar.form("Input form", clear_on_submit=True)
    dico_entrees["Name"] = form.text_input("Indicator")
    dico_entrees["Associated Study"] = form.text_input("Name associated study")
    dico_entrees["Issues"] = form.text_area("Issues answered or remark")
    dico_entrees["Source"] = form.text_input("Source")
    dico_entrees["Contact"] = form.text_input("Contact mail")
    dico_entrees["Explicative Source"] = form.text_input('Explicative source')
    dico_entrees["Video"] = form.checkbox('Explicative video')
    dico_entrees["Frequence"] = form.radio("Fréquence",('Daily', 'Monthly', 'Annualy'))
    form.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    return form.form_submit_button("Add"), dico_entrees


def construction_formulaire_modif(post):
    form = st.form("Modifier " + post['Name'], clear_on_submit=True)
    dico_entrees = {}

    col1, col2 = form.columns(2)
    dico_entrees["Name"] = col1.text_input("Indicator")
    dico_entrees["Associated Study"] = col2.text_input("Name associated study")
    dico_entrees["Issues"] = form.text_area("Issues answered or remark")

    col3, col4 = form.columns(2)
    dico_entrees["Source"] = col3.text_input("Source")
    dico_entrees["Contact"] = col4.text_input("Contact mail")
    dico_entrees["Explicative Source"] = form.text_input('Explicative source')
    dico_entrees["Video"] = form.checkbox('Explicative video')
    dico_entrees["Frequence"] = form.radio("Fréquence",('Daily', 'Monthly', 'Annualy'))
    form.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    return form.form_submit_button("Modify"), dico_entrees