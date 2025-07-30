import streamlit as st
import re

import streamlit as st
import re

# Inicializa as variáveis de sessão se necessário
if 'screen_width' not in st.session_state:
    st.session_state.screen_width = 1024
if 'is_mobile' not in st.session_state:
    st.session_state.is_mobile = False

def is_mobile():
    """Detecção híbrida: User-Agent + tamanho de tela"""
    try:
        # 1. Tentativa com User-Agent
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        ctx = get_script_run_ctx()
        user_agent = ctx.request.headers.get("User-Agent", "").lower() if ctx else ""
        
        # Palavras-chave para dispositivos móveis
        mobile_keywords = ['mobile', 'android', 'iphone', 'ipad', 'windows phone']
        if any(keyword in user_agent for keyword in mobile_keywords):
            st.session_state.is_mobile = True
            return True
        
        # 2. Verificação pelo tamanho da tela (via JavaScript)
        # Script para detectar a largura da tela
        st.components.v1.html("""
            <script>
            function sendScreenSize() {
                const width = window.innerWidth;
                // Envia as dimensões de volta para o Streamlit
                window.parent.postMessage(
                    {type: 'screenSize', screenWidth: width}, 
                    '*'
                );
            }
            
            // Envia o tamanho da tela quando a página carrega e quando redimensiona
            window.addEventListener('load', sendScreenSize);
            window.addEventListener('resize', sendScreenSize);
            </script>
        """, height=0)
        
        # Se largura de tela < 768px, consider como mobile
        if st.session_state.screen_width < 768:
            st.session_state.is_mobile = True
            return True
            
    except Exception as e:
        st.error(f"Erro na detecção de dispositivo: {e}")
        pass
    
    st.session_state.is_mobile = False
    return False

# Função para capturar mensagens do JavaScript
def capture_js_messages():
    """Captura mensagens do JavaScript para detectar tamanho de tela"""
    # Componente para receber mensagens do JavaScript
    result = st.components.v1.html("""
        <script>
        window.addEventListener('message', (event) => {
            if (event.data.type === 'screenSize') {
                const screenWidth = event.data.screenWidth;
                window.parent.postMessage({
                    type: 'setScreenWidth', 
                    screenWidth: screenWidth
                }, '*');
            }
        });
        </script>
    """, height=0)
    
    # Tenta capturar a mensagem do JavaScript
    try:
        from streamlit.web.server.websocket_headers import _get_websocket_headers
        headers = _get_websocket_headers()
        if headers and 'screenWidth' in headers:
            st.session_state.screen_width = int(headers['screenWidth'])
    except:
        pass


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

    
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <a href="?force_mobile=1">Versão para celular</a> | 
        <a href="?force_desktop=1">Versão para computador</a>
    </div>"""
               )
    