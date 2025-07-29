import streamlit as st
from utils import show_header, show_footer
from dashboard_component import powerbi_dashboard  # Importe a função do novo arquivo
# Configuração de layout
st.set_page_config(layout="wide", page_title="Dashboard de Resíduos")
# CSS para remover barra lateral e otimizar mobile
st.markdown("""
    <style>
        section[data-testid="stSidebar"] { display: none !important; }
        .stApp { padding: 0 !important; }
    </style>
""", unsafe_allow_html=True)
# Mostra cabeçalho
show_header(show_calculadora=False)
# URL do Power BI
powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiYTE0NTliNjQtMTYzMC00MDZmLTgyODgtMTE5Y2UwOTc2MjQ2IiwidCI6ImU5YTgyZWM3LTRhODYtNDNkZS1hYjJhLTcxOWQ2Njk1OWExYiJ9"
# Chama o componente personalizado
powerbi_dashboard(powerbi_url)
# Rodapé
show_footer()
