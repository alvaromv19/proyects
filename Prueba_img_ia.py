import streamlit as st
from html2image import Html2Image
import os

# ... (resto de tu configuración de página) ...

# --- FUNCIÓN GENERADORA PRO (HTML) ---
def generar_ad_html(headline, cta, fondo_url, filename):
    hti = Html2Image()
    
    # Ajustes para que funcione en Nube (Linux) y Local (Windows/Mac)
    # Estas flags son necesarias para servidores sin pantalla gráfica
    hti.browser_executable = "chromium" # Opcional: ajustar según entorno
    
    css = """
    body { margin: 0; padding: 0; width: 1080px; height: 1080px; 
           background: url('""" + fondo_url + """') no-repeat center center; background-size: cover;
           display: flex; flex-direction: column; justify-content: flex-end; align-items: center; 
           font-family: sans-serif; }
    .card { background: rgba(255,255,255,0.2); backdrop-filter: blur(10px); 
            padding: 40px; border-radius: 20px; text-align: center; margin-bottom: 100px; width: 80%; }
    h1 { color: white; font-size: 60px; text-transform: uppercase; text-shadow: 2px 2px 4px #000; }
    .btn { background: #ff4b4b; color: white; padding: 20px 50px; font-size: 40px; 
           border-radius: 50px; display: inline-block; margin-top: 20px; font-weight: bold;}
    """
    
    html = f"""
    <html>
    <style>{css}</style>
    <body>
        <div class="card">
            <h1>{headline}</h1>
            <div class="btn">{cta}</div>
        </div>
    </body>
    </html>
    """
    
    # Generar
    output_path = hti.screenshot(html_str=html, save_as=filename, size=(1080, 1080))
    return output_path[0] # Retorna la ruta del archivo generado

# ... (luego en tu botón de Streamlit) ...
if st.button("Generar con HTML"):
    img_path = generar_ad_html("TITULO PRO", "COMPRAR", "https://...", "temp_ad.png")
    st.image(img_path) # Streamlit lee el archivo generado
