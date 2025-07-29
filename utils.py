import streamlit as st

def is_mobile():
    """Detecta se o usuário está em um dispositivo móvel"""
    try:
        # Tenta obter o contexto do Streamlit
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        ctx = get_script_run_ctx()
        if ctx is not None:
            user_agent = ctx.request.headers.get("User-Agent", "").lower()
            mobile_keywords = ['mobile', 'android', 'iphone', 'ipad', 'windows phone']
            return any(keyword in user_agent for keyword in mobile_keywords)
    except:
        # Fallback para caso de erro
        return False
    return False


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