import streamlit as st

# Configuração da página
st.set_page_config(page_title="Casamento João & Francielle", page_icon="💍", layout="wide")

# Estilização básica
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("💍 Nosso Casamento: João & Francielle")
st.subheader("22 de Agosto de 2026")
st.write("Padrinhos e convidados, escolhemos itens que refletem nossa vida real para nos ajudar a organizar a festa e a nossa lua de mel!")

st.divider()

# --- CONFIGURAÇÃO DOS PRESENTES ---
# Estrutura: (Título, Valor, Descrição, Nome_da_Imagem, Link_do_Cartao)
# DICA: Crie os links de valor fixo no app do Mercado Pago/PayPal e cole abaixo.
presentes = [
    (
        "📺 1 Ano de Netflix (Sossego do João)", 
        480.00, 
        "Garante as maratonas de séries da noiva enquanto o João se concentra nos códigos e na física.",
        "netflix.jpg", # Nome do arquivo de imagem que você vai subir no GitHub
        "https://link.mercadopago.com.br/seu-link-netflix" # Cole o link de pagamento aqui
    ),
    (
        "🧖‍♀️ Spa Relaxante para a Noiva", 
        250.00, 
        "Tratamento essencial anti-surto para a noiva relaxar na semana do casamento.",
        "spa.jpg",
        "https://link.mercadopago.com.br/seu-link-spa"
    ),
    (
        "🍹 Cota 'Open Bar' da Casa Nova", 
        180.00, 
        "Para garantir que o estoque esteja sempre pronto para quando os padrinhos visitarem.",
        "open_bar.jpg",
        "https://link.mercadopago.com.br/seu-link-bar"
    ),
    (
        "🍝 Jantar 'O João que fez'", 
        120.00, 
        "Contribuição para o primeiro jantar ou para o delivery de emergência se a receita falhar.",
        "jantar.jpg",
        "https://link.mercadopago.com.br/seu-link-jantar"
    )
]

# Exibição em Grid (2 colunas para dar destaque às fotos)
cols = st.columns(2)

for i, (titulo, valor, desc, img_nome, link_cartao) in enumerate(presentes):
    with cols[i % 2]:
        with st.container():
            # Tenta carregar a imagem. Se não achar, não quebra o site
            try:
                st.image(img_nome, use_container_width=True)
            except:
                st.caption("📷 [Espaço para a foto]")
                
            st.markdown(f"### {titulo}")
            st.markdown(f"**Valor: R$ {valor:.2f}**")
            st.write(desc)
            
            # Opções de pagamento
            col_btn1, col_btn2 = st.columns(2)
            
            with col_btn1:
                # Botão do Pix Grátis via WhatsApp
                texto_wa = f"Oi! Quero presentear com: {titulo} via Pix."
                link_wa = f"https://wa.me/5535999999999?text={texto_wa.replace(' ', '%20')}"
                st.link_button("💸 Presentear via Pix (Sem Taxas)", link_wa)
                
            with col_btn2:
                # Botão do Cartão (Mercado Pago / PayPal)
                st.link_button("💳 Pagar com Cartão", link_cartao)
            
            st.write("---")

st.divider()

# --- INSTRUÇÕES GERAIS ---
st.header("💰 Informações de Envio")
st.info("Se optar pelo Pix Direto, nossa chave é: **seu-email-ou-cpf@aqui.com** (João Gabriel M. Carvalho). Se preferir usar o cartão, basta clicar no botão correspondente ao item acima!")
