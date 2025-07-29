# app.py
import streamlit as st
from utils import show_header, show_footer
from device_detection import is_mobile

# Configuração responsiva
st.set_page_config(
    layout="wide",
    page_title="Calculadora de Impacto Ambiental",
    initial_sidebar_state="collapsed"
)

# CSS para dispositivos móveis
st.markdown("""
    <style>
        /* Remover barra lateral */
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        
        /* Ajustes para mobile */
        @media (max-width: 768px) {
            .stApp {
                padding: 5px !important;
            }
            
            .stNumberInput input {
                font-size: 16px !important;
                padding: 12px !important;
            }
            
            .stButton button {
                font-size: 16px !important;
                padding: 12px !important;
            }
            
            /* Ajuste de containers */
            .stContainer {
                padding: 5px !important;
            }
            
            /* Textos maiores */
            .stMarkdown p, .stMarkdown li {
                font-size: 16px !important;
                line-height: 1.6 !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Mostra cabeçalho
show_header(show_calculadora=True)

# ... (restante do código da calculadora permanece igual) ...

# Rodapé
show_footer()