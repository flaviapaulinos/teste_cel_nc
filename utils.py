import streamlit as st
import re

import streamlit as st

# Corrija a função is_mobile
def is_mobile():
    """Determina se deve mostrar a versão mobile"""
    query_params = st.experimental_get_query_params()
    
    if "force_mobile" in query_params:
        return True
    if "force_desktop" in query_params:
        return False
    
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        ctx = get_script_run_ctx()
        if ctx and hasattr(ctx, 'request'):
            user_agent = ctx.request.headers.get("User-Agent", "").lower()
            mobile_keywords = ['mobi', 'android', 'iphone', 'ipad']
            return any(k in user_agent for k in mobile_keywords)
    except Exception:
        pass
    
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
    # Determina o modo atual
    mobile_mode = is_mobile()
    
    # Mostra a barra superior
    if mobile_mode:
        st.image("imagem/barra_sup_mob.png", use_container_width=True)
    else:
        st.image("imagem/novo_ciclo_sup1.png", use_container_width=True)
    
    # Mostra indicador de modo
    mode_indicator = "📱 Modo Celular" if mobile_mode else "💻 Modo Computador"
    st.markdown(f"""
    <div style="text-align: right; margin: -30px 10px 10px 0; position: relative; z-index: 100;">
        <small>{mode_indicator}</small>
    </div>
    """, unsafe_allow_html=True)

def show_footer():
    st.markdown("---")
    
    # Mostra a imagem do rodapé
    if is_mobile():
        st.image("imagem/calc_mob.png", use_container_width=True)
    else:
        st.image("imagem/logos.png", use_container_width=True)
    
    # Links para alternar entre versões
    st.markdown("""
    <div class="mode-switcher" style="text-align: center; margin-top: 20px; padding: 10px; background-color: #f0f2f6; border-radius: 5px;">
        <p style="margin-bottom: 10px;">Alterar versão:</p>
        <a href="?force_mobile=1" style="...">Versão para Celular</a>
        <a href="?force_desktop=1" style="...">Versão para Computador</a>  # Corrigido para 'desktop'
    </div>
    """, unsafe_allow_html=True)