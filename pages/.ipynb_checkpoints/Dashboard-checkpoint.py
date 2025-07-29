import streamlit as st
import streamlit.components.v1 as components
from utils import show_header, show_footer

# Configuração de layout
st.set_page_config(layout="wide", page_title="Dashboard de Resíduos")

# CSS para remover barra lateral e otimizar mobile
st.markdown("""
    <style>
        section[data-testid="stSidebar"] { display: none !important; }
        .stApp { padding: 0 !important; }
        iframe { border: none; }
        
        /* Container responsivo */
        .responsive-container {
            position: relative;
            overflow: hidden;
            padding-top: 56.25%; /* Proporção 16:9 */
        }
        
        .responsive-iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        
        @media (max-width: 768px) {
            .responsive-container {
                padding-top: 100vh; /* Ocupa toda altura */
            }
        }
    </style>
""", unsafe_allow_html=True)

# Mostra cabeçalho
show_header(show_calculadora=False)

# URL do Power BI com parâmetros para forçar versão interativa
powerbi_link = "https://app.powerbi.com/view?r=eyJrIjoiYTE0NTliNjQtMTYzMC00MDZmLTgyODgtMTE5Y2UwOTc2MjQ2IiwidCI6ImU5YTgyZWM3LTRhODYtNDNkZS1hYjJhLTcxOWQ2Njk1OWExYiJ9"

# Adicione estes parâmetros essenciais:
powerbi_link += "&rs:embed=true"  # Força modo embed
powerbi_link += "&rs:command=Render"  # Força renderização completa
powerbi_link += "&rs:device=desktop"  # Força versão desktop

# Container responsivo
st.markdown(
    f"""
    <div class="responsive-container">
        <iframe class="responsive-iframe" 
                src="{powerbi_link}" 
                allowFullScreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# Rodapé
show_footer()