import streamlit as st
import requests

# URL Render
API_URL = "https://aps-3-flask-rest-mongo-garciapp.onrender.com"

# Barra lateral de navegação (Usuários / Bicicletas / Empréstimos)
st.sidebar.title("Aluguel de Bicicletas")
opcao = st.sidebar.selectbox("Selecione uma opção", ["Usuários", "Bicicletas", "Empréstimos"])


# ----------------- Usuários -----------------

if opcao == "Usuários":
    st.title("Gerenciamento de Usuários")

    # Visualizar Usuários
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
    
    # Adicionar novo usuário
    st.subheader("Adicionar Novo Usuário")
    with st.form(key="inserir_usuario"):
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        data_nascimento = st.text_input("Data de Nascimento (DD/MM/AAAA)")
        submit_button = st.form_submit_button("Adicionar")
        
    if submit_button:
        novo_usuario = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento
        }
        response = requests.post(f"{API_URL}/usuarios", json=novo_usuario)
        if response.status_code == 201:
            st.success("Usuário adicionado com sucesso!")
        else:
            st.error("Falha ao adicionar usuário.")

    # Atualizar usuário
    st.subheader("Atualizar Usuário")
    usuario_id = st.text_input("ID do Usuário a ser atualizado")
    with st.form(key="atualizar_usuario"):
        nome = st.text_input("Novo Nome")
        cpf = st.text_input("Novo CPF")
        data_nascimento = st.text_input("Nova Data de Nascimento (DD/MM/AAAA)")
        submit_button = st.form_submit_button("Atualizar")
        
    if submit_button:
        usuario_atualizado = {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento
        }
        response = requests.put(f"{API_URL}/usuarios/{usuario_id}", json=usuario_atualizado)
        if response.status_code == 200:
            st.success("Usuário atualizado com sucesso!")
        else:
            st.error("Falha ao atualizar usuário.")

    # Deletar usuário
    st.subheader("Deletar Usuário")
    usuario_id = st.text_input("ID do Usuário a ser deletado")
    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/usuarios/{usuario_id}")
        if response.status_code == 200:
            st.success("Usuário deletado com sucesso!")
        else:
            st.error("Falha ao deletar usuário.")


# ----------------- Bicicletas -----------------

elif opcao == "Bicicletas":
    st.title("Gerenciamento de Bicicletas")

    # Visualizar Bicicletas
    st.subheader("Lista de Bicicletas")
    response = requests.get(f"{API_URL}/bikes")
    if response.status_code == 200:
        bikes = response.json()
        for bike in bikes:
            st.write(f"**ID:** {bike['_id']}")
            st.write(f"**Marca:** {bike['marca']}")
            st.write(f"**Modelo:** {bike['modelo']}")
            st.write(f"**Cidade:** {bike['cidade']}")
            st.write(f"**Status:** {bike['status']}")
            st.write("---")
    else:
        st.error("Não foi possível carregar as bicicletas.")

    # Adicionar nova bicicleta
    st.subheader("Adicionar Nova Bicicleta")
    with st.form(key="inserir_bike"):
        marca = st.text_input("Marca")
        modelo = st.text_input("Modelo")
        cidade = st.text_input("Cidade")
        status = st.selectbox("Status", ["disponivel", "em uso"])
        submit_button = st.form_submit_button("Adicionar")

    if submit_button:
        nova_bike = {
            "marca": marca,
            "modelo": modelo,
            "cidade": cidade,
            "status": status
        }
        response = requests.post(f"{API_URL}/bikes", json=nova_bike)
        if response.status_code == 201:
            st.success("Bicicleta adicionada com sucesso!")
        else:
            st.error(f"Falha ao adicionar bicicleta: {response.json().get('erro', 'Erro desconhecido')}")

    # Atualizar bicicleta
    st.subheader("Atualizar Bicicleta")
    bike_id = st.text_input("ID da Bicicleta a ser atualizada", key="atualizar_bike_id")
    with st.form(key="atualizar_bike_form"):
        marca = st.text_input("Nova Marca")
        modelo = st.text_input("Novo Modelo")
        cidade = st.text_input("Nova Cidade")
        status = st.selectbox("Novo Status", ["disponivel", "em uso"], key="novo_status")
        submit_button = st.form_submit_button("Atualizar")

    if submit_button:
        bike_atualizada = {
            "marca": marca,
            "modelo": modelo,
            "cidade": cidade,
            "status": status
        }
        response = requests.put(f"{API_URL}/bikes/{bike_id}", json=bike_atualizada)
        if response.status_code == 200:
            st.success("Bicicleta atualizada com sucesso!")
        else:
            st.error(f"Falha ao atualizar bicicleta: {response.json().get('erro', 'Erro desconhecido')}")

    # Deletar bicicleta
    st.subheader("Deletar Bicicleta")
    bike_id_deletar = st.text_input("ID da Bicicleta a ser deletada", key="deletar_bike_id")
    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/bikes/{bike_id_deletar}")
        if response.status_code == 200:
            st.success("Bicicleta deletada com sucesso!")
        else:
            st.error(f"Falha ao deletar bicicleta: {response.json().get('erro', 'Erro desconhecido')}")


# ----------------- Empréstimos -----------------

elif opcao == "Empréstimos":

    # Visualizar empréstimos
    st.title("Gerenciamento de Empréstimos")
    st.subheader("Lista de Empréstimos")
    response = requests.get(f"{API_URL}/emprestimos")
    if response.status_code == 200:
        emprestimos = response.json()
        for emprestimo in emprestimos:
            st.write(f"ID Empréstimo: {emprestimo['_id']}")
            st.write(f"ID Usuário: {emprestimo['id_usuario']}")
            st.write(f"ID Bicicleta: {emprestimo['id_bike']}")
            st.write(f"Data Empréstimo: {emprestimo['data_emprestimo']}")
            st.write("---")
    else:
        st.error("Não foi possível carregar os empréstimos.")

    # Registrar novo empréstimo
    st.subheader("Registrar Novo Empréstimo")
    with st.form(key="registrar_emprestimo"):
        id_usuario = st.text_input("ID do Usuário")
        id_bike = st.text_input("ID da Bicicleta")
        submit_button = st.form_submit_button("Registrar Empréstimo")
        
    if submit_button:
        response = requests.post(f"{API_URL}/emprestimos/usuarios/{id_usuario}/bikes/{id_bike}")
        if response.status_code == 201:
            st.success("Empréstimo registrado com sucesso!")
        else:
            st.error("Falha ao registrar empréstimo.")

    # Encerrar empréstimo (Devolução)
    st.subheader("Encerrar Empréstimo")
    emprestimo_id = st.text_input("ID do Empréstimo a ser encerrado")
    if st.button("Encerrar Empréstimo"):
        response = requests.delete(f"{API_URL}/emprestimos/{emprestimo_id}")
        if response.status_code == 200:
            st.success("Empréstimo encerrado com sucesso!")
        else:
            st.error("Falha ao encerrar empréstimo.")


