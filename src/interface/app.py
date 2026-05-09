import streamlit as st
import sys
import os

from src.logic.consumo import (
    definir_meta,
    adicionar_consumo,
    calcular_progresso,
    get_meta,
    get_consumo
)

from services.clima import pegar_temperatura
from src.logic.historico import salvar_dia  # ajuste se o nome for diferente

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# SESSION STATE (FIX)
if "meta" not in st.session_state:
    st.session_state.meta = 0

if "consumo" not in st.session_state:
    st.session_state.consumo = 0

# TÍTULO

st.set_page_config(page_title="Lembrete de Água", layout="centered")

st.title("💧 Lembrete de Água Inteligente")

st.divider()


# COLUNAS DA META E DO CONSUMO

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Meta diária")
    meta_input = st.number_input("Meta (ml)", min_value=0, value=2000)

    if st.button("Definir meta"):
        definir_meta(meta_input)
        st.session_state.meta = meta_input
        st.session_state.consumo = 0
        st.success("Meta definida!")

with col2:
    st.subheader("🥤 Consumo")
    quantidade = st.number_input("Quantidade (ml)", min_value=0, value=200)

    if st.button("Adicionar"):
        novo = adicionar_consumo(quantidade)
        st.session_state.consumo = novo
        st.success(f"+{quantidade}ml")

st.divider()

# BARRA DE PROGRESSO

meta = st.session_state.meta
consumo = st.session_state.consumo

st.subheader("📊 Progresso do dia")

if meta > 0:
    progresso = calcular_progresso()

    st.progress(min(int(progresso), 100))

    st.markdown(f"""
    **{consumo}ml / {meta}ml**
    """)

    if progresso == 100:
        st.success("🎉 Meta atingida! Parabéns!")
    else:
        st.success("Uau você ultrapassou a meta, parabéns!!")
else:
    st.info("Defina uma meta para começar")

st.divider()


# CLIMA

st.subheader("🌡️ Clima")

if st.button("Ver clima"):
    st.info("⏳ API ainda não ativada (em breve...)")

st.divider()

# HISTÓRICO

st.subheader("💾 Histórico")

if st.button("Salvar dia"):
    salvar_dia(consumo, meta)
    st.success("Dia salvo!")
