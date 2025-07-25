import streamlit as st
from utils import show_header, show_footer

# Configuração de layout amplo
st.set_page_config(layout="wide")

# Mostra cabeçalho personalizado
show_header()

st.title("🔗 Conheça o projeto")

# Container central para conteúdo
with st.container():
    left_padding, main_content, right_padding = st.columns([0.5, 3, 0.5])
    
    with main_content:
        st.markdown("""
        <div style='background-color:#fff0f6; padding:25px; border-radius:15px;'>
        <h2>Sobre o Projeto</h2>
        <p style='font-size:18px;'>
        O projeto <b>Análise e Impacto dos Resíduos em Belo Horizonte</b> nasceu da necessidade de compreender 
        e quantificar os benefícios ambientais e econômicos da reciclagem em nossa cidade. 
        Através de dados coletados pela prefeitura e estudos do IPEA, desenvolvemos ferramentas 
        para visualizar o impacto positivo da coleta seletiva.
        </p>
        
        <div style='display:flex; justify-content:space-between; margin-top:30px;'>
            <div style='flex:1; padding:15px; background:#e6f7ff; border-radius:10px; margin-right:10px;'>
                <h3>📈 Nossos Objetivos</h3>
                <ul>
                    <li>Quantificar a economia gerada pela reciclagem</li>
                    <li>Reduzir o impacto ambiental dos resíduos</li>
                    <li>Transformar BH em cidade modelo em gestão de resíduos</li>
                    <li>Conscientizar a população sobre a importância da reciclagem</li>
                </ul>
            </div>
            
            <div style='flex:1; padding:15px; background:#f6ffed; border-radius:10px; margin-left:10px;'>
                <h3>👥 Equipe</h3>
                <div style='display:flex; justify-content:space-around;'>
                    <div style='text-align:center;'>
                        <div style='background-color:#d9d9d9; width:80px; height:80px; border-radius:50%; margin:0 auto 10px;'></div>
                        <b>Joana Silva</b><br>Coordenadora
                    </div>
                    <div style='text-align:center;'>
                        <div style='background-color:#d9d9d9; width:80px; height:80px; border-radius:50%; margin:0 auto 10px;'></div>
                        <b>Carlos Mendes</b><br>Analista de Dados
                    </div>
                    <div style='text-align:center;'>
                        <div style='background-color:#d9d9d9; width:80px; height:80px; border-radius:50%; margin:0 auto 10px;'></div>
                        <b>Mariana Costa</b><br>Engenheira Ambiental
                    </div>
                </div>
            </div>
        </div>
        
        <div style='margin-top:30px; text-align:center;'>
            <h3>🤝 Parceiros</h3>
            <div style='background-color:#f0f0f0; padding:20px; border-radius:10px;'>
                <p>Logos dos parceiros serão exibidas aqui</p>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

# Rodapé
show_footer()