import streamlit as st

# Configuração da página - Layout Wide para caber os cards lado a lado
st.set_page_config(page_title="Casamento João & Noiva", page_icon="💍", layout="wide")

# Estilização básica para os cards
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; }
    .gift-card { background-color: #f0f2f6; padding: 20px; border-radius: 15px; border: 1px solid #d1d5db; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("💍 Operação Casamento: 22 de Agosto")
st.subheader("Missão Padrinhos & Madrinhas")
st.write("Padrinhos, criamos esta lista para que vocês possam nos ajudar a tornar nossa festa e lua de mel inesquecíveis. Escolham um item e o valor será enviado diretamente para nós, sem taxas de sites!")

st.divider()

# --- ITENS DOS PADRINHOS ---
# (Item, Valor, Descrição)
presentes = [
    ("📺 1 Ano de Netflix (Sossego do João)", 480.00, "Garante as maratonas de séries da noiva enquanto o João se concentra na física e nos dados."),
    ("🧖‍♀️ Spa Anti-Surto para a Noiva", 250.00, "Tratamento essencial para evitar que a noiva surte com os fornecedores na semana do casamento."),
    ("🍹 Cota 'Open Bar' da Casa Nova", 180.00, "Para que o estoque de gin e cerveja esteja sempre pronto para quando os padrinhos aparecerem."),
    ("🍝 Jantar 'O João que fez'", 120.00, "Um valor simbólico para o primeiro jantar do casal (ou para o delivery que pediremos quando a receita falhar)."),
    ("🚗 Cota 'Fuga dos Noivos'", 150.00, "Ajuda para o tanque cheio e os pedágios rumo à Lua de Mel logo após a festa."),
    ("💡 Setup do Físico", 300.00, "Contribuição para a iluminação e organização do home-office onde o João vai codar (e minerar felicidade).")
]

# Exibição em Grid (3 colunas)
cols = st.columns(3)

for i, (item, valor, desc) in enumerate(presentes):
    with cols[i % 3]:
        with st.container():
            st.markdown(f"### {item}")
            st.write(f"**Sugestão: R$ {valor:.2f}**")
            st.caption(desc)
            
            # Botão de ação
            texto_whatsapp = f"Oi! Escolhi o presente: {item} (R$ {valor:.2f})"
            link_wa = f"https://wa.me/5535999999999?text={texto_whatsapp.replace(' ', '%20')}"
            
            st.link_button(f"🎁 Presentear {item.split()[0]}", link_wa)
            st.write("") # Espaçamento

st.divider()

# --- INSTRUÇÕES DE PAGAMENTO ---
col_pix, col_rsvp = st.columns(2)

with col_pix:
    st.header("💰 Como enviar o presente?")
    st.write("Como não queremos pagar as taxas de 10% dos sites de casamento, pedimos que o envio seja via Pix direto:")
    st.info("**Chave Pix:** seu-email-ou-cpf@aqui.com\n\n**Nome:** João Gabriel M. Carvalho")
    st.warning("⚠️ Importante: Após o Pix, clique no botão do item acima para nos avisar pelo WhatsApp! Assim a gente comemora e retira o item da lista.")

with col_rsvp:
    st.header("✅ Confirmar Presença")
    with st.form("rsvp"):
        nome = st.text_input("Nome do Padrinho/Madrinha")
        st.form_submit_button("Confirmar para o dia 22/08")

# Rodapé
st.markdown("---")
st.markdown("<center>Feito com ❤️ (e Python) para o melhor time de padrinhos do mundo!</center>", unsafe_allow_html=True)