import streamlit as st
import streamlit.components.v1 as components
from utils import show_header, show_footer

# Configuração de layout amplo
st.set_page_config(
    layout="wide",
    page_title="Dashboard de Impacto Ambiental",
    initial_sidebar_state="collapsed"
)

# === CSS CORRIGIDO ===
st.markdown("""
    <style>
        /* Remover completamente a barra lateral */
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Espaçamento apenas no topo para o cabeçalho */
        .stApp {
            padding-top: 0 !important;
        }
        
        /* Container principal com espaço para o cabeçalho */
        .block-container {
            padding: 0 !important;
            max-width: 100vw !important;
        }
        
        /* Cabeçalho com altura automática */
        header {
            max-width: 100vw !important;
            padding: 0 !important;
            height: auto !important;
            position: relative !important;
        }
        
        /* Iframe do PowerBI ocupando a altura restante */
        .iframe-container {
            height: calc(100vh - 120px); /* Espaço para cabeçalho/rodapé */
            width: 100vw;
            padding: 0;
            margin: 0;
        }
        
        /* Iframe interno */
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        
        /* Rodapé fixo na parte inferior */
        footer {
            position: relative;
            bottom: 0;
            width: 100%;
            padding: 10px 0 !important;
            background: white;
            z-index: 100;
        }
    </style>
""", unsafe_allow_html=True)

# Mostra cabeçalho personalizado
show_header(show_calculadora=False)

# Container para o iframe do PowerBI
powerbi_link = "https://app.powerbi.com/view?r=eyJrIjoiYTE0NTliNjQtMTYzMC00MDZmLTgyODgtMTE5Y2UwOTc2MjQ2IiwidCI6ImU5YTgyZWM3LTRhODYtNDNkZS1hYjJhLTcxOWQ2Njk1OWExYiJ9"

st.markdown(
    f"""
    <div class="iframe-container">
        <iframe title="PowerBI" src="{powerbi_link}" frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# Rodapé
show_footer()
