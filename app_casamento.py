import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Casamento João & Francielle", 
    page_icon="💍", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização personalizada para deixar o site moderno, limpo e romântico
st.markdown("""
    <style>
    /* Alinhamento global e fontes */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Customização dos botões */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        border: none;
        background: linear-gradient(135deg, #ff823a 0%, #bc84ee 100%);
        color: white;
        font-weight: 600;
        transition: all 0.3s ease;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(188, 132, 238, 0.4);
        color: white;
    }
    
    /* Estilo dos Cards de Presentes */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 15px;
    }
    
    /* Títulos e Subtítulos */
    .wedding-title {
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 5px;
    }
    .wedding-subtitle {
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 25px;
    }
    
    /* Infos de Chave Pix */
    .pix-box {
        background-color: #f8fafc;
        border-left: 5px solid #bc84ee;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<h1 class='wedding-title'>💍 Nosso Casamento: João & Francielle</h1>", unsafe_allow_html=True)
st.markdown("<p class='wedding-subtitle'>22 de Agosto de 2026 • Bichinhos, MG</p>", unsafe_allow_html=True)

st.write(
    "Padrinhos e convidados, criamos esta lista de presentes realistas e bem-humorados "
    "para que vocês nos ajudem a começar nossa vida de casados, organizar nossa lua de mel e, claro, garantir a paz do lar! 😄"
)

st.divider()

# --- CONFIGURAÇÃO DOS PRESENTES ---
# Lista de presentes com títulos, valores e descrições baseadas nas imagens criadas
presentes = [
    {
        "titulo": "💸 Adote um Boleto do Casal",
        "valor": 75.00,
        "desc": "Ajude o casal a pagar os boletos da vida real e começar o casamento com as contas no azul! (A Francielle agradece o apoio ao João!).",
        "imagem": "watermarked_img_17953936335980797091.png",  # Imagem do casal com os boletos e a foto emoldurada
        "link_cartao": "https://link.mercadopago.com.br/seu-link-boleto"
    },
    {
        "titulo": "🏡 Passeio na Casa Torta de Bichinhos",
        "valor": 110.00,
        "desc": "Entrada garantida na famosa atração turística da Casa Torta na charmosa vila de Bichinhos, MG, para um passeio romântico e divertido.",
        "imagem": "casa torta.webp",  # Foto original da Casa Torta de Bichinhos
        "link_cartao": "https://link.mercadopago.com.br/seu-link-casatorta"
    },
    {
        "titulo": "🥂 Jogo de Taças e Copos",
        "valor": 220.00,
        "desc": "Para brindar os momentos felizes na casa nova (e garantir que os padrinhos tenham onde beber quando forem nos visitar!).",
        "imagem": "jogo_tacas.png",  # Nome sugerido para a ilustração de taças e copos
        "link_cartao": "https://link.mercadopago.com.br/seu-link-tacas"
    },
    {
        "titulo": "📺 Streaming para a Noiva Ter um Minuto de Paz",
        "valor": 450.00,
        "desc": "1 ano garantido de maratonas de séries favoritas para a Francielle relaxar no sofá enquanto o João se concentra na física e nos códigos.",
        "imagem": "streaming_paz.png",  # Nome sugerido para a imagem da noiva no sofá assistindo TV
        "link_cartao": "https://link.mercadopago.com.br/seu-link-streaming"
    },
    {
        "titulo": "💪 O PIX para 'Segunda Começarmos na Academia'",
        "valor": 190.00,
        "desc": "A clássica promessa de início de semana que agora vai virar realidade com a Francielle liderando o foco fitness na academia!",
        "imagem": "watermarked_img_5885490087528510738.png",  # Imagem focada na noiva decidida no calendário da academia
        "link_cartao": "https://link.mercadopago.com.br/seu-link-academia"
    },
    {
        "titulo": "🚗 Aluguel de Carro para a Lua de Mel",
        "valor": 380.00,
        "desc": "Ajuda para o aluguel do carro conversível perfeito para o casal explorar as belas estradas de Minas Gerais durante a lua de mel.",
        "imagem": "aluguel_carro.png",  # Nome sugerido para o desenho do casal dirigindo o conversível
        "link_cartao": "https://link.mercadopago.com.br/seu-link-carro"
    },
    {
        "titulo": "🧣 Um Cobertor para a Noiva 'Coberta de Razão'",
        "valor": 130.00,
        "desc": "Porque todos nós sabemos que a noiva está sempre coberta de razão! Garanta o aquecimento físico e moral da Francielle.",
        "imagem": "cobertor_razao.png",  # Nome sugerido para o desenho da noiva sob o cobertor
        "link_cartao": "https://link.mercadopago.com.br/seu-link-cobertor"
    },
    {
        "titulo": "🐾 Ajuda para a Ração da Amora e da Bebel",
        "valor": 350.00,
        "desc": "6 meses de ração super premium garantidos para as donas da casa: a Amora (nossa companheira pretinha) e a Bebel (nossa branquinha fofa).",
        "imagem": "racao_pets.png",  # Nome sugerido para o desenho das duas com seus potinhos personalizados de ração
        "link_cartao": "https://link.mercadopago.com.br/seu-link-racao"
    },
    {
        "titulo": "🤫 Tampão de Ouvido para o Noivo",
        "valor": 100.00,
        "desc": "Item essencial de sobrevivência conjugal para o João filtrar o esporro carinhoso da noiva e focar na paz interior! Com balão clássico do 'Esporro da Noiva!'.",
        "imagem": "watermarked_img_4092439108608279997.png",  # Imagem limpa com o noivo e o balão do esporro da noiva
        "link_cartao": "https://link.mercadopago.com.br/seu-link-tampao"
    }
]

# Exibição dos Presentes em Grid Responsivo (3 colunas)
cols = st.columns(3)

for i, item in enumerate(presentes):
    with cols[i % 3]:
        with st.container(border=True):
            # Tenta carregar a imagem configurada, senão exibe um placeholder bonito
            try:
                st.image(item["imagem"], use_container_width=True)
            except Exception:
                st.image("https://placehold.co/400x300/f8fafc/bc84ee?text=💍+Presente+Especial", use_container_width=True)
            
            st.markdown(f"### {item['titulo']}")
            st.markdown(f"**Valor sugerido: R$ {item['valor']:.2f}**")
            st.write(item["desc"])
            
            # Botões para ações de pagamento
            col_btn1, col_btn2 = st.columns(2)
            
            with col_btn1:
                texto_wa = f"Oi! Quero presentear vocês com: {item['titulo']} via Pix!"
                link_wa = f"https://wa.me/5535999999999?text={texto_wa.replace(' ', '%20')}"
                st.link_button("✉️ Via Pix", link_wa, use_container_width=True)
                
            with col_btn2:
                st.link_button("💳 Cartão", item["link_cartao"], use_container_width=True)

st.divider()

# --- INSTRUÇÕES GERAIS / PIX ---
st.markdown("## ℹ️ Como Presentear")
st.markdown(
    """
    <div class="pix-box">
        <h4>Chave Pix Direta para o Casal:</h4>
        <p><strong>seu-email-ou-cpf@aqui.com</strong><br>
        <em>Nome: João Gabriel M. Carvalho (Banco Sicoob/Inter)</em></p>
        <p style="margin-top: 10px; font-size: 0.9rem; color: #475569;">
            💡 <strong>Dica:</strong> Se fizer via Pix Direto pelo seu banco, clique no botão "Via Pix" acima do item escolhido 
            para nos avisar no WhatsApp qual presente você escolheu! Se preferir usar o cartão de crédito, use o botão correspondente.
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
