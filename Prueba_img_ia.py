import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Test Motor Gráfico V2", page_icon="🎨")
st.title("🎨 Prueba de Motor Gráfico: V2 (Texto Responsive)")

# --- FUNCIÓN AUXILIAR: DESCARGAR FUENTE ---
# Esto garantiza que siempre tengamos una letra bonita y GRANDE
def conseguir_fuente(size):
    url_fuente = "https://github.com/google/fonts/raw/main/apache/roboto/Roboto-Bold.ttf"
    try:
        response = requests.get(url_fuente)
        return ImageFont.truetype(BytesIO(response.content), size)
    except:
        return ImageFont.load_default()

# --- FUNCIÓN DEL MOTOR GRÁFICO (El Cerebro) ---
def crear_anuncio_con_texto(url_fondo, headline_texto, cta_texto):
    # 1. Descargar imagen
    response = requests.get(url_fondo)
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    width, height = img.size
    draw = ImageDraw.Draw(img)

    # 2. CALCULAR TAMAÑO DINÁMICO (Aquí está la magia)
    # El texto será el 8% del ancho de la imagen (se adapta si la imagen es 4k o pequeña)
    size_headline = int(width * 0.08) 
    size_cta = int(width * 0.05)
    
    font_headline = conseguir_fuente(size_headline)
    font_cta = conseguir_fuente(size_cta)

    # 3. Dibujar Headline (Arriba)
    text_color = (255, 255, 255)
    
    # Calcular caja del texto
    bbox = draw.textbbox((0, 0), headline_texto, font=font_headline)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x_headline = (width - text_w) / 2
    y_headline = height * 0.15 # Un poco más abajo (15%)

    # Fondo semitransparente MÁS GRANDE (padding)
    padding = 20
    draw.rectangle(
        [(x_headline - padding, y_headline - padding), (x_headline + text_w + padding, y_headline + text_h + padding)],
        fill=(0, 0, 0, 180) # Negro un poco más oscuro
    )
    draw.text((x_headline, y_headline), headline_texto, font=font_headline, fill=text_color)

    # 4. Dibujar CTA (Abajo)
    bbox_cta = draw.textbbox((0, 0), cta_texto, font=font_cta)
    cta_w = bbox_cta[2] - bbox_cta[0]
    cta_h = bbox_cta[3] - bbox_cta[1]
    
    x_cta = (width - cta_w) / 2
    y_cta = height * 0.85
    
    # Botón Rojo EVO
    padding_cta = 30
    draw.rectangle(
        [(x_cta - padding_cta, y_cta - padding_cta/2), (x_cta + cta_w + padding_cta, y_cta + cta_h + padding_cta/2)],
        fill=(220, 20, 60, 255) # Un rojo más intenso
    )
    draw.text((x_cta, y_cta), cta_texto, font=font_cta, fill=(255, 255, 255))

    return img

# --- INTERFAZ ---

st.write("Ahora descargamos la fuente 'Roboto' de Google para que se vea profesional siempre.")

if st.button("⚡ Generar Tanda V2 (Texto Grande)"):
    
    tandas_para_generar = [
        {
            "fondo": "https://picsum.photos/id/3/1080/1080", # Formato cuadrado HD
            "headline": "ESCALA A $10K USD",
            "cta": "CLASE GRATIS ▶"
        },
        {
            "fondo": "https://picsum.photos/id/180/1080/1080",
            "headline": "STOP ADS BARATOS",
            "cta": "VER ESTRATEGIA"
        }
    ]
    
    col1, col2 = st.columns(2)
    cols = [col1, col2]

    for i, datos in enumerate(tandas_para_generar):
        with cols[i]:
            with st.spinner(f"Diseñando Ad #{i+1}..."):
                imagen_final = crear_anuncio_con_texto(datos["fondo"], datos["headline"], datos["cta"])
                st.image(imagen_final, caption=f"Ad #{i+1}", use_container_width=True)
                st.success("✅ ¡Ahora sí se lee!")
