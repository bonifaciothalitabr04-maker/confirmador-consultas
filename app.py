import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

st.set_page_config(page_title="Confirmação WhatsApp", page_icon="🏥", layout="centered")

st.title("🏥 Central de Confirmação de Consultas")
st.write("Preencha os dados abaixo para enviar a confirmação.")

col1, col2 = st.columns(2)
with col1:
    nome_paciente = st.text_input("Nome do Paciente", placeholder="Ex: Maria da Silva")
    data = st.text_input("Data da Consulta", placeholder="Ex: 25/11/2026")
with col2:
    telefone = st.text_input("WhatsApp (com DDD)", placeholder="Ex: 34999998888")
    horario = st.text_input("Horário", placeholder="Ex: 14:30")

nome_medico = st.text_input("Nome do Médico", placeholder="Ex: Dr. Carlos Eduardo")

if st.button("Gerar e Abrir no WhatsApp", type="primary"):
    if not telefone or not nome_paciente:
        st.error("Por favor, preencha pelo menos o nome do paciente e o WhatsApp.")
    else:
        num_limpo = ''.join(filter(str.isdigit, str(telefone)))
        if not num_limpo.startswith('55'):
            num_limpo = '55' + num_limpo

        mensagem = (
            f"Olá, {nome_paciente}!\n\n"
            f"Passando para confirmar sua consulta médica agendada:\n"
            f"- Médico(a): {nome_medico}\n"
            f"- Data: {data}\n"
            f"- Horário: {horario}\n\n"
            f"Por favor, responda com *SIM* para confirmar ou nos avise caso precise reagendar."
        )

        texto_url = urllib.parse.quote(mensagem, safe='')
        link_app_pc = f"whatsapp://send/?phone={num_limpo}&text={texto_url}"

        st.success("Mensagem preparada com sucesso!")
        st.text_area("Pré-visualização do texto:", mensagem, height=130)

        # Dispara a abertura do aplicativo nativo diretamente via script
        components.html(
            f"""
            <iframe src="{link_app_pc}" style="display:none;"></iframe>
            <div style="text-align: center; margin-top: 10px;">
                <p style="color: #166534; font-weight: bold;">
                    A abrir o WhatsApp no computador...
                </p>
                <a href="{link_app_pc}" style="
                    display: inline-block;
                    background-color: #25D366;
                    color: white;
                    padding: 10px 18px;
                    border-radius: 6px;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 14px;
                ">
                    Clique aqui se o programa não abrir automaticamente
                </a>
            </div>
            """,
            height=90
        )
