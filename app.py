import streamlit as st
import urllib.parse

# Configurações da página
st.set_page_config(
    page_title="SUS - Confirmação de Consultas",
    page_icon="⚕️",
    layout="centered"
)

# Estilização visual inspirada na identidade do SUS
st.markdown(
    """
    <style>
        .main {
            background-color: #F8FAFC;
        }
        .sus-header {
            background: linear-gradient(135deg, #005CA9 0%, #003B6F 100%);
            padding: 24px;
            border-radius: 12px;
            color: white;
            text-align: center;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }
        .sus-header h1 {
            color: #FFFFFF !important;
            font-size: 26px;
            font-weight: 700;
            margin: 0;
            letter-spacing: 0.5px;
        }
        .sus-header p {
            color: #E2E8F0;
            font-size: 14px;
            margin-top: 6px;
            margin-bottom: 0;
        }
        label {
            font-weight: 600 !important;
            color: #1E293B !important;
        }
        .stTextInput input {
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            padding: 10px 14px !important;
        }
        .stTextInput input:focus {
            border-color: #005CA9 !important;
            box-shadow: 0 0 0 2px rgba(0, 92, 169, 0.2) !important;
        }
        div.stButton > button:first-child {
            background-color: #005CA9 !important;
            color: white !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 12px 24px !important;
            width: 100% !important;
            transition: all 0.2s ease-in-out !important;
        }
        div.stButton > button:first-child:hover {
            background-color: #004580 !important;
            box-shadow: 0 4px 8px rgba(0, 92, 169, 0.25) !important;
        }
        .sus-footer {
            text-align: center;
            color: #64748B;
            font-size: 12px;
            margin-top: 40px;
            padding-top: 15px;
            border-top: 1px solid #E2E8F0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho Institucional
st.markdown(
    """
    <div class="sus-header">
        <div style="font-size: 28px; margin-bottom: 4px;">⚕️</div>
        <h1>SISTEMA ÚNICO DE SAÚDE</h1>
        <p>Central de Notificação e Confirmação de Consultas Especializadas</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Campos de preenchimento
col1, col2 = st.columns(2)
with col1:
    nome_paciente = st.text_input("Nome do Paciente", placeholder="Ex: Maria da Silva")
    data = st.text_input("Data da Consulta", placeholder="Ex: 20/10/2026")

with col2:
    telefone = st.text_input("WhatsApp de Contato (com DDD)", placeholder="Ex: 34999998888")
    horario = st.text_input("Horário", placeholder="Ex: 18:30")

nome_medico = st.text_input("Nome do Médico(a)", placeholder="Ex: Dr. Fernando")
unidade_saude = st.text_input("Unidade / Posto (opcional)", placeholder="Ex: UBS Central")

st.write("")
btn_gerar = st.button("Gerar Mensagem de Confirmação")

if btn_gerar:
    if not telefone or not nome_paciente:
        st.error("Por favor, preencha pelo menos o nome do paciente e o WhatsApp.")
    else:
        num_limpo = ''.join(filter(str.isdigit, str(telefone)))
        if not num_limpo.startswith('55'):
            num_limpo = '55' + num_limpo

        linha_unidade = f"🏥 Local: {unidade_saude}\n" if unidade_saude else ""
        
        # Mensagem formatada com os avatares solicitados
        mensagem = (
            f"Olá, {nome_paciente}! 👋\n\n"
            f"Passando para confirmar sua consulta médica agendada:\n\n"
            f"{linha_unidade}"
            f"👨‍⚕️ Médico(a): {nome_medico}\n"
            f"📅 Data: {data}\n"
            f"⏰ Horário: {horario}\n\n"
            f"Por favor, responda esta mensagem com *SIM* para confirmar ou nos avise se precisar reagendar."
        )

        texto_url = urllib.parse.quote(mensagem, safe='')
        link_web = f"https://web.whatsapp.com/send?phone={num_limpo}&text={texto_url}"
        link_api = f"https://api.whatsapp.com/send?phone={num_limpo}&text={texto_url}"

        st.success("Mensagem preparada com sucesso!")
        st.text_area("Pré-visualização do texto:", mensagem, height=180)

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.link_button("💻 Enviar pelo WhatsApp Web", link_web, type="primary")
        with col_btn2:
            st.link_button("📱 Enviar pelo Celular / App", link_api)

# Rodapé
st.markdown(
    """
    <div class="sus-footer">
        Ministério da Saúde • Sistema Único de Saúde • Brasil
    </div>
    """,
    unsafe_allow_html=True
)
