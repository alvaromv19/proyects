import streamlit as st
from html2image import Html2Image
import os

# --- 1. CONFIGURACIÓN DE PÁGINA (IMPORTANTE: Debe ir al principio) ---
st.set_page_config(page_title="Generador HTML PRO", page_icon="🎨")
st.title("🎨 Generador de Ads con HTML + CSS")

# --- 2. FUNCIÓN GENERADORA ---
def generar_ad_html(headline, cta, fondo_url, filename):
    hti = Html2Image()
    
    # --- CORRECCIÓN CRÍTICA PARA LOCAL ---
    # Para que funcione en tu PC (VS Code), COMENTA o BORRA esta línea.
    # Solo se usa cuando subas el proyecto a la nube (Linux).
    # hti.browser_executable = "chromium" 
    
    # CSS Moderno con Glassmorphism
    css = """
    body { 
        margin: 0; padding: 0; width: 1080px; height: 1080px; 
        background: url('""" + fondo_url + """') no-repeat center center; 
        background-size: cover;
        display: flex; flex-direction: column; justify-content: flex-end; align-items: center; 
        font-family: 'Helvetica', sans-serif; 
    }
    .card { 
        background: rgba(255, 255, 255, 0.25); 
        backdrop-filter: blur(15px); 
        -webkit-backdrop-filter: blur(15px);
        padding: 50px; 
        border-radius: 40px; 
        text-align: center; 
        margin-bottom: 120px; 
        width: 80%; 
        border: 2px solid rgba(255,255,255,0.4);
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    h1 { 
        color: white; 
        font-size: 70px; 
        text-transform: uppercase; 
        margin: 0 0 30px 0;
        text-shadow: 0 4px 10px rgba(0,0,0,0.5); 
    }
    .btn { 
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%); 
        color: white; 
        padding: 25px 60px; 
        font-size: 45px; 
        border-radius: 100px; 
        display: inline-block; 
        font-weight: bold;
        box-shadow: 0 10px 25px rgba(255, 75, 43, 0.5);
    }
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
    
    # Generar la imagen (1080x1080)
    # output_path devuelve una lista, tomamos el primer elemento [0]
    rutas = hti.screenshot(html_str=html, save_as=filename, size=(1080, 1080))
    return rutas[0] 

# --- 3. INTERFAZ Y BOTÓN ---
st.write("Prueba de renderizado usando el motor de tu navegador (Chrome/Edge).")

col1, col2 = st.columns(2)

with col1:
    txt_titulo = st.text_input("Titular", "DOMINA LA IA")
    txt_cta = st.text_input("Botón", "CLASE GRATIS")

with col2:
    # Usamos una imagen real de Unsplash para probar
    url_fondo = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1080&auto=format&fit=crop"
    st.image(url_fondo, caption="Fondo de prueba", width=150)

if st.button("✨ Generar Imagen PRO"):
    with st.spinner("Renderizando HTML a Imagen... (Esto usa tu Chrome en segundo plano)"):
        try:
            archivo_final = "ad_generado_temp.png"
            
            # Llamamos a la función
            ruta_imagen = generar_ad_html(txt_titulo, txt_cta, url_fondo, archivo_final)
            
            # Mostramos el resultado
            st.success("¡Imagen generada con éxito!")
            st.image(ruta_imagen, caption="Diseño Final HTML+CSS", use_container_width=True)
            
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")
            st.info("Asegúrate de tener Google Chrome o Microsoft Edge instalados en esta PC.")
