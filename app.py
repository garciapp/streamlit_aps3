import streamlit as st
import requests

# URL Render
API_URL = "https://aps-3-flask-rest-mongo-garciapp.onrender.com"

# Barra lateral de navegação (Usuários / Bicicletas / Empréstimos)
st.sidebar.title("Aluguel de Bicicletas")
opcao = st.sidebar.selectbox("Selecione uma opção", ["Usuários", "Bicicletas", "Empréstimos"])


# ----------------- Usuários -----------------

# Visualizar Usuários
if opcao == "Usuários":
    st.title("Gerenciamento de Usuários")
    st.subheader("Lista de Usuários")
    
    response = requests.get(f"{API_URL}/usuarios")
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            st.write(f"ID: {usuario['_id']}")
            st.write(f"Nome: {usuario['nome']}")
            st.write(f"CPF: {usuario['cpf']}")
            st.write(f"Data de Nascimento: {usuario['data_nascimento']}")
            st.write("---")
    else:
        st.error("Não foi possível carregar os usuários.")

