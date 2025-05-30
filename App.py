import streamlit as st
from datetime import datetime

# Título da aplicação
st.set_page_config(page_title="Formulário de Cadastro", page_icon="📝", layout="centered")
st.title("📋 Formulário de Cadastro")

st.markdown("Preencha os dados abaixo e clique em **ENVIAR** para salvar suas informações.")

# Formulário com UX amigável
with st.form("formulario_usuario"):
    nome = st.text_input("Nome completo")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    
    times = ["Flamengo", "Corinthians", "Palmeiras", "Outro"]
    time_futebol = st.selectbox("Time de Futebol", options=times)

    # Botão de envio
    enviado = st.form_submit_button("ENVIAR")

    if enviado:
        if nome.strip() == "":
            st.warning("⚠️ Por favor, preencha seu nome.")
        else:
            # Formata os dados
            data = f"""
==== Novo Registro ====
Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Nome: {nome}
Idade: {idade}
Time: {time_futebol}
=========================
"""
            # Salva os dados em um arquivo texto
            with open("registros_usuarios.txt", "a", encoding="utf-8") as f:
                f.write(data)

            st.success("✅ Informações salvas com sucesso!")
