import streamlit as st
import pandas as pd
import time
import random
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="EVO LAUNCH | AI Ad Manager",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PERSONALIZADOS (Para darle look "Pro") ---
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
    }
    .ad-preview {
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CONFIGURACIÓN Y CUENTAS ---
with st.sidebar:
    st.title("⚙️ Configuración")
    st.subheader("Credenciales")
    openai_key = st.text_input("OpenAI API Key", type="password", help="Tu llave para GPT-4 y DALL-E")
    meta_token = st.text_input("Meta Access Token", type="password", help="Token de Graph API")
    
    st.divider()
    
    st.subheader("Selección de Cuenta")
    ad_account = st.selectbox(
        "Cuenta Publicitaria",
        ["Seleccionar...", "Activos Tino Mossu (ID: 99281...)", "EVO Launch Sandbox (ID: 1123...)"]
    )
    
    page_fb = st.selectbox("Fan Page", ["Tino Mossu Oficial", "EVO Launch Agency"])
    ig_account = st.selectbox("Instagram", ["@tinomossu", "@evolaunch"])
    
    st.info(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d')}")

# --- TÍTULO PRINCIPAL ---
st.title("🚀 EVO LAUNCH - AI Media Buyer")
st.markdown("**Workflow:** Ingesta -> Creativos IA -> Configuración 1-1-1 -> Lanzamiento -> Optimización")

# --- GESTIÓN DE ESTADO (SESSION STATE) ---
if 'creativos_generados' not in st.session_state:
    st.session_state.creativos_generados = []

# --- PESTAÑAS DEL WORKFLOW ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🧠 1. Estrategia e Ingesta", 
    "🎨 2. Laboratorio Creativo", 
    "🛠️ 3. Configuración Trafficker",
    "📊 4. Dashboard & Reglas"
])

# ==========================================
# TAB 1: ESTRATEGIA (EL CEREBRO)
# ==========================================
with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📥 Input de Datos")
        uploaded_file = st.file_uploader("Sube investigaciones (PDF/TXT)", type=['txt', 'pdf', 'docx'])
        product_promise = st.text_area("Promesa / Oferta Irresistible", placeholder="Ej: Ayudo a escalar a $10k en 90 días...")
        target_audience = st.text_area("Detalles del Avatar", placeholder="Dolores, deseos, objeciones...")
        
    with col2:
        st.subheader("🤖 Análisis de IA")
        if st.button("Analizar Datos y Generar Ángulos"):
            if not product_promise:
                st.warning("Por favor ingresa al menos la promesa del producto.")
            else:
                with st.spinner('La IA está leyendo tus documentos y analizando el mercado...'):
                    time.sleep(2) # Simulación de tiempo de carga
                    st.success("¡Análisis Completado!")
                    
                    st.markdown("""
                    **Estrategia Recomendada por IA:**
                    * **Ángulo 1 (Dolor):** "Estás cansado de quemar dinero en Ads sin retorno..."
                    * **Ángulo 2 (Aspiracional):** "Imagina tu agencia facturando $10k consistentemente..."
                    * **Formato Sugerido:** Imagen estática con headline fuerte + Copy largo storytelling.
                    """)
                    st.info("La IA ha detectado 3 objeciones principales para atacar en los creativos.")

# ==========================================
# TAB 2: CREATIVOS (LA FÁBRICA)
# ==========================================
with tab2:
    st.subheader("Generación de Activos (DALL-E 3 + GPT-4o)")
    
    c_col1, c_col2 = st.columns([1,3])
    with c_col1:
        qty = st.slider("Cantidad de Variaciones", 1, 4, 2)
        visual_style = st.selectbox("Estilo Visual", ["Fotorealista", "Minimalista 3D", "Ilustración Vectorial", "UGC Style"])
        if st.button("✨ Generar Creativos"):
            with st.spinner(f'Generando {qty} variaciones de imagen y copy...'):
                time.sleep(3) # Simulación
                # MOCK DATA: Generamos datos falsos para el demo
                st.session_state.creativos_generados = [
                    {
                        "id": 1,
                        "img": "https://picsum.photos/400/400?random=1",
                        "primary": "🔥 Deja de perseguir clientes. Haz que ellos vengan a ti con este sistema de Funnels High-Ticket.",
                        "headline": "Clase Gratuita: Sistema de Atracción",
                        "desc": "Regístrate ahora 👇"
                    },
                    {
                        "id": 2,
                        "img": "https://picsum.photos/400/400?random=2",
                        "primary": "⚠️ Advertencia: No lances tu próxima campaña sin ver esto. El ROAS de 3.5x es posible si cambias esto...",
                        "headline": "El secreto del ROAS estable",
                        "desc": "Ver entrenamiento de 10 min"
                    }
                ]
                if qty > 2: # Solo agregamos más si pide más
                     st.session_state.creativos_generados.append({
                        "id": 3,
                        "img": "https://picsum.photos/400/400?random=3",
                        "primary": "¿Tu agencia está estancada? Descubre cómo EVO LAUNCH escala ofertas.",
                        "headline": "Escala tu Agencia hoy",
                        "desc": "Cupos limitados"
                     })
    
    with c_col2:
        if st.session_state.creativos_generados:
            st.write("### Vista Previa de Anuncios")
            cols = st.columns(len(st.session_state.creativos_generados))
            
            selected_ads = []
            
            for idx, ad in enumerate(st.session_state.creativos_generados):
                with cols[idx]:
                    st.markdown(f"<div class='ad-preview'>", unsafe_allow_html=True)
                    st.image(ad['img'], use_container_width=True)
                    new_primary = st.text_area(f"Primary Text {idx+1}", value=ad['primary'], height=100)
                    new_head = st.text_input(f"Headline {idx+1}", value=ad['headline'])
                    is_selected = st.checkbox(f"✅ Aprobar Ad {idx+1}", value=True, key=f"ad_{idx}")
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    if is_selected:
                        selected_ads.append(idx)

# ==========================================
# TAB 3: LANZAMIENTO (TRAFFICKER MODE)
# ==========================================
with tab3:
    st.header("Configuración de Campaña (Estructura 1-1-1)")
    
    l_col1, l_col2, l_col3 = st.columns(3)
    
    with l_col1:
        st.subheader("1. Segmentación Broad")
        geo = st.multiselect("Países", ["Peru", "USA", "Argentina", "Colombia"], default=["Peru"])
        age_min, age_max = st.slider("Rango de Edad", 18, 65, (22, 55))
        gender = st.radio("Género", ["Todos", "Hombres", "Mujeres"], horizontal=True)
        
    with l_col2:
        st.subheader("2. Presupuesto y Pixel")
        budget = st.number_input("Budget Diario (USD) por AdSet", value=10.0, step=5.0)
        pixel_id = st.text_input("Pixel ID", value="1283928392...")
        conversion_event = st.selectbox("Evento", ["Comprar", "Lead", "CompleteRegistration"])
        
    with l_col3:
        st.subheader("3. Nomenclatura EVO")
        st.markdown("*Define las variables para nombrar automáticamente*")
        tanda = st.text_input("Tanda (T)", value="T01")
        script = st.text_input("Script (SC)", value="SC_Dolor")
        trigger = st.text_input("Trigger (TG)", value="TG_Video")
        opening = st.text_input("Opening Scene (OS)", value="OS_Gancho")
        
        # Generador de nombre en tiempo real
        campaign_name = f"CONV | BROAD | {tanda} | {script}"
        adset_name = f"BROAD | {age_min}-{age_max} | {geo[0] if geo else 'Global'}"
        ad_name = f"{tanda}-{script}-{trigger}-{opening}"
        
        st.info(f"📝 **Preview Nombre Ad:** {ad_name}")

    st.divider()
    
    launch_state = st.radio("Estado Inicial", ["PAUSED (Recomendado)", "ACTIVE"], horizontal=True)
    
    if st.button("🚀 LANZAR CAMPAÑAS A META", type="primary"):
        if not ad_account or ad_account == "Seleccionar...":
            st.error("❌ Selecciona una cuenta publicitaria en el Sidebar primero.")
        else:
            progress_text = "Conectando con Graph API..."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.05)
                if percent_complete == 20: my_bar.progress(percent_complete + 1, text="Subiendo imágenes al Ad Library...")
                if percent_complete == 50: my_bar.progress(percent_complete + 1, text=f"Creando Estructura 1-1-1 ({len(st.session_state.creativos_generados)} campañas)...")
                if percent_complete == 80: my_bar.progress(percent_complete + 1, text="Aplicando Nomenclaturas y UTMs...")
                my_bar.progress(percent_complete + 1)
            
            st.balloons()
            st.success(f"✅ ¡ÉXITO! Se han creado {len(st.session_state.creativos_generados)} campañas en modo {launch_state}.")
            st.json({
                "Campaña 1": {"ID": "2384992...", "Nombre": campaign_name, "Estado": launch_state},
                "Campaña 2": {"ID": "2384993...", "Nombre": campaign_name, "Estado": launch_state}
            })

# ==========================================
# TAB 4: ANALYTICS (RULES ENGINE)
# ==========================================
with tab4:
    st.header("Optimizador Basado en Reglas")
    
    # Simulación de Datos
    data = {
        'Campaña': ['T01-SC01-TG01', 'T01-SC02-TG01', 'T01-SC03-TG02', 'T02-SC01-TG01'],
        'Spend': [150.0, 45.0, 320.0, 12.0],
        'ROAS': [4.2, 0.8, 1.4, 0.0],
        'CPR': [5.5, 25.0, 12.0, 0.0],
        'Status': ['ACTIVE', 'ACTIVE', 'ACTIVE', 'ACTIVE']
    }
    df = pd.DataFrame(data)
    
    # Definir Reglas (Visuales)
    col_rule1, col_rule2 = st.columns(2)
    with col_rule1:
        st.markdown("#### 📏 Reglas de Apagado")
        st.code("IF ROAS < 1.0 AND Spend > $40 THEN: PAUSE")
    with col_rule2:
        st.markdown("#### 🚀 Reglas de Escala")
        st.code("IF ROAS > 3.0 THEN: INCREASE BUDGET 20%")

    st.divider()
    
    st.subheader("Análisis en Tiempo Real")
    
    # Aplicar lógica mock
    def get_action(row):
        if row['ROAS'] < 1.0 and row['Spend'] > 40:
            return "🛑 APAGAR"
        elif row['ROAS'] > 3.0:
            return "📈 ESCALAR (+20%)"
        else:
            return "👀 VIGILAR"

    df['IA Suggestion'] = df.apply(get_action, axis=1)
    
    # Mostrar tabla con colores
    st.dataframe(df.style.map(lambda x: 'color: red' if x == "🛑 APAGAR" else ('color: green' if "ESCALAR" in str(x) else ''), subset=['IA Suggestion']), use_container_width=True)
    
    if st.button("🤖 Aplicar Cambios Sugeridos Automáticamente"):
        st.toast("Optimizaciones enviadas a Meta API...", icon="✅")
