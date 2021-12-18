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
        title = post["title"]
        url = post["url"]

        st.subheader(f"{title}")
        st.write(f":link: [{url}]({url})")

def ecriture_data(db, title, url):

    doc_ref = db.collection("posts").document(title)
    doc_ref.set({
        "title": title,
        "url": url
    })
