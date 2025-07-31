import streamlit as st
import urllib.parse

def is_mobile():
    if "force_mobile" in st.query_params: return True
    if "force_desktop" in st.query_params: return False
    try:
        ctx = st.runtime.scriptrunner.script_run_context.get_script_run_ctx()
        user_agent = ctx.request.headers.get("User-Agent", "").lower()
        mobile_keywords = ['mobile', 'android', 'iphone', 'ipad']
        return any(k in user_agent for k in mobile_keywords)
    except: return False

def get_page_url(page_path):
    params = st.query_params.to_dict()
    if "force_mobile" in params: del params["force_desktop"]
    if "force_desktop" in params: del params["force_mobile"]
    return f"{page_path}?{urllib.parse.urlencode(params)}" if params else page_path

def show_header(show_calculadora=True):
    mobile_mode = is_mobile()
    st.markdown("""
    <style>
        .nav-link-container { padding: 0 15px; margin-bottom: 10px; text-align: center; }
        @media (max-width: 768px) { .nav-link-container { padding: 0 5px; } }
        .nav-link { display: block; padding: 8px 12px; border-radius: 4px; transition: all 0.3s; }
        .nav-link:hover { background-color: #f0f0f0; transform: scale(1.05); }
    </style>
    """, unsafe_allow_html=True)
    
    if mobile_mode:
        st.image("imagem/header_mob.png", use_container_width=True)
        col1, col2, col3, col4 = st.columns([1, 2, 1, 2])
        if show_calculadora:
            col2.markdown(f'<div class="nav-link-container"><a href="{get_page_url("pages/Dashboard.py")}" class="nav-link">Análise Resíduos BH</a></div>', unsafe_allow_html=True)
            col4.markdown(f'<div class="nav-link-container"><a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a></div>', unsafe_allow_html=True)
            st.image("imagem/calc_mob.png", use_container_width=True)
        else:
            col2.markdown(f'<div class="nav-link-container"><a href="{get_page_url("app.py")}" class="nav-link">Calculadora</a></div>', unsafe_allow_html=True)
            col4.markdown(f'<div class="nav-link-container"><a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a></div>', unsafe_allow_html=True)
    else:
        st.image("imagem/header.png", use_container_width=True)
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        if show_calculadora:
            col2.markdown(f'<a href="{get_page_url("pages/Dashboard.py")}" class="nav-link">Análise Resíduos BH</a>', unsafe_allow_html=True)
            col4.markdown(f'<a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a>', unsafe_allow_html=True)
            st.image("imagem/calc_bar.png", use_container_width=True)
        else:
            col2.markdown(f'<a href="{get_page_url("app.py")}" class="nav-link">Calculadora</a>', unsafe_allow_html=True)
            col4.markdown(f'<a href="https://novocicloresiduos.com.br/" class="nav-link">Sobre o Projeto</a>', unsafe_allow_html=True)

def show_footer():
    st.image("imagem/logos_mob_fundo.png" if is_mobile() else "imagem/logos.png", use_container_width=True)
    st.markdown("---")
    
    params = st.query_params.to_dict()
    mobile_params = {k: v for k, v in params.items() if k != "force_desktop"}
    mobile_params["force_mobile"] = "1"
    desktop_params = {k: v for k, v in params.items() if k != "force_mobile"}
    desktop_params["force_desktop"] = "1"
    reset_params = {k: v for k, v in params.items() if k not in ["force_mobile", "force_desktop"]}
    
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <a href="?{urllib.parse.urlencode(mobile_params)}" style="display: inline-block; padding: 12px 20px; background: #4CAF50; color: white; border-radius: 4px; text-decoration: none; margin: 0 10px;">
            Versão Celular
        </a>
        <a href="?{urllib.parse.urlencode(desktop_params)}" style="display: inline-block; padding: 12px 20px; background: #2196F3; color: white; border-radius: 4px; text-decoration: none; margin: 0 10px;">
            Versão Desktop
        </a>
    </div>
    <div style="text-align: center; margin-top: 10px;">
        <small><a href="?{urllib.parse.urlencode(reset_params)}" style="color: #666; text-decoration: none;">Restaurar modo padrão</a></small>
    </div>
    """, unsafe_allow_html=True)