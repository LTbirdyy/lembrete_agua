import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.logic.consumo import (
    definir_meta,
    adicionar_consumo,
    calcular_progresso,
)

from services.clima import pegar_clima
from src.logic.historico import salvar_dia  # ajuste se o nome for diferente


# CSS para ficar bonito
st.markdown("""
<style>
.main-card {
    background: #f8f9fa;
    padding: 40px;
    border-radius: 25px;
    max-width: 1100px;
    margin: auto;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

/* texto escuro dentro */
.main-card h1,
.main-card h2,
.main-card h3,
.main-card p,
.main-card label {
    color: #111 !important;
}

/* inputs */
.main-card input {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""

<style>
.card {
    background: linear-gradient(145deg, #1c1f26, #111318);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}

.metric-card {
    background: #151922;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}

.alert-card {
    background: linear-gradient(90deg, #3a1f0f, #5c2d0c);
    padding: 15px;
    border-radius: 15px;
    color: #ffb74d;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# SESSION STATE (FIX)
if "meta" not in st.session_state:
    st.session_state.meta = 2000

if "consumo" not in st.session_state:
    st.session_state.consumo = 0

# TÍTULO

st.set_page_config(page_title="Lembrete de Água", layout="centered")

st.title("💧 Lembrete de Água Inteligente")

st.markdown('<div class="card">', unsafe_allow_html=True)


# COLUNAS DA META E DO CONSUMO

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Meta diária")
    meta_input = st.number_input("Meta (ml)", min_value=1, value=2000)

    if st.button("Definir meta"):
        definir_meta(meta_input)
        st.session_state.meta = meta_input
        st.session_state.consumo = 0
        st.success("Meta definida!")

with col2:
    st.subheader("🥤 Consumo")
    quantidade = st.number_input("Quantidade (ml)", min_value=1, value=200)

    if st.button("Adicionar"):
        novo = adicionar_consumo(quantidade)
        st.session_state.consumo = novo
        st.success(f"+{quantidade}ml")


# BARRA DE PROGRESSO

meta = st.session_state.meta
consumo = st.session_state.consumo
progresso = float(calcular_progresso() if meta > 0 else 0)

# cor dinâmica
if progresso < 50:
    cor = "#FF4B4B"
elif progresso < 100:
    cor = "#FFA500"
else:
    cor = "#00C853"

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 Progresso do dia")

st.markdown(f"""
<div style="background-color:#333; border-radius:10px;">
    <div style="
        width:{max(min(progresso, 100), 5)}%;
        background-color:{cor};
        padding:10px;
        border-radius:10px;
        text-align:center;
        color:white;
        white-space: nowrap;
        font-weight:bold;">
        {progresso:.1f}%
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"**{consumo}ml / {meta}ml**")

if progresso == 100:
    st.markdown("""
    <div style="background: linear-gradient(90deg,#0f3d22,#1b5e20);
    padding:15px; border-radius:15px; color:#00e676;">
    💧️ Parabéns você bateu a meta!!
    </div>
    """, unsafe_allow_html=True)

if 0 < progresso > 100:
    st.markdown("""
    <div style="background: linear-gradient(90deg,#0f3d22,#1b5e20);
    padding:15px; border-radius:15px; color:#00e676;">
    ✔️ Uau você ultrapassou a meta, parabéns!!
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# CLIMA
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### 🌤️ Clima atual")

if st.button("Atualizar clima"):
    clima = pegar_clima()

    if clima is None:
        st.error("Erro ao buscar clima")
    else:

        col1, col2, col3, col4 = st.columns(4)

        col1.markdown(f'<div class="metric-card">🌡️<br>Temperatura<br><b>{clima["temp"]}°C</b></div>',
                      unsafe_allow_html=True)
        col2.markdown(f'<div class="metric-card">💧<br>Umidade<br><b>{clima["umidade"]}%</b></div>',
                      unsafe_allow_html=True)
        col3.markdown(f'<div class="metric-card">🏠<br>Cidade<br><b>{clima["cidade"]} </b></div>',
                      unsafe_allow_html=True)
        col4.markdown(f'<div class="metric-card">☁️<br>Condição<br><b>{clima["descricao"]}</b></div>',
                      unsafe_allow_html=True)

        # REGRA DE HIDRATAÇÃO

        if clima["temp"] >= 30 or clima["umidade"] <= 40:
            st.markdown("""
            <div class="alert-card">
            ⚠️ Umidade muito baixa! O ar está seco, beba mais água.
            </div>
            """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

# HISTÓRICO

if st.button("💾 Salvar dia"):
    salvar_dia(consumo, meta)
    st.success("Dados salvos!")
