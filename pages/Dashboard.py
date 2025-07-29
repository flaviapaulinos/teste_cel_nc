import streamlit as st
import streamlit.components.v1 as components
from utils import show_header, show_footer

# Configuração de layout amplo
st.set_page_config(
    layout="wide",
    page_title="Dashboard de Impacto Ambiental",
    initial_sidebar_state="collapsed"
)

# === CSS para ocupar máximo espaço ===
st.markdown("""
    <style>
        /* Remover completamente a barra lateral */
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Remover espaçamentos padrão */
        .block-container {
            padding: 0 !important;
            max-width: 100vw !important;
        }
        
        /* Remover margens do cabeçalho */
        header {
            max-width: 100vw !important;
            left: 0 !important;
            right: 0 !important;
            padding: 0 !important;
        }
        
        /* Remover margens do rodapé */
        footer {
            max-width: 100vw !important;
            padding: 0 !important;
        }
        
        /* Container principal sem espaçamentos */
        .stApp {
            max-width: 100vw !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Iframe do PowerBI ocupando toda a altura visível */
        .iframe-container {
            height: calc(100vh - 70px); /* Considera altura do cabeçalho */
            width: 100vw;
            padding: 0;
            margin: 0;
            overflow: hidden;
        }
        
        /* Iframe interno - 100% do container */
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        
        /* Ajustes para dispositivos móveis */
        @media (max-width: 768px) {
            .iframe-container {
                height: calc(100vh - 50px);
            }
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
