import streamlit as st
import re

def is_mobile():
    """Detecta com mais precisão se o usuário está em um dispositivo móvel"""
    try:
        # Tenta obter o User-Agent do contexto do Streamlit
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        ctx = get_script_run_ctx()
        if ctx is not None:
            user_agent = ctx.request.headers.get("User-Agent", "").lower()
        else:
            # Fallback para User-Agent do navegador
            user_agent = st.experimental_user_agent.lower()
    except:
        # Fallback para User-Agent do navegador
        user_agent = st.experimental_user_agent.lower()
    
    # Palavras-chave para detecção de dispositivos móveis
    mobile_keywords = [
        'mobile', 'android', 'iphone', 'ipad', 'windows phone',
        'blackberry', 'webos', 'iemobile', 'kindle', 'opera mini'
    ]
    
    # Verifica se é um tablet (alguns tablets podem ser detectados como mobile)
    tablet_keywords = ['ipad', 'tablet', 'playbook', 'nexus 7', 'nexus 10']
    
    # Expressão regular para detectar dispositivos móveis
    mobile_pattern = r'android|webos|iphone|ipad|ipod|blackberry|iemobile|opera mini|mobile'
    
    # Verifica se é um dispositivo móvel
    is_mobile_device = any(keyword in user_agent for keyword in mobile_keywords)
    is_tablet = any(keyword in user_agent for keyword in tablet_keywords)
    
    # Verificação adicional com regex
    if re.search(mobile_pattern, user_agent, re.IGNORECASE):
        is_mobile_device = True
    
    # Considera tablets como dispositivos móveis para nossos propósitos
    return is_mobile_device or is_tablet

def show_header(show_calculadora=True):
    is_mobile_device = is_mobile()
    
    # Barra superior responsiva
    if is_mobile_device:
        st.image("imagem/barra_sup_mob.png", use_container_width=True)
    else:
        st.image("imagem/novo_ciclo_sup1.png", use_container_width=True)
    
    # Links responsivos
    if is_mobile_device:
        with st.expander("☰ Menu", expanded=False):
            col1, col2 = st.columns(2)
            if show_calculadora:
                with col1:
                    st.page_link("pages/Dashboard.py", label="📊 Análise Resíduos BH")
                with col2:
                    st.page_link("https://novocicloresiduos.com.br/", label="ℹ️ Sobre o Projeto")
            else:
                with col1:
                    st.page_link("app.py", label="🧮 Calculadora")
                with col2:
                    st.page_link("https://novocicloresiduos.com.br/", label="ℹ️ Sobre o Projeto")
    else:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        if show_calculadora:
            with col2:
                st.page_link("pages/Dashboard.py", label="📊 Análise Resíduos BH")
            with col4:
                st.page_link("https://novocicloresiduos.com.br/", label="ℹ️ Sobre o Projeto")
        else:
            with col2:
                st.page_link("app.py", label="🧮 Calculadora de Impacto")
            with col4:
                st.page_link("https://novocicloresiduos.com.br/", label="ℹ️ Sobre o Projeto")
    
    # Imagem da calculadora (se aplicável)
    if show_calculadora:
        if is_mobile_device:
            st.image("imagem/calc_mob.png", use_container_width=True)
        else:
            st.image("imagem/calculadora_circulos.png", use_container_width=True)

def show_footer():
    st.markdown("---")
    is_mobile_device = is_mobile()
    
    if is_mobile_device:
        st.image("imagem/calc_mob.png", use_container_width=True)
    else:
        st.image("imagem/logos.png", use_container_width=True)