
import streamlit as st
from streamlit_option_menu import option_menu
import math


# Konfigurasi halaman
st.set_page_config(page_title="Smart Kalkulator pH", layout="centered")

# CSS styling
st.markdown("""
    <style>
    body, .stApp {
        background-color: #537895;
            
        color: white;
    }

    h1, h2, h3, h4, h5, h6, p, label, .stTextInput, .stSelectbox, .stNumberInput, .stMarkdown, .stButton, .stRadio > div {
        color: white !important;
    }

    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
    }

    .stSidebar {
        background-color: black !important;
    }

    section[data-testid="stSidebar"] .stRadio label {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Navigasi Sidebar
selected = st.sidebar.radio("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi", "📞Kotak Saran dan Kritik"])

# ========== BERANDA ==========
if selected == "Beranda":
    st.title("Selamat Datang di Smart Kalkulator pH")
    st.markdown("""
        <div style="text-align: center;">
            <img src="https://cdn.pixabay.com/photo/2013/07/13/13/48/chemistry-161575_640.png" width="250">
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    📖 *Teori Asam dan Basa*

    *Arrhenius*  
    - Asam: Melepaskan ion H⁺ dalam air  
    - Basa: Melepaskan ion OH⁻

    *Bronsted-Lowry*  
    - Asam: Donor proton (H⁺)  
    - Basa: Akseptor proton

    *Lewis*  
    - Asam: Akseptor pasangan elektron  
    - Basa: Donor pasangan elektron
    """)

    st.markdown("""
    ### Dibuat Oleh:
    - Amar Evan Gading (2460321)
    - Diandra Namira Zahfa (2460360)
    - Lutfhia Salwani Fatonah (2460410)
    - Nevi Sahara (2460471)
    - Taufan Aliafi (2460525)
    """)

# ========== HITUNG pH ==========
elif selected == "Hitung pH":
    st.header("🧪 Kalkulator pH Larutan")

    jenis = option_menu(
        None, ["Asam", "Basa"],
        icons=["droplet", "beaker"],
        orientation="horizontal"
    )

    hasil = ""
    penjelasan = ""
    ph = None

    # ============================
    # ==== BAGIAN ASAM ==========
    # ============================
    if jenis == "Asam":
        tipe = st.radio("Pilih Jenis Asam:", ["Asam Kuat", "Asam Lemah", "Custom"])

        if tipe == "Asam Kuat":
            asam_kuat = {
                "Asam Klorida (HCl)": 1,
        "Asam Nitrat (HNO3)": 1,
        "Asam Sulfat (H2SO4)": 2,            
        "Asam Bromida (HBr)": 1,
        "Asam Bromit (HBrO3)": 1,
        "Asam Perbromat (HBrO4)": 1,
        "Asam Klorat (HClO3)": 1,             
        "Asam Perklorat (HClO4)": 1,
        "Asam Iodida (HI)": 1,
        "Asam Iodit (HIO3)": 1,
        "Asam Periodat (HIO4)": 1,
            }

            senyawa = st.selectbox("Pilih senyawa asam kuat:", list(asam_kuat.keys()))
            valensi = asam_kuat[senyawa]
            st.write(f"Valensi ion H⁺: {valensi}")

            konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, step=0.0001, format="%.4f")

            if st.button("Hitung pH"):
                h = konsentrasi * valensi
                ph = -math.log10(h)
                penjelasan = f"Asam kuat {senyawa} terionisasi sempurna. [H⁺] = konsentrasi × valensi"

        elif tipe == "Asam Lemah":
            asam_lemah = {
                "Asam Asetat (CH3COOH)": 1,
            "Asam Format (HCOOH)": 1,
            "Asam Oksalat (H2C2O4)": 2,
            "Asam Tartarat (H2C4H4O6)": 2, 
            "Asam Sitrat (H3C6H5O7)": 3, 
            "Asam Sianida (HCN)": 1, 
            "Asam Sulfit (H2SO3)": 2,
            }

            senyawa = st.selectbox("Pilih senyawa asam lemah:", list(asam_lemah.keys()))
            valensi = asam_lemah[senyawa]
            st.write(f"Valensi ion H⁺: {valensi}")

            ka = st.number_input("Masukkan konstanta asam (Ka)", min_value=0.0, format="%.2e")
            konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, step=0.0001, format="%.4f")

            if st.button("Hitung pH"):
                h = math.sqrt(valensi * ka * konsentrasi)
                ph = -math.log10(h)
                penjelasan = f"Asam lemah {senyawa}, rumus pH = -log(√(a × Ka × [HA]))"

        elif tipe == "Custom":
            valensi = st.number_input("Masukkan valensi (a)", min_value=1, step=1)
            ka = st.number_input("Masukkan Ka", min_value=0.0, format="%.2e")
            konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, step=0.0001, format="%.4f")

            if st.button("Hitung pH"):
                h = math.sqrt(valensi * ka * konsentrasi)
                ph = -math.log10(h)
                penjelasan = f"Asam lemah custom, pH = -log(√(a × Ka × [HA]))"

    # ============================
    # ==== BAGIAN BASA ==========
    # ============================
    elif jenis == "Basa":
        tipe = st.radio("Pilih Jenis Basa:", ["Basa Kuat", "Basa Lemah", "Custom"])

        if tipe == "Basa Kuat":
            basa_kuat = {
                "Natrium Hidroksida (NaOH)": 1,
            "Litium Hidroksida (LiOH)": 1,
            "Kalium Hidroksida (KOH)": 1,
            "Rubidium Hidroksida (RbOH)": 1,
            "Cesium Hidroksida (CsOH)": 1,
            "Kalsium Hidroksida (Ca(OH)2)": 2,
            "Barium Hidroksida (Ba(OH)2)": 2,
            "Stronsium Hidroksida (Sr(OH)2)": 2,
            "Magnesium Hidroksida (Mg(OH)2)": 2
        }

            senyawa = st.selectbox("Pilih senyawa basa kuat:", list(basa_kuat.keys()))
            valensi = basa_kuat[senyawa]
            st.write(f"Valensi ion OH⁻: {valensi}")

            konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, step=0.0001, format="%.4f")

            if st.button("Hitung pH"):
                oh = konsentrasi * valensi
                poh = -math.log10(oh)
                ph = 14 - poh
                penjelasan = f"Basa kuat {senyawa} terionisasi sempurna. [OH⁻] = konsentrasi × valensi"

        elif tipe == "Basa Lemah":
            basa_lemah = {
            "Amonia (NH3)": 1,
            "Metilamina (CH3NH2)": 1,
            "Etilamina (C2H5NH2)": 1,
            "Propilamina (C3H7NH2)": 1,
            "Butilamina (C4H9NH2)": 1,
            "Anilina (C6H5NH2)": 1,
            "Hidrazina (N2H4)": 2,
            "Etilendiamina (C2H4(NH2)2)": 2,
        }
            senyawa = st.selectbox("Pilih senyawa basa lemah:", list(basa_lemah.keys()))
            valensi = basa_lemah[senyawa]
            st.write(f"Valensi ion OH⁻: {valensi}")

            kb = st.number_input("Masukkan konstanta basa (Kb)", min_value=0.0, format="%.2e")
            konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, step=0.0001, format="%.4f")

            if st.button("Hitung pH"):
                oh = math.sqrt(valensi * kb * konsentrasi)
                poh = -math.log10(oh)
                ph = 14 - poh
                penjelasan = f"Basa lemah {senyawa}, pH = 14 - log(√(a × Kb × [B]))"

        elif tipe == "Custom":
            valensi = st.number_input("Masukkan valensi (a)", min_value=1, step=1)
            kb = st.number_input("Masukkan Kb", min_value=0.0, format="%.2e")
            konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, step=0.0001, format="%.4f")

            if st.button("Hitung pH"):
                oh = math.sqrt(valensi * kb * konsentrasi)
                poh = -math.log10(oh)
                ph = 14 - poh
                penjelasan = f"Basa lemah custom, pH = 14 - log(√(a × Kb × [B]))"

    # ============================
    # ==== HASIL PH DITAMPILKAN
    # ============================
    try:
        if ph is not None:
         st.success(f"Hasil pH: {ph:.2f}")
        st.info(penjelasan)
    # Tampilkan hasil
        if ph is not None:
            st.success(f"Hasil pH: {ph:.2f}")
        st.info(penjelasan)
    except Exception as e:
        st.error("Terjadi kesalahan perhitungan. Pastikan data valid.")

# ========== TENTANG APLIKASI ==========
elif selected == "Tentang Aplikasi":
    st.header("📘 Tentang Aplikasi")
    st.markdown("""
    ### 1. Apa itu pH?  
    pH adalah ukuran konsentrasi ion hidrogen (H⁺) dalam larutan.  
    Skala pH:
    - pH < 7 : Asam  
    - pH = 7 : Netral  
    - pH > 7 : Basa  

    ### 2. Rumus pH:
    - Asam Kuat : pH = -log[H⁺]
    - Basa Kuat : pH = 14 - log[OH⁻]
    - Asam Lemah : pH = -log(√(Ka × [HA]))
    - Basa Lemah : pH = 14 - log(√(Kb × [B]))
    """)

# ========== KOTAK SARAN ==========
elif selected == "📞Kotak Saran dan Kritik":
    st.header("📨 Kotak Saran dan Kritik")
    st.markdown("Silahkan tinggalkan pesan Anda di bawah ini:")

    contact_form = """
        <form action="https://formsubmit.co/nevisahara2006@gmail.com" method="POST">
            <input type="email" name="email" placeholder="Email Anda" required><br>
            <textarea name="message" placeholder="Pesan Anda" rows="5" required></textarea><br>
            <button type="submit">Kirim</button>
        </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)