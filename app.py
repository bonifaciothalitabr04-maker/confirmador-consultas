import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="SUS - Confirmação de Consultas",
    page_icon="⚕️",
    layout="centered"
)

# Estilização visual SUS
st.markdown(
    """
    <style>
        .sus-header {
            background: linear-gradient(135deg, #005CA9 0%, #003B6F 100%);
            padding: 22px;
            border-radius: 10px;
            color: white;
            text-align: center;
            margin-bottom: 25px;
        }
        .sus-header h1 {
            color: #FFFFFF !important;
            font-size: 24px;
            margin: 0;
            font-weight: 700;
        }
        .sus-header p {
            color: #E2E8F0;
            font-size: 14px;
            margin-top: 5px;
            margin-bottom: 0;
        }
        div.stButton > button:first-child {
            background-color: #005CA9 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            border: none !important;
            width: 100% !important;
            padding: 10px 20px !important;
        }
        .sus-footer {
            text-align: center;
            color: #64748B;
            font-size: 12px;
            margin-top: 35px;
            padding-top: 15px;
            border-top: 1px solid #E2E8F0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sus-header">
        <div style="font-size: 26px; margin-bottom: 4px;">⚕️</div>
        <h1>SISTEMA ÚNICO DE SAÚDE</h1>
        <p>Central de Notificação e Confirmação de Consultas</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    nome_paciente = st.text_input("Nome do Paciente", placeholder="Ex: Maria da Silva")
    data = st.text_input("Data da Consulta", placeholder="Ex: 20/10/2026")

with col2:
    telefone = st.text_input("WhatsApp (com DDD)", placeholder="Ex: 34999998888")
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

st.markdown(
    """
    <div class="sus-footer">
        Ministério da Saúde • Sistema Único de Saúde • Brasil
    </div>
    """,
    unsafe_allow_html=True
)
