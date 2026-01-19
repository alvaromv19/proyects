import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Test Motor Gráfico EVO", page_icon="🎨")
st.title("🎨 Prueba de Motor Gráfico: Texto sobre Imagen")

# --- FUNCIÓN DEL MOTOR GRÁFICO (El Cerebro) ---
def crear_anuncio_con_texto(url_fondo, headline_texto, cta_texto):
    """
    Toma una URL, descarga la imagen y le estampa texto.
    """
    # 1. Descargar imagen
    response = requests.get(url_fondo)
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    width, height = img.size
    draw = ImageDraw.Draw(img)

    # 2. Configuración de Fuentes (Fallback a default si no hay Arial)
    try:
        font_headline = ImageFont.truetype("arial.ttf", 50)
        font_cta = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font_headline = ImageFont.load_default()
        font_cta = ImageFont.load_default()

    # 3. Dibujar Headline (Arriba)
    text_color = (255, 255, 255)
    headline_bbox = draw.textbbox((0, 0), headline_texto, font=font_headline)
    text_width = headline_bbox[2] - headline_bbox[0]
    text_height = headline_bbox[3] - headline_bbox[1]
    
    x_headline = (width - text_width) / 2
    y_headline = height * 0.1 

    # Fondo semitransparente para el título
    draw.rectangle(
        [(x_headline - 10, y_headline - 10), (x_headline + text_width + 10, y_headline + text_height + 10)],
        fill=(0, 0, 0, 150)
    )
    draw.text((x_headline, y_headline), headline_texto, font=font_headline, fill=text_color)

    # 4. Dibujar CTA (Abajo)
    cta_bbox = draw.textbbox((0, 0), cta_texto, font=font_cta)
    cta_width = cta_bbox[2] - cta_bbox[0]
    cta_height = cta_bbox[3] - cta_bbox[1]
    
    x_cta = (width - cta_width) / 2
    y_cta = height * 0.8
    
    # Botón Rojo EVO
    draw.rectangle(
        [(x_cta - 20, y_cta - 10), (x_cta + cta_width + 20, y_cta + cta_height + 10)],
        fill=(255, 75, 75, 255) 
    )
    draw.text((x_cta, y_cta), cta_texto, font=font_cta, fill=(255, 255, 255))

    return img

# --- INTERFAZ DE USUARIO (Lo que ves en pantalla) ---

st.write("Este script simula que DALL-E generó imágenes de fondo y Python les coloca el Copy encima.")

if st.button("⚡ Generar Tanda de Prueba"):
    
    # Datos simulados (como si vinieran de GPT-4)
    tandas_para_generar = [
        {
            "fondo": "https://picsum.photos/id/1/800/800",
            "headline": "ESCALA TU AGENCIA A $10K",
            "cta": "VER CLASE GRATUITA ▶"
        },
        {
            "fondo": "https://picsum.photos/id/20/800/800",
            "headline": "¿QUEMANDO PRESUPUESTO?",
            "cta": "DESCUBRE EL SISTEMA EVO ▶"
        },
        {
            "fondo": "https://picsum.photos/id/180/800/800",
            "headline": "METODOLOGÍA HIGH-TICKET",
            "cta": "AGENDA TU LLAMADA"
        }
    ]
    
    # Creamos columnas para mostrar resultados
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]

    for i, datos in enumerate(tandas_para_generar):
        with cols[i]:
            st.info(f"Procesando Ad #{i+1}...")
            
            # LLAMADA AL MOTOR GRÁFICO
            imagen_final = crear_anuncio_con_texto(datos["fondo"], datos["headline"], datos["cta"])
            
            # MOSTRAR EN PANTALLA
            st.image(imagen_final, caption=f"Ad #{i+1} Generado", use_container_width=True)
            st.success("✅ ¡Texto Estampado!")
