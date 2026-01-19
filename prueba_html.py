from html2image import Html2Image
import os

# Inicializamos el "Fotógrafo"
hti = Html2Image()

def generar_ad_pro(headline, cta, fondo_url, nombre_archivo):
    
    # --- AQUÍ ESTÁ LA MAGIA: DISEÑO WEB PURO (HTML + CSS) ---
    # Fíjate cómo uso CSS moderno: Flexbox, Backdrop Filter, Shadows
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;800&display=swap" rel="stylesheet">
        <style>
            body {{
                margin: 0;
                padding: 0;
                width: 1080px;
                height: 1080px;
                background: url('{fondo_url}') no-repeat center center;
                background-size: cover;
                font-family: 'Montserrat', sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: flex-end; /* Todo el contenido abajo */
                align-items: center;
                padding-bottom: 150px; /* Espacio desde abajo */
                box-sizing: border-box;
            }}

            /* TARJETA CON EFECTO VIDRIO (GLASSMORPHISM) */
            .glass-card {{
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(20px); /* El efecto borroso detrás */
                -webkit-backdrop-filter: blur(20px);
                border-radius: 40px;
                border: 2px solid rgba(255, 255, 255, 0.3);
                padding: 60px;
                width: 80%;
                text-align: center;
                box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            }}

            h1 {{
                color: white;
                font-size: 75px;
                font-weight: 800;
                margin: 0 0 40px 0;
                text-transform: uppercase;
                line-height: 1.1;
                text-shadow: 0 5px 15px rgba(0,0,0,0.3);
            }}

            .cta-button {{
                background: linear-gradient(135deg, #FF4B4B 0%, #FF9068 100%); /* Gradiente PRO */
                color: white;
                font-size: 40px;
                font-weight: 800;
                padding: 25px 60px;
                border-radius: 100px;
                display: inline-block;
                box-shadow: 0 10px 30px rgba(255, 75, 75, 0.6);
                text-transform: uppercase;
                letter-spacing: 2px;
            }}
            
            /* Etiqueta flotante superior */
            .badge {{
                position: absolute;
                top: 60px;
                right: 60px;
                background: #00C853;
                color: white;
                padding: 15px 30px;
                border-radius: 20px;
                font-size: 30px;
                font-weight: bold;
                box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            }}
        </style>
    </head>
    <body>
        <div class="badge">NUEVO</div>
        
        <div class="glass-card">
            <h1>{headline}</h1>
            <div class="cta-button">{cta}</div>
        </div>
    </body>
    </html>
    """

    # --- RENDERIZAR: TOMAR LA FOTO ---
    print(f"📸 Generando diseño PRO: {nombre_archivo}...")
    
    # Renderizamos el HTML a un archivo PNG de 1080x1080
    hti.screenshot(
        html_str=html_template, 
        save_as=nombre_archivo, 
        size=(1080, 1080)
    )

# --- EJECUCIÓN ---
datos_ads = [
    {
        "headline": "Domina la IA en 30 Días", 
        "cta": "Acceso Beta", 
        "fondo": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1080&auto=format&fit=crop"
    },
    {
        "headline": "Tu Agencia al Siguiente Nivel", 
        "cta": "Clase Gratis", 
        "fondo": "https://images.unsplash.com/photo-1557804506-669a67965ba0?q=80&w=1080&auto=format&fit=crop"
    }
]

for i, ad in enumerate(datos_ads):
    generar_ad_pro(ad["headline"], ad["cta"], ad["fondo"], f"ad_html_{i+1}.png")

print("✅ ¡Listo! Revisa las imágenes generadas (ad_html_X.png).")
