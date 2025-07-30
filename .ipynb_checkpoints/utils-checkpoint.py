import streamlit as st

def is_mobile():
    """Determina se deve mostrar a versão mobile, considerando a preferência do usuário"""
    # Verifica se o usuário forçou um modo específico
    if "force_mobile" in st.query_params:
        return True
    if "force_desktop" in st.query_params:
        return False
    
    # Tenta detecção automática usando headers
    try:
        ctx = st.runtime.scriptrunner.script_run_context.get_script_run_ctx()
        if ctx and hasattr(ctx, 'request'):
            user_agent = ctx.request.headers.get("User-Agent", "").lower()
            mobile_keywords = ['mobile', 'android', 'iphone', 'ipad', 'windows phone']
            return any(keyword in user_agent for keyword in mobile_keywords)
    except Exception:
        pass
    return False

def show_header(show_calculadora=True):
    # Determina o modo atual
    mobile_mode = is_mobile()
    
    # Obtém os parâmetros atuais da URL
    params = st.query_params
    
    # Constrói a query string para manter o modo
    query_string = "?force_mobile=1" if "force_mobile" in params else ""
    
    # Mostra a barra superior
    if mobile_mode:
        st.image("imagem/header_mob.png", use_container_width=True)
        
        # Links com imagens e botões reais
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        if show_calculadora:
            with col2:
                # Link para o Dashboard - SEM query string
                st.page_link("pages/Dashboard.py", label="**Análise Resíduos BH**")
            with col4:
                st.page_link("https://novocicloresiduos.com.br/", label="**Sobre o Projeto**")
            st.image("imagem/calc_mob.png", use_container_width=True)
        else:
            with col2:
                # Link para calculadora - SEM query string
                st.page_link("app.py", label="**Calculadora de impacto coleta seletiva**")
            with col4:
                st.page_link("https://novocicloresiduos.com.br/", label="**Sobre o Projeto**")
    else:
        st.image("imagem/header.png", use_container_width=True)
        
        # Links com imagens e botões reais
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        if show_calculadora:
            with col2:
                # Link para o Dashboard - SEM query string
                st.page_link("pages/Dashboard.py", label="**Análise Resíduos BH**")
            with col4:
                st.page_link("https://novocicloresiduos.com.br/", label="**Sobre o Projeto**")
            st.image("imagem/calculadora_circulos.png", use_container_width=True)
        else:
            with col2:
                # Link para calculadora - SEM query string
                st.page_link("app.py", label="**Calculadora de impacto coleta seletiva**")
            with col4:
                st.page_link("https://novocicloresiduos.com.br/", label="**Sobre o Projeto**")

def show_footer():
    # Mostra a imagem do rodapé
    if is_mobile():
        st.image("imagem/logos_mob.png", use_container_width=True)
    else:
        st.image("imagem/logos.png", use_container_width=True)
    
    st.markdown("---")
    
    # Mostra mensagem de modo atual
    if "force_mobile" in st.query_params:
        st.info(" Você está visualizando a versão para celular")
    
    # Botão para alternar versão
    st.markdown("""
    <div class="mode-switcher" style="text-align: center; margin: 20px 0; padding: 15px; background-color: #f0f2f6; border-radius: 5px;">
        <p style="margin-bottom: 15px;">Alterar versão:</p>
        <a href="?force_mobile=1" style="width: 80%; padding: 12px 15px; background-color: #4CAF50; color: white; border-radius: 4px; text-decoration: none; text-align: center;">
            Versão para Celular
        </a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; margin-top: 10px;">
    <small><a href="?" style="color: #666; text-decoration: none;">Restaurar modo padrão</a></small>
    </div>
    """, unsafe_allow_html=True)
