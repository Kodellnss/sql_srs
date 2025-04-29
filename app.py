import streamlit as st
import pandas as pd
import duckdb

st.write("""
#SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review ?",
    ("Join","GroupBy","Windows Functions"),
    index=None,
    placeholder = "Select contact method...",
)

st.write('You selected :', option)


data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(['Cat', "Dog","Owl"])

with tab1:
        sql_query = st.text_area(label = "entrez votre input")
        if sql_query.strip():
            try:
                result = duckdb.query(sql_query).df()
                st.write(f"Vous avez entré la requête suivante : {sql_query}")
                st.dataframe(result)
            except Exception as e:
                st.error(f"Erreur lors de l'exécution de la requête : {e}")
        else:
            st.info("Veuillez entrer une requête SQL pour voir les résultats.")




with tab2 :
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3 :
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg",  width=200)