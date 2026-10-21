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

# Cabe
