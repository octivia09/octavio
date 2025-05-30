import streamlit as st
import csv
import os
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Formulário de Cadastro", page_icon="📝", layout="centered")
st.title("📋 Formulário de Cadastro")

st.markdown("Preencha os dados abaixo e clique em **ENVIAR** para salvar suas informações em CSV.")

# Caminho do arquivo CSV
csv_file = "registros_usuarios.csv"

# Cabeçalho do CSV (caso ainda não exista)
if not os.path.isfile(csv_file):
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Data", "Nome", "Idade", "Time"])

# Formulário
with st.form("formulario_usuario"):
    nome = st.text_input("Nome completo")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1)
    times = ["Flamengo", "Corinthians", "Palmeiras", "Outro"]
    time_futebol = st.selectbox("Time de Futebol", options=times)

    enviado = st.form_submit_button("ENVIAR")

    if enviado:
        if nome.strip() == "":
            st.warning("⚠️ Por favor, preencha seu nome.")
        else:
            data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nova_linha = [data_atual, nome, idade, time_futebol]

            with open(csv_file, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(nova_linha)

            st.success("✅ Dados salvos com sucesso no arquivo CSV!")
