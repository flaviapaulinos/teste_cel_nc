# Dashboard.py
import streamlit as st
import streamlit.components.v1 as components
from utils import show_header, show_footer, is_mobile  # Importe a função is_mobile

# Configuração de layout
st.set_page_config(
    layout="wide", 
    page_title="Dashboard de Resíduos",
    initial_sidebar_state="collapsed"
)

# CSS responsivo otimizado
st.markdown("""
    <style>
        section[data-testid="stSidebar"] { display: none !important; }
        .stApp { padding: 0 !important; margin: 0 !important; }
        header, footer { padding: 0 !important; }
        
        .responsive-container { position: relative; width: 100%; overflow: hidden; }
        .desktop-view { padding-top: 56.25%; } /* 16:9 */
        .mobile-view { height: calc(100vh - 150px); } /* Altura ajustada */
        
        .responsive-iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }
        
        .mobile-warning {
            padding: 10px;
            text-align: center;
            background-color: #fff8e1;
            color: #333;
            font-size: 14px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
        
        @media (max-width: 768px) {
            .stImage img { max-height: 50px !important; }
            .stMarkdown, .stMarkdown p { font-size: 16px !important; }
        }
    </style>
""", unsafe_allow_html=True)

# Mostra cabeçalho otimizado
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