import streamlit as st
from utils import show_header, show_footer, is_mobile, capture_js_messages

# 1. Captura mensagens do JavaScript primeiro
capture_js_messages()

# 2. Configuração de layout
st.set_page_config(
    layout="wide", 
    page_title="Dashboard de Resíduos",
    initial_sidebar_state="collapsed"
)

# 3. Detecta se é dispositivo móvel
is_mobile_device = is_mobile()

# 4. Mostra cabeçalho
show_header(show_calculadora=False)

# URL do Power BI
powerbi_link = "https://app.powerbi.com/view?r=eyJrIjoiYTE0NTliNjQtMTYzMC00MDZmLTgyODgtMTE5Y2UwOTc2MjQ2IiwidCI6ImU5YTgyZWM3LTRhODYtNDNkZS1hYjJhLTcxOWQ2Njk1OWExYiJ9"

# Parâmetros essenciais
powerbi_link += "&rs:embed=true"
powerbi_link += "&rs:command=Render"
powerbi_link += "&rs:device=desktop"

# Verifica se é dispositivo móvel
is_mobile_device = is_mobile()

# Aviso para mobile
if is_mobile_device:
    st.markdown(
        '<div class="mobile-warning">📱 Para melhor experiência, gire seu dispositivo para o modo paisagem</div>',
        unsafe_allow_html=True
    )

# HTML para incorporar o Power BI
st.markdown(
    f"""
    <div class="responsive-container {'mobile-view' if is_mobile_device else 'desktop-view'}">
        <iframe class="responsive-iframe" 
                src="{powerbi_link}" 
                allowfullscreen>
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

# Rodapé otimizado
show_footer()