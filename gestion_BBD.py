import streamlit as st
from google.oauth2 import service_account
from google.cloud import firestore
import json

def connexion(secret, project_name):

    key_dict = json.loads(secret)
    creds = service_account.Credentials.from_service_account_info(key_dict)
    return firestore.Client(credentials=creds, project=project_name)

def lecture_data(db, collection_name):

    posts_ref = db.collection(collection_name)
    for doc in posts_ref.stream():
        post = doc.to_dict()
        presentation_indicateur(post)

def presentation_indicateur(post):
    c = st.container()
    c.markdown('## ' + post["Name"])
    col1, col2 = c.columns(2)
    col1.markdown("<strong>Etude associé : </strong>" + post["Associated Study"], unsafe_allow_html=True)
    col1.markdown("<strong>Source : </strong>" + post["Source"], unsafe_allow_html=True)
    col2.markdown("<strong>Remark or issues aborded : </strong>" + post["Issues"], unsafe_allow_html=True)
    col2.markdown("<strong>Contact : </strong>" + post["Contact"], unsafe_allow_html=True)
    if(post["Video"]):
        c.empty()
        c.write("To have more information about this indicator you can see the following video :")
        c.video(post["Explicative Source"])
    else:
        c.empty()
        c.write("To have more information about this indicator you can see the following source :")
        c.write(post["Explicative Source"])


def ecriture_data(db, collection_name, dico_form):

    doc_ref = db.collection(collection_name).document(dico_form['Name'])
    doc_ref.set(dico_form)