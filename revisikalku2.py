import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Smart Kalkulator pH", layout="centered")

# CSS Styling
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
    </style>
""", unsafe_allow_html=True)

# Navigasi Sidebar
menu = st.sidebar.radio("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi", "Kotak Saran dan Kritik"])

# =================== BERANDA ======================
if menu == "Beranda":
    st.title("Selamat Datang di Smart Kalkulator pH")
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn.pixabay.com/photo/2013/07/13/13/48/chemistry-161575_640.png" 
                 alt="Ilustrasi Kimia" 
                 width="250">
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown("""
    ### Teori Asam Basa
    📖 Teori Arrhenius
- Asam adalah zat yang dapat melepaskan ion H+ dalam larutan air.
- Basa adalah zat yang dapat melepaskan ion OH- dalam larutan air.

📖Teori Bronsted-Lowry
- Asam adalah zat yang dapat melepaskan proton (H+).
- Basa adalah zat yang dapat menerima proton (H+).

📖 Teori Lewis
- Asam adalah zat yang dapat menerima pasangan elektron.
- Basa adalah zat yang dapat memberikan pasangan elektron.
    """)
    st.markdown("""
    ### Dibuat Oleh:
    - Amar Evan Gading (2460321)
    - Diandra Namira Zahfa (2460360)
    - Lutfhia Salwani Fatonah (2460410)
    - Nevi Sahara (2460471)
    - Taufan Aliafi (2460525)
    """)

# ================== HITUNG PH ======================
elif menu == "Hitung pH":
    st.header("🧪 Kalkulator pH Larutan")

    jenis = st.radio("Pilih Jenis Larutan", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah", "Custom"])
    konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, max_value=14.0, step=0.0001, format="%.4f")

    konstanta = 0.0
    valensi = 1

    if jenis in ["Asam Lemah", "Basa Lemah", "Custom"]:
        konstanta = st.number_input(f"Masukkan {'Ka' if 'Asam' in jenis else 'Kb'}", min_value=0.0, step=1e-8, format="%.2e")

    if jenis == "Custom":
        valensi = st.number_input("Masukkan valensi (a)", min_value=1, step=1)

    if st.button("Hitung pH"):
        try:
            if jenis == "Asam Kuat":
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
                h = konsentrasi * valensi
                ph = -math.log10(h)
                st.success(f"pH = {ph:.2f}")
                st.info("Asam kuat terionisasi sempurna, sehingga [H⁺] = konsentrasi.")

            elif jenis == "Asam Lemah":
                 asam_lemah = {
        "Asam Asetat (CH3COOH)": 1,
        "Asam Format (HCOOH)": 1,
        "Asam Oksalat (H2C2O4)": 2,
        "Asam Tartarat (H2C4H4O6)": 2, 
        "Asam Sitrat (H3C6H5O7)": 3, 
        "Asam Sianida (HCN)": 1, 
        "Asam Sulfit (H2SO3)": 2,
        "Asam Benzoat (C6H5COOH)": 1,
        "Asam Laktat (C3H6O3)": 1,
    }
                h = math.sqrt(konstanta * konsentrasi)
                ph = -math.log10(h)
                st.success(f"pH = {ph:.2f}")
                st.info("Asam lemah: pH = -log(√(Ka × [HA]))")

            elif jenis == "Basa Kuat":
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
                oh = konsentrasi * valensi
                poh = -math.log10(oh)
                ph = 14 - poh
                st.success(f"pH = {ph:.2f}")
                st.info("Basa kuat: pH = 14 - log [OH⁻]")

            elif jenis == "Basa Lemah":
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
                oh = math.sqrt(konstanta * konsentrasi)
                poh = -math.log10(oh)
                ph = 14 - poh
                st.success(f"pH = {ph:.2f}")
                st.info("Basa lemah: pH = 14 - log(√(Kb × [B]))")

            elif jenis == "Custom":
                if konstanta == 0:
                    st.error("Ka atau Kb tidak boleh nol.")
                else:
                    if "Asam" in jenis:
                        h = math.sqrt(konstanta * konsentrasi * valensi)
                        ph = -math.log10(h)
                        st.success(f"pH = {ph:.2f}")
                    else:
                        oh = math.sqrt(konstanta * konsentrasi * valensi)
                        poh = -math.log10(oh)
                        ph = 14 - poh
                        st.success(f"pH = {ph:.2f}")
        except:
            st.error("Terjadi kesalahan dalam perhitungan. Cek input Anda.")

# =============== TENTANG APLIKASI ===================
elif menu == "Tentang Aplikasi":
    st.header("📘 Tentang Aplikasi")
    st.markdown("""
    ### Apa itu pH?
    pH adalah ukuran konsentrasi ion hidrogen (H⁺) dalam larutan:
    - pH < 7 : Asam
    - pH = 7 : Netral
    - pH > 7 : Basa

    ### Rumus pH:
    - Asam Kuat: pH = -log [H⁺]
    - Basa Kuat: pH = 14 - log [OH⁻]
    - Asam Lemah: pH = -log(√(Ka × [HA]))
    - Basa Lemah: pH = 14 - log(√(Kb × [B]))

    ### 💡 Contoh Soal:
    1. HCl 0.01 M → pH = -log(0.01) = 2.00  
    2. NH₃ 0.1 M, Kb = 1.8×10⁻⁵  
       → pOH = -log(√(1.8e-5 × 0.1)) ≈ 2.87  
       → pH = 14 - 2.87 = 11.13
    """)

# =============== KOTAK SARAN ========================
elif menu == "Kotak Saran dan Kritik":
    st.header("📩 Kotak Saran dan Kritik")
    st.markdown("Silakan tinggalkan saran atau pesan Anda melalui form berikut:")

    st.markdown("""
        <form action="https://formsubmit.co/nevisahara2006@gmail.com" method="POST">
            <input type="email" name="email" placeholder="Email Anda" required style="width: 100%; padding: 8px;"><br><br>
            <textarea name="message" placeholder="Pesan Anda" rows="5" style="width: 100%; padding: 8px;"></textarea><br><br>
            <button type="submit" style="padding: 10px 20px; background-color: #1e3a8a; color: white; border: none;">Kirim</button>
        </form>
    """, unsafe_allow_html=True)