import streamlit as st
import pandas as pd
import numpy as np

def autenticar():
    usuarios = {"ligyadmin": "2707"}  # simples para demo
    with st.sidebar:
        st.title("🔐 Login")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        login = st.button("Entrar")

    if login:
        if usuario in usuarios and usuarios[usuario] == senha:
            st.session_state["logado"] = True
        else:
            st.error("Usuário ou senha inválidos.")

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    autenticar()
    st.stop()

st.title("📊 Projeto Faturamento Ligy")
uploaded_file = st.file_uploader("Selecione o arquivo .xlsx", type=["xlsx"])

if uploaded_file:
    df_temp = pd.read_excel(uploaded_file, sheet_name="temp", header=0)
    st.write("Pré-visualização dos dados da aba temp:")
    st.dataframe(df_temp.head())
