import streamlit as st
import urllib.parse

st.set_page_config(page_title="Confirmação WhatsApp", page_icon="🏥", layout="centered")

st.title("🏥 Central de Confirmação de Consultas")
st.write("Preencha os dados abaixo para gerar a mensagem e abrir o WhatsApp.")

col1, col2 = st.columns(2)
with col1:
    nome_paciente = st.text_input("Nome do Paciente", placeholder="Ex: Maria da Silva")
    data = st.text_input("Data da Consulta", placeholder="Ex: 25/11/2026")
with col2:
    telefone = st.text_input("WhatsApp (com DDD)", placeholder="Ex: 34999998888")
    horario = st.text_input("Horário", placeholder="Ex: 14:30")

nome_medico = st.text_input("Nome do Médico", placeholder="Ex: Dr. Carlos Eduardo")

if st.button("Gerar Mensagem", type="primary"):
    if not telefone or not nome_paciente:
        st.error("Por favor, preencha ao menos o nome do paciente e o WhatsApp.")
    else:
        num_limpo = ''.join(filter(str.isdigit, str(telefone)))
        if not num_limpo.startswith('55'):
            num_limpo = '55' + num_limpo

        mensagem = (
            f"Olá, {nome_paciente}! 👋\n\n"
            f"Passando para confirmar sua consulta médica agendada:\n"
            f"👨‍⚕️ Médico(a): {nome_medico}\n"
            f"📅 Data: {data}\n"
            f"⏰ Horário: {horario}\n\n"
            f"Por favor, responda esta mensagem com *SIM* para confirmar ou nos avise se precisar reagendar."
        )

        texto_url = urllib.parse.quote(mensagem)
        
        # Link direto para WhatsApp Web (no computador)
        link_web = f"https://web.whatsapp.com/send?phone={num_limpo}&text={texto_url}"
        
        # Link universal direto para celular (abre o app do WhatsApp no telefone)
        link_mobile = f"https://wa.me/{num_limpo}?text={texto_url}"

        st.success("Mensagem gerada!")
        st.text_area("Pré-visualização do texto:", mensagem, height=130)

        # Botão principal para quem está no PC
        st.link_button("💻 Enviar pelo WhatsApp Web (Computador)", link_web, type="primary")
        
        # Botão alternativo para celular
        st.link_button("📱 Enviar pelo Celular (App)", link_mobile)
