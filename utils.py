import streamlit as st

def construction_form_sidebar():
    
    dico_entrees = {}

    st.sidebar.image('image/michelin_logo.png')
    form = st.sidebar.form("Input form")
    dico_entrees["Name"] = form.text_input("Indicator")
    dico_entrees["Associated Study"] = form.text_input("Name associated study")
    dico_entrees["Issues"] = form.text_area("Issues answered or remark")
    dico_entrees["Source"] = form.text_input("Source")
    dico_entrees["Contact"] = form.text_input("Contact mail")
    dico_entrees["Explicative Source"] = form.text_input('Explicative source')
    dico_entrees["Video"] = form.checkbox('Explicative video ?')
    dico_entrees["Frequence"] = form.radio("Fréquence",('Daily', 'Monthly', 'Annualy'))
    form.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    return form.form_submit_button("Ajouter"), dico_entrees
