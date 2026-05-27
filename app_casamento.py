import streamlit as st
import urllib.parse

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Casamento João & Francielle",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILIZAÇÃO CUSTOMIZADA (CSS) ---
st.markdown("""
    <style>
    /* Importação de fontes elegantes */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        background-color: #FAF6F5;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #5D4037 !important;
    }
    
    /* Cartões dos presentes */
    .gift-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(93, 64, 55, 0.06);
        border: 1px solid #F1E5E2;
        margin-bottom: 10px;
        transition: transform 0.2s ease-in-out;
    }
    
    .gift-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(93, 64, 55, 0.1);
    }
    
    /* Preço em Destaque */
    .price-tag {
        font-size: 1.2rem;
        font-weight: 600;
        color: #C2185B;
        margin: 12px 0;
        line-height: 1.4;
    }
    
    /* Botões personalizados */
    .stButton>button {
        width: 100%;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÃO AUXILIAR: CÁLCULO REVERSO MERCADO PAGO ---
def calcular_valor_cartao(valor_original):
    """
    Calcula o valor final repassando a taxa de 4,99% + R$ 0,40 do Mercado Pago.
    Assim, após a taxa ser descontada, o casal recebe exatamente o valor original.
    """
    taxa_percentual = 0.0499
    tarifa_fixa = 0.40
    valor_final = (valor_original + tarifa_fixa) / (1 - taxa_percentual)
    return round(valor_final, 2)

# --- DADOS DO CASAL ---
CHAVE_PIX = "seu-email-ou-cpf@aqui.com" # Substitua pela sua chave real
NOME_PIX = "João Gabriel M. Carvalho"
TELEFONE_WHATSAPP = "5535999999999"  # Substitua pelo celular real com DDD (Exemplo: 5535999999999)

# --- CABEÇALHO ---
col_space1, col_header, col_space2 = st.columns([1, 4, 1])
with col_header:
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>💍 Nosso Casamento: João & Francielle</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #8D6E63 !important;'>22 de Agosto de 2026</h3>", unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center; font-size: 1.15rem; color: #5D4037;'>
        Queridos amigos, padrinhos e familiares! Escolhemos com muito carinho e bom humor itens reais da nossa 
        rotina para que vocês façam parte da construção do nosso lar e da nossa Lua de Mel! ❤️
        </p>
    """, unsafe_allow_html=True)
    
    # Exibição da foto real do casal
    try:
        st.image("WhatsApp Image 2026-05-26 at 20.56.57.jpeg", use_container_width=True, caption="João & Francielle ❤️")
    except Exception:
        st.info("✨ [Foto do Casal João & Francielle]")

st.divider()

# --- LISTA DE PRESENTES ATUALIZADA (10 ITENS) ---
# Estrutura: (Título, Valor Pix, Descrição, Nome do Arquivo de Imagem, Link do Mercado Pago)
presentes = [
    (
        "📝 Adote um Boleto do Casal",
        75.00,
        "Ajude o casal a começar a vida adulta sem sustos! Patrocine uma conta básica de água, luz ou internet para garantir o sossego no primeiro mês.",
        "boleto_casal.jpg",
        "https://link.mercadopago.com.br/seu-link-boleto"
    ),
    (
        "🏡 Passeio na Casa Torta de Bichinhos",
        110.00,
        "Um passeio mega divertido pela charmosa e famosa atração turística de Bichinhos, em Minas Gerais! Garanta fotos inesquecíveis para o nosso álbum.",
        "casa torta.webp", # Foto real fornecida
        "https://link.mercadopago.com.br/seu-link-casatorta"
    ),
    (
        "🍷 Jogo de Taças e Copos",
        220.00,
        "Para celebrarmos a vida nova e os jantares especiais! Essencial para termos onde servir uma boa bebida para as nossas visitas (prometemos aposentar os copos de requeijão!).",
        "tacas_copos.jpg",
        "https://link.mercadopago.com.br/seu-link-tacas"
    ),
    (
        "📺 Streaming para a Noiva ter um Minuto de Paz",
        450.00,
        "O verdadeiro segredo da harmonia do lar! Enquanto o João foca nas suas linhas de código e teorias de Física, a Francielle maratona suas séries favoritas tranquila.",
        "streaming_noiva.jpg",
        "https://link.mercadopago.com.br/seu-link-streaming"
    ),
    (
        "💪 O Pix para 'Segunda Começamos na Academia'",
        190.00,
        "Aquele incentivo financeiro para a clássica promessa de casal fitness finalmente sair do papel! A noiva estará bem atenta para garantir a frequência.",
        "academia.jpg",
        "https://link.mercadopago.com.br/seu-link-academia"
    ),
    (
        "🚗 Ajuda para Aluguel do Carro da Lua de Mel",
        380.00,
        "Contribua com a locomoção do casal durante a viagem de núpcias. Garanta que possamos explorar lindas paisagens com segurança e conforto!",
        "aluguel_carro.jpg",
        "https://link.mercadopago.com.br/seu-link-carro"
    ),
    (
        "🛌 Cobertor para a Noiva (Sempre Coberta de Razão)",
        130.00,
        "Regra número 1 do casamento: a noiva está sempre certa! Esse cobertor quentinho vai mantê-la confortável enquanto desfruta da sua razão absoluta.",
        "cobertor.jpg",
        "https://link.mercadopago.com.br/seu-link-cobertor"
    ),
    (
        "🐶 Ração de Qualidade para a Amora e a Bebel",
        350.00,
        "Nossas filhotas de quatro patas também querem comemorar! Ajude a garantir o estoque de ração super premium para manter as duas fortes e saudáveis.",
        "pets_racao", # Identificador para usar fotos reais dos dogs
        "https://link.mercadopago.com.br/seu-link-racao"
    ),
    (
        "🧼 Banho para a Amora e Brinquedo para a Bebel",
        90.00,
        "Dia de spa para a Amora (que é a pretinha mais charmosa!) e diversão garantida com brinquedinho novo para a Bebel (nossa branquinha amada!).",
        "pets_banho", # Identificador para fotos reais dos dogs
        "https://link.mercadopago.com.br/seu-link-banho"
    ),
    (
        "🔇 Tampão de Ouvido Seletivo para o Noivo",
        100.00,
        "O acessório de sobrevivência do noivo para ouvir os famosos 'esporros carinhosos' da noiva de forma sutil, transformando o som em pura melodia e amor.",
        "tampao.jpg",
        "https://link.mercadopago.com.br/seu-link-tampao"
    )
]

# --- GRID DE PRESENTES ---
st.markdown("<h2 style='text-align: center; margin-top: 30px;'>🎁 Lista de Presentes Virtuais</h2>", unsafe_allow_html=True)

cols = st.columns(3)

for i, (titulo, valor_pix, desc, img_nome, link_cartao) in enumerate(presentes):
    valor_cartao = calcular_valor_cartao(valor_pix)
    
    with cols[i % 3]:
        # Card em HTML para manter a unidade visual
        st.markdown(f"""
            <div class="gift-card">
                <h3 style="margin-top: 0; font-size: 1.3rem; color: #5D4037; height: 50px; overflow: hidden;">{titulo}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Lógica especial para exibir as fotos reais das cadelinhas
        if img_nome in ["pets_racao", "pets_banho"]:
            try:
                col_dog1, col_dog2 = st.columns(2)
                with col_dog1:
                    st.image("momola.jpeg", use_container_width=True, caption="Amora 🐾")
                with col_dog2:
                    st.image("bebel.jpeg", use_container_width=True, caption="Bebel 🎀")
            except Exception:
                st.caption("🐾 [Fotos de Amora & Bebel]")
        else:
            # Carregamento seguro das outras imagens
            try:
                st.image(img_nome, use_container_width=True)
            except Exception:
                st.markdown("""
                    <div style="background-color: #F5EEEE; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 8px; margin-bottom: 10px;">
                        <span style="font-size: 3rem;">🎁</span>
                    </div>
                """, unsafe_allow_html=True)
                
        st.write(desc)
        
        # Exibição de preços
        st.markdown(f"""
            <div class="price-tag">
                💵 Pix Direto: <b>R$ {valor_pix:.2f}</b><br/>
                <span style="font-size: 0.85rem; color: #757575; font-weight: normal;">
                    💳 No Cartão: R$ {valor_cartao:.2f} <br/>(taxas operacionais inclusas)
                </span>
            </div>
        """, unsafe_allow_html=True)
        
        # Botões de Ação
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            texto_wa = f"Olá João e Francielle! Escolhi presentear vocês com '{titulo}' via Pix (R$ {valor_pix:.2f}). Podem me passar os dados?"
            texto_codificado = urllib.parse.quote(texto_wa)
            link_wa = f"https://wa.me/{TELEFONE_WHATSAPP}?text={texto_codificado}"
            st.link_button("✉️ Via Pix", link_wa, type="primary")
            
        with col_btn2:
            st.link_button("💳 No Cartão", link_cartao)
            
        st.markdown("<p style='text-align: center; color: #E0D4D1; font-size: 0.8rem; margin-top: 15px;'>━━━━━ 💝 ━━━━━</p>", unsafe_allow_html=True)

st.divider()

# --- PAINEL INFORMATIVO DE SEGURANÇA E TAXAS ---
st.markdown("<h2 style='text-align: center;'>ℹ️ Como funciona o envio dos presentes?</h2>", unsafe_allow_html=True)

col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown(f"""
        <div style="background-color: #E8F5E9; padding: 22px; border-radius: 12px; border-left: 5px solid #4CAF50; height: 100%;">
            <h4 style="color: #2E7D32; margin-top: 0; font-family: 'Playfair Display', serif; font-size: 1.3rem;">🍀 Via Pix Direto (Sem taxas!)</h4>
            <p style="color: #1B5E20; font-size: 0.95rem;">
                É a forma de carinho mais direta e prática! O valor integral cai direto na nossa conta, livre de qualquer taxa cobrada pelas operadoras.
            </p>
            <p style="font-size: 1rem; font-weight: bold; color: #1B5E20; background-color: #C8E6C9; padding: 10px; border-radius: 6px; display: inline-block;">
                🔑 Chave Pix: {CHAVE_PIX}<br/>
                👤 Titular: {NOME_PIX}
            </p>
        </div>
    """, unsafe_allow_html=True)

with col_info2:
    st.markdown("""
        <div style="background-color: #ECEFF1; padding: 22px; border-radius: 12px; border-left: 5px solid #607D8B; height: 100%;">
            <h4 style="color: #37474F; margin-top: 0; font-family: 'Playfair Display', serif; font-size: 1.3rem;">💳 Via Cartão de Crédito</h4>
            <p style="color: #263238; font-size: 0.95rem;">
                Ideal para quem deseja parcelar o presente ou usar limite de cartão! Para viabilizar, as taxas operacionais de recebimento imediato da plataforma foram acrescidas ao valor final deste botão.
            </p>
            <p style="font-size: 0.9rem; color: #455A64; font-weight: bold; margin-top: 15px;">
                🔒 Processado com segurança através do <b>Mercado Pago</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <p style='text-align: center; margin-top: 50px; font-family: "Playfair Display", serif; font-size: 1.6rem; color: #8D6E63; font-style: italic;'>
        "Com todo o amor, Francielle, João, Amora 🐶 & Bebel 🐩"
    </p>
""", unsafe_allow_html=True)
