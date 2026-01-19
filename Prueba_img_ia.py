from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def crear_anuncio_con_texto(url_fondo, headline_texto, cta_texto):
    """
    Toma una URL de imagen de fondo y le estampa un Headline y un CTA.
    """
    print(f"Procesando imagen...")
    
    # 1. Descargar la imagen de fondo (simulando que viene de DALL-E)
    response = requests.get(url_fondo)
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    width, height = img.size

    # 2. Preparar el "Lienzo" para dibujar
    draw = ImageDraw.Draw(img)

    # --- CONFIGURACIÓN DE FUENTES ---
    # NOTA CRÍTICA: Para un look PRO, necesitas un archivo de fuente real (.ttf)
    # Si tienes uno (ej: 'Montserrat-Bold.ttf') ponlo en la misma carpeta y descomenta la línea de abajo:
    # font_headline = ImageFont.truetype("Montserrat-Bold.ttf", size=50)
    # font_cta = ImageFont.truetype("Montserrat-Bold.ttf", size=30)
    
    # Para este demo, usaremos la fuente por defecto (que es fea, pero sirve para probar)
    try:
        # Intenta cargar una fuente de sistema común (Arial en Windows/Linux)
        font_headline = ImageFont.truetype("arial.ttf", 50)
        font_cta = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        # Si falla, usa la fuente por defecto de Python (muy básica)
        print("⚠️ No se encontró arial.ttf, usando fuente por defecto.")
        font_headline = ImageFont.load_default()
        font_cta = ImageFont.load_default()

    # --- DIBUJAR EL HEADLINE (Título Principal) ---
    # Color blanco (255,255,255)
    text_color = (255, 255, 255)
    
    # Opcional: Dibujar una "caja negra" semitransparente detrás del texto para que se lea mejor
    headline_bbox = draw.textbbox((0, 0), headline_texto, font=font_headline)
    text_width = headline_bbox[2] - headline_bbox[0]
    text_height = headline_bbox[3] - headline_bbox[1]
    
    # Calcular posición centrada arriba
    x_headline = (width - text_width) / 2
    y_headline = height * 0.1 # Al 10% de altura

    # Dibujar rectángulo de fondo para el texto (opacidad 150 sobre 255)
    draw.rectangle(
        [(x_headline - 10, y_headline - 10), (x_headline + text_width + 10, y_headline + text_height + 10)],
        fill=(0, 0, 0, 150)
    )
    
    # Dibujar el texto encima
    draw.text((x_headline, y_headline), headline_texto, font=font_headline, fill=text_color)

    # --- DIBUJAR EL CTA (Botón Falso) ---
    cta_bbox = draw.textbbox((0, 0), cta_texto, font=font_cta)
    cta_width = cta_bbox[2] - cta_bbox[0]
    cta_height = cta_bbox[3] - cta_bbox[1]
    
    # Posición centrada abajo
    x_cta = (width - cta_width) / 2
    y_cta = height * 0.8 # Al 80% de altura
    
    # Dibujar un "botón" rojo detrás del CTA
    draw.rectangle(
        [(x_cta - 20, y_cta - 10), (x_cta + cta_width + 20, y_cta + cta_height + 10)],
        fill=(255, 75, 75, 255) # Color rojo EVO
    )
    draw.text((x_cta, y_cta), cta_texto, font=font_cta, fill=(255, 255, 255))

    return img

# =========================================
# SIMULACIÓN DE TU SOFTWARE EN ACCIÓN
# =========================================

# 1. La IA nos da estas URLs de fondo y estos textos:
tandas_para_generar = [
    {
        "fondo": "https://picsum.photos/id/1/800/800", # Imagina que esto lo dio DALL-E
        "headline": "ESCALA TU AGENCIA A $10K",
        "cta": "VER CLASE GRATUITA ▶"
    },
    {
        "fondo": "https://picsum.photos/id/20/800/800",
        "headline": "¿CANSADO DE QUEMAR PRESUPUESTO?",
        "cta": "DESCUBRE EL SISTEMA EVO ▶"
    }
    # Imagina aquí 8 elementos más para completar la tanda de 10
]

print("--- INICIANDO MOTOR GRÁFICO EVO LAUNCH ---")

# 2. El Loop Mágico (Esto irá dentro de tu Streamlit)
for i, datos in enumerate(tandas_para_generar):
    print(f"Generando Ad #{i+1}...")
    imagen_final = crear_anuncio_con_texto(datos["fondo"], datos["headline"], datos["cta"])
    
    # Guardamos el resultado en tu computadora
    nombre_archivo = f"ad_generado_{i+1}.png"
    imagen_final.save(nombre_archivo)
    print(f"✅ {nombre_archivo} guardado con éxito.")

print("--- PROCESO TERMINADO. REVISA LA CARPETA DEL PROYECTO ---")
