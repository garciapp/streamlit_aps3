import streamlit as st
import requests

# URL Render
API_URL = "https://aps-3-flask-rest-mongo-garciapp.onrender.com"

# Configurações da página
st.set_page_config(page_title="Aluguel de Bicicletas", layout="wide")

# Barra lateral de navegação (Usuários / Bicicletas / Empréstimos)
st.sidebar.title("Aluguel de Bicicletas")
categoria = st.sidebar.selectbox("Selecione uma Categoria", ["Usuários", "Bicicletas", "Empréstimos"])

# ----------------- Usuários -----------------

if categoria == "Usuários":
    st.title("Gerenciamento de Usuários")
    
    # Sub-navegação para Operações de Usuários
    operacao_usuario = st.selectbox("Selecione uma Operação", ["Visualizar", "Adicionar", "Atualizar", "Deletar"])
    
    if operacao_usuario == "Visualizar":
        st.subheader("Lista de Usuários")
        response = requests.get(f"{API_URL}/usuarios")
        if response.status_code == 200:
            usuarios = response.json()
            if usuarios:
                for usuario in usuarios:
                    st.markdown(f"**ID:** {usuario['_id']}")
                    st.markdown(f"**Nome:** {usuario['nome']}")
                    st.markdown(f"**CPF:** {usuario['cpf']}")
                    st.markdown(f"**Data de Nascimento:** {usuario['data_nascimento']}")
                    st.markdown("---")
            else:
                st.info("Nenhum usuário encontrado.")
        else:
            st.error("Não foi possível carregar os usuários.")

    elif operacao_usuario == "Adicionar":
        st.subheader("Adicionar Novo Usuário")
        with st.form(key="inserir_usuario"):
            nome = st.text_input("Nome")
            cpf = st.text_input("CPF")
            data_nascimento = st.text_input("Data de Nascimento (DD/MM/AAAA)")
            submit_button = st.form_submit_button("Adicionar")
            
        if submit_button:
            if nome and cpf and data_nascimento:
                novo_usuario = {
                    "nome": nome,
                    "cpf": cpf,
                    "data_nascimento": data_nascimento
                }
                response = requests.post(f"{API_URL}/usuarios", json=novo_usuario)
                if response.status_code == 201:
                    st.success("Usuário adicionado com sucesso!")
                else:
                    erro = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Falha ao adicionar usuário: {erro}")
            else:
                st.warning("Por favor, preencha todos os campos.")

    elif operacao_usuario == "Atualizar":
        st.subheader("Atualizar Usuário")
        with st.form(key="atualizar_usuario_form"):
            usuario_id = st.text_input("ID do Usuário a ser atualizado", key="usuario_id_atualizar")
            nome = st.text_input("Novo Nome")
            cpf = st.text_input("Novo CPF")
            data_nascimento = st.text_input("Nova Data de Nascimento (DD/MM/AAAA)")
            submit_button = st.form_submit_button("Atualizar")
            
        if submit_button:
            if usuario_id and (nome or cpf or data_nascimento):
                usuario_atualizado = {}
                if nome:
                    usuario_atualizado["nome"] = nome
                if cpf:
                    usuario_atualizado["cpf"] = cpf
                if data_nascimento:
                    usuario_atualizado["data_nascimento"] = data_nascimento
                
                response = requests.put(f"{API_URL}/usuarios/{usuario_id}", json=usuario_atualizado)
                if response.status_code == 200:
                    st.success("Usuário atualizado com sucesso!")
                else:
                    erro = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Falha ao atualizar usuário: {erro}")
            else:
                st.warning("Por favor, preencha o ID do usuário e pelo menos um campo para atualização.")

    elif operacao_usuario == "Deletar":
        st.subheader("Deletar Usuário")
        with st.form(key="deletar_usuario_form"):
            usuario_id_deletar = st.text_input("ID do Usuário a ser deletado", key="usuario_id_deletar")
            submit_button = st.form_submit_button("Deletar")
            
        if submit_button:
            if usuario_id_deletar:
                confirmacao = st.warning("Tem certeza que deseja deletar este usuário?", icon="⚠️")
                confirmar = st.button("Confirmar Deleção")
                if confirmar:
                    response = requests.delete(f"{API_URL}/usuarios/{usuario_id_deletar}")
                    if response.status_code == 200:
                        st.success("Usuário deletado com sucesso!")
                    else:
                        erro = response.json().get('erro', 'Erro desconhecido.')
                        st.error(f"Falha ao deletar usuário: {erro}")
            else:
                st.warning("Por favor, insira o ID do usuário a ser deletado.")

# ----------------- Bicicletas -----------------

elif categoria == "Bicicletas":
    st.title("Gerenciamento de Bicicletas")
    
    # Sub-navegação para Operações de Bicicletas
    operacao_bicicleta = st.selectbox("Selecione uma Operação", ["Visualizar", "Adicionar", "Atualizar", "Deletar"])
    
    if operacao_bicicleta == "Visualizar":
        st.subheader("Lista de Bicicletas")
        response = requests.get(f"{API_URL}/bikes")
        if response.status_code == 200:
            bikes = response.json()
            if bikes:
                for bike in bikes:
                    st.markdown(f"**ID:** {bike['_id']}")
                    st.markdown(f"**Marca:** {bike['marca']}")
                    st.markdown(f"**Modelo:** {bike['modelo']}")
                    st.markdown(f"**Cidade:** {bike['cidade']}")
                    st.markdown(f"**Status:** {bike['status']}")
                    st.markdown("---")
            else:
                st.info("Nenhuma bicicleta encontrada.")
        else:
            st.error("Não foi possível carregar as bicicletas.")

    elif operacao_bicicleta == "Adicionar":
        st.subheader("Adicionar Nova Bicicleta")
        with st.form(key="inserir_bike_form"):
            marca = st.text_input("Marca")
            modelo = st.text_input("Modelo")
            cidade = st.text_input("Cidade")
            status = st.selectbox("Status", ["disponivel", "em uso"])
            submit_button = st.form_submit_button("Adicionar")
            
        if submit_button:
            if marca and modelo and cidade and status:
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
                    erro = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Falha ao adicionar bicicleta: {erro}")
            else:
                st.warning("Por favor, preencha todos os campos.")

    elif operacao_bicicleta == "Atualizar":
        st.subheader("Atualizar Bicicleta")
        with st.form(key="atualizar_bike_form"):
            bike_id = st.text_input("ID da Bicicleta a ser atualizada", key="bike_id_atualizar")
            marca = st.text_input("Nova Marca")
            modelo = st.text_input("Novo Modelo")
            cidade = st.text_input("Nova Cidade")
            status = st.selectbox("Novo Status", ["disponivel", "em uso"], key="novo_status_bike")
            submit_button = st.form_submit_button("Atualizar")
            
        if submit_button:
            if bike_id and (marca or modelo or cidade or status):
                bike_atualizada = {}
                if marca:
                    bike_atualizada["marca"] = marca
                if modelo:
                    bike_atualizada["modelo"] = modelo
                if cidade:
                    bike_atualizada["cidade"] = cidade
                if status:
                    bike_atualizada["status"] = status
                
                response = requests.put(f"{API_URL}/bikes/{bike_id}", json=bike_atualizada)
                if response.status_code == 200:
                    st.success("Bicicleta atualizada com sucesso!")
                else:
                    erro = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Falha ao atualizar bicicleta: {erro}")
            else:
                st.warning("Por favor, insira o ID da bicicleta e pelo menos um campo para atualização.")

    elif operacao_bicicleta == "Deletar":
        st.subheader("Deletar Bicicleta")
        with st.form(key="deletar_bike_form"):
            bike_id_deletar = st.text_input("ID da Bicicleta a ser deletada", key="bike_id_deletar")
            submit_button = st.form_submit_button("Deletar")
            
        if submit_button:
            if bike_id_deletar:
                confirmacao = st.warning("Tem certeza que deseja deletar esta bicicleta?", icon="⚠️")
                confirmar = st.button("Confirmar Deleção")
                if confirmar:
                    response = requests.delete(f"{API_URL}/bikes/{bike_id_deletar}")
                    if response.status_code == 200:
                        st.success("Bicicleta deletada com sucesso!")
                    else:
                        erro = response.json().get('erro', 'Erro desconhecido.')
                        st.error(f"Falha ao deletar bicicleta: {erro}")
            else:
                st.warning("Por favor, insira o ID da bicicleta a ser deletada.")

# ----------------- Empréstimos -----------------

elif categoria == "Empréstimos":
    st.title("Gerenciamento de Empréstimos")
    
    # Sub-navegação para Operações de Empréstimos
    operacao_emprestimo = st.selectbox("Selecione uma Operação", ["Visualizar", "Registrar", "Encerrar"])
    
    if operacao_emprestimo == "Visualizar":
        st.subheader("Lista de Empréstimos")
        response = requests.get(f"{API_URL}/emprestimos")
        if response.status_code == 200:
            emprestimos = response.json()
            if emprestimos:
                for emprestimo in emprestimos:
                    st.markdown(f"**ID Empréstimo:** {emprestimo['_id']}")
                    st.markdown(f"**ID Usuário:** {emprestimo['id_usuario']}")
                    st.markdown(f"**ID Bicicleta:** {emprestimo['id_bike']}")
                    st.markdown(f"**Data Empréstimo:** {emprestimo['data_emprestimo']}")
                    st.markdown("---")
            else:
                st.info("Nenhum empréstimo encontrado.")
        else:
            st.error("Não foi possível carregar os empréstimos.")

    elif operacao_emprestimo == "Registrar":
        st.subheader("Registrar Novo Empréstimo")
        with st.form(key="registrar_emprestimo_form"):
            # Obter lista de usuários
            usuarios_response = requests.get(f"{API_URL}/usuarios")
            if usuarios_response.status_code == 200:
                usuarios = usuarios_response.json()
                if usuarios:
                    usuario_options = {f"{u['nome']} (ID: {u['_id']})": u['_id'] for u in usuarios}
                    selected_usuario = st.selectbox("Selecione o Usuário", list(usuario_options.keys()), key="emprestimo_usuario")
                    id_usuario = usuario_options[selected_usuario]
                else:
                    st.warning("Nenhum usuário disponível para empréstimo.")
                    id_usuario = None
            else:
                st.error("Não foi possível carregar os usuários.")
                id_usuario = None

            # Obter lista de bicicletas disponíveis
            bikes_response = requests.get(f"{API_URL}/bikes")
            if bikes_response.status_code == 200:
                bikes = bikes_response.json()
                bikes_disponiveis = [b for b in bikes if b['status'] == 'disponivel']
                if bikes_disponiveis:
                    bike_options = {f"{b['marca']} {b['modelo']} (ID: {b['_id']})": b['_id'] for b in bikes_disponiveis}
                    selected_bike = st.selectbox("Selecione a Bicicleta", list(bike_options.keys()), key="emprestimo_bike")
                    id_bike = bike_options[selected_bike]
                else:
                    st.warning("Nenhuma bicicleta disponível para empréstimo.")
                    id_bike = None
            else:
                st.error("Não foi possível carregar as bicicletas.")
                id_bike = None

            submit_button = st.form_submit_button("Registrar Empréstimo")
            
        if submit_button:
            if id_usuario and id_bike:
                response = requests.post(f"{API_URL}/emprestimos/usuarios/{id_usuario}/bikes/{id_bike}")
                if response.status_code == 201:
                    st.success("Empréstimo registrado com sucesso!")
                else:
                    erro = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Falha ao registrar empréstimo: {erro}")
            else:
                st.warning("Por favor, selecione um usuário e uma bicicleta disponíveis.")

    elif operacao_emprestimo == "Encerrar":
        st.subheader("Encerrar Empréstimo")
        with st.form(key="encerrar_emprestimo_form"):
            # Obter lista de empréstimos ativos
            emprestimos_response = requests.get(f"{API_URL}/emprestimos")
            if emprestimos_response.status_code == 200:
                emprestimos = emprestimos_response.json()
                emprestimos_ativos = emprestimos  # Supondo que todos os empréstimos são ativos
                if emprestimos_ativos:
                    emprestimo_options = {f"Empréstimo ID: {e['_id']} | Usuário ID: {e['id_usuario']} | Bicicleta ID: {e['id_bike']}" : e['_id'] for e in emprestimos_ativos}
                    selected_emprestimo = st.selectbox("Selecione o Empréstimo para Encerrar", list(emprestimo_options.keys()), key="encerrar_emprestimo")
                    emprestimo_id = emprestimo_options[selected_emprestimo]
                else:
                    st.warning("Nenhum empréstimo ativo para encerrar.")
                    emprestimo_id = None
            else:
                st.error("Não foi possível carregar os empréstimos.")
                emprestimo_id = None

            submit_button = st.form_submit_button("Encerrar Empréstimo")
            
        if submit_button:
            if emprestimo_id:
                confirmacao = st.warning("Tem certeza que deseja encerrar este empréstimo?", icon="⚠️")
                confirmar = st.button("Confirmar Encerramento")
                if confirmar:
                    response = requests.delete(f"{API_URL}/emprestimos/{emprestimo_id}")
                    if response.status_code == 200:
                        st.success("Empréstimo encerrado com sucesso!")
                    else:
                        erro = response.json().get('erro', 'Erro desconhecido.')
                        st.error(f"Falha ao encerrar empréstimo: {erro}")
            else:
                st.warning("Por favor, selecione um empréstimo para encerrar.")
