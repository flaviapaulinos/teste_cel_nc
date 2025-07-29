# utils.py
import streamlit as st
from device_detection import is_mobile

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