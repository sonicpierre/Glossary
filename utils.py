import streamlit as st

def construction_form_sidebar():
    st.sidebar.image('image/michelin_logo.png')

    form = st.sidebar.form("Input form")
    form.text_input("Indicator")
    form.text_input("Name associated study")
    form.text_input("Azure Data Lake source")
    form.text_input("Contact mail")
    form.text_input('Explicative source')
    form.checkbox('Explicative video')
    form.radio("Fréquence",('Daily', 'Monthly', 'Annualy'))
    form.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    return form.form_submit_button("Ajouter")
