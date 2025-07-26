import streamlit as st
import math

# Konfigurasi halaman
st.set_page_config(page_title="Smart Kalkulator pH", layout="centered")

# Tema warna biru dengan font putih dan navigasi hitam
st.markdown("""
    <style>
    /* Ubah warna latar belakang utama */
    body, .stApp {
        background-color: #537895;
        color: white;
    }

    /* Ubah semua teks termasuk heading dan input */
    h1, h2, h3, h4, h5, h6, p, label, .stTextInput, .stSelectbox, .stNumberInput, .stMarkdown, .stButton, .stRadio > div {
        color: white !important;
    }

    /* Styling tombol */
    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
    }

    /* Styling khusus sidebar */
    .stSidebar {
        background-color: black !important;
    }

    /* Warna font pada radio (navigasi sidebar) */
    section[data-testid="stSidebar"] .stRadio label {
        color: black !important;
    }

    /* Optional: Ubah warna teks judul sidebar jika ada */
    section[data-testid="stSidebar"] .css-1cypcdb {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar Navigasi
menu = st.sidebar.radio("Navigasi", ["Beranda", "Hitung pH", "Tentang Aplikasi"])

if menu == "Beranda":
    st.title("Selamat Datang di Smart Kalkulator pH")

    # Menampilkan gambar dengan ukuran custom (HTML)
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn.pixabay.com/photo/2013/07/13/13/48/chemistry-161575_640.png" 
                 alt="Ilustrasi Kimia" 
                 width="250">
        </div>
        """,
        unsafe_allow_html=True
    )
    # Informasi Asam Basa
    st.markdown("""
📖 Teori Arrhenius
- Asam adalah zat yang dapat melepaskan ion H+ dalam larutan air.
- Basa adalah zat yang dapat melepaskan ion OH- dalam larutan air.

📖 Teori Bronsted-Lowry
- Asam adalah zat yang dapat melepaskan proton (H+).
- Basa adalah zat yang dapat menerima proton (H+).

📖 Teori Lewis
- Asam adalah zat yang dapat menerima pasangan elektron.
- Basa adalah zat yang dapat memberikan pasangan elektron.

   """)

    # Informasi pembuat
    st.markdown("""
    ### Dibuat Oleh:
    - Amar Evan Gading (2460321)
    - Diandra Namira Zahfa (2460360)
    - Lutfhia Salwani Fatonah (2460410)
    - Nevi Sahara (2460471)
    - Taufan Aliafi (2460525)
    """)

# Hitung pH
if menu == "Hitung pH":
        st.header("🧪 Kalkulator pH Larutan")

        selected = option_menu (
            None, 
            ["Konsentrasi Asam ", "Konsentrasi Basa"],  
            menu_icon="cast", 
            default_index=0, 
            orientation="horizontal"
        )

        if selected == "Konsentrasi Asam":
            selected_asam = option_menu(
            None,
            ["Asam Kuat", "Asam Lemah", "Custom"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
        if selected_asam == "Asam Kuat":
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

         # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M):", min_value=0.0, max_value=14.0, step=0.0001, format="%.3f")

        if selected_asam == "Asam Lemah":
            # Pilih senyawa asam lemah
             asam_lemah = {
            "Asam Asetat (CH3COOH)": 1,
            "Asam Format (HCOOH)": 1,
            "Asam Oksalat (H2C2O4)": 2,
            "Asam Tartarat (H2C4H4O6)": 2, 
            "Asam Sitrat (H3C6H5O7)": 3, 
            "Asam Sianida (HCN)": 1, 
            "Asam Sulfit (H2SO3)": 2,
             }
            # Masukkan Ka
        konstanta_asam = st.number_input("Masukkan Ka", key = "K2")
        st.write("Ka = ", konstanta_asam)

            # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, max_value=14, step=0.0001, format="%.3f", key = "H2")
 
        if selected_asam == "Custom":
            st.subheader("Asam Kuat","Asam Lemah")
            # Masukkan konsentrasi
            konsentrasi = st.number_input("Masukkan konsentrasi (M)",  min_value=0.0, max_value=14.0, format = "%.3f", step=0.0001, key = "H3")
            st.write("Konsentrasi = ", konsentrasi)

            # Masukkan valensi
            a = st.number_input("Masukkan valensi (a)", format = "%i", step=1, key = "A3")
            st.write("a = ", a)

            # Masukkan Ka
            konstanta_asam = st.number_input("Masukkan Ka", key = "K2")
            st.write("Ka = ", konstanta_asam)


        selected_basa = option_menu(
            None, 
            ["Konsentrasi Asam", "Konsentrasi Basa"],  
            menu_icon="cast", 
            default_index=0,
            orientation="horizontal"
        )
    
        if selected == "Konsentrasi Basa":
            selected_basa = option_menu(
            None, 
            ["Basa Kuat", "Basa Lemah", "Custom"],  
            menu_icon="cast", 
            default_index=0,
            orientation="horizontal"
        )    
        if selected_basa == "Basa Kuat":
             # Pilih senyawa basa kuat
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
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", min_value=0.0, max_value=14.0, format= "%.3f", step=0.0001, key = "H5")
        st.write("Konsentrasi = ", konsentrasi)

        if  selected_basa == "Basa Lemah":
            # Pilih senyawa basa lemah
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
        # Masukkan Kb
        konstanta_basa = st.number_input("Masukkan Kb", key = "K6")
        st.write("Kb = ", konstanta_basa)
    
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)",  min_value=0.0, max_value=14.0, format = "%.3f", step=0.0001, key = "H6")
        st.write("Konsentrasi = ", konsentrasi)

        if selected_basa == "Custom":
            st.subheader("Basa Kuat", "Basa Lemah")
        
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)",  min_value=0.0, max_value=14.0, format = "%.3f", step=0.0001, key = "H7")
        st.write("Konsentrasi = ", konsentrasi)
    
        # Masukkan valensi
        a = st.number_input("Masukkan valensi (a)", format = "%i", step=1, key = "A7")
        st.write("a = ", a)

        # Masukkan Kb
        konstanta_basa = st.number_input("Masukkan Kb", key = "K6")
        st.write("Kb = ", konstanta_basa)

    # Perhitungan Hitung pH 
if selected in ["Asam Lemah", "Basa Lemah"]:
        konstanta = st.number_input(f"Masukkan {'Ka' if 'Asam' in selected else 'Kb'}:", min_value=0.0, max_value=14.0, format="%.2e")
if st.button("Hitung pH"):
        try:
            st.markdown("Langkah Perhitungan:")
            if selected == "Asam Kuat":
                ph = -math.log10(konsentrasi)
                penjelasan = "Asam kuat terionisasi sempurna sehingga [H⁺] = konsentrasi asam."
                st.write(f"- [H⁺] = {konsentrasi:.3f} M")
                st.write(f"- pH = -log({konsentrasi:.3f}) = {ph:.2f}")

            elif selected == "Basa Kuat":
                poh = -math.log10(konsentrasi)
                ph = 14 - poh
                penjelasan = "Basa kuat terionisasi sempurna sehingga [OH⁻] = konsentrasi basa."
                st.write(f"- [OH⁻] = {konsentrasi:.3f} M")
                st.write(f"- pOH = -log({konsentrasi:.3f}) = {poh:.2f}")
                st.write(f"- pH = 14 - {poh:.2f} = {ph:.2f}")

            elif jenis == "Asam Lemah":
                h = math.sqrt(konstanta * konsentrasi)
                ph = -math.log10(h)
                penjelasan = "Asam lemah hanya terionisasi sebagian. Rumus: pH = -log(√(Ka * [HA]))"
                st.write(f"- [H⁺] = √({konstanta:.2e} * {konsentrasi:.3f}) = {h:.3f} M")
                st.write(f"- pH = -log({h:.3f}) = {ph:.2f}")

            elif selected == "Basa Lemah":
                oh = math.sqrt(konstanta * konsentrasi)
                poh = -math.log10(oh)
                ph = 14 - poh
                penjelasan = "Basa lemah hanya terionisasi sebagian. Rumus: pH = 14 - log(√(Kb * [B]))"
                st.write(f"- [OH⁻] = √({konstanta:.2e} * {konsentrasi:.3f}) = {oh:.3f} M")
                st.write(f"- pOH = -log({oh:.3f}) = {poh:.2f}")
                st.write(f"- pH = 14 - {poh:.2f} = {ph:.2f}")

            st.success(f"Hasil pH: {ph:.2f}")
            st.info(penjelasan)
          
        except Exception as e:
            st.error("Terjadi kesalahan perhitungan. Pastikan data valid.")

# Tentang Aplikasi
elif menu == "Tentang Aplikasi":
    st.header("📘 Tentang Aplikasi")

    st.markdown("""
    ### 1. Apa itu pH?
    pH adalah ukuran konsentrasi ion hidrogen (H⁺) dalam larutan. Skala pH berkisar dari 0 sampai 14:
    - pH < 7 : larutan bersifat asam
    - pH = 7 : larutan netral
    - pH > 7 : larutan bersifat basa
                
    ### 2. Rumus pH yang Digunakan:
    - Asam Kuat : pH = -log[H⁺]
    - Basa Kuat : pH = 14 - (-log[OH⁻])
    - Asam Lemah: pH = -log(√(Ka * [HA]))
    - Basa Lemah: pH = 14 - log(√(Kb * [B]))
                
    ### 3. 💡 Contoh Soal:
    Hitung pH dari larutan HCl 0.01 M (Asam Kuat)
    - Rumus: pH = -log [H⁺] = -log(0.01) = 2.00
    Hitung pH dari NH₃ 0.1 M, Kb = 1.8 * 10⁻⁵ (Basa Lemah)
    - [OH⁻] = √(Kb * [B]) = √(1.8e-5 * 0.1) ≈ 1.34*10⁻³
    - pOH = -log(1.34e-3) ≈ 2.87
    - pH = 14 - 2.87 =11.13
    """)
    
    #Kotak Saran
elif selected == "📞Kotak Saran dan Kritik":
    st.header(":blue[Hubungi Kami]")
    st.write("Silahkan tinggalkan pesan Anda pada kolom yang tersedia.")
    contact_from = """
        <form action="https://formsubmit.co/nevisahara2006@gmail.com" method="POST">
            <input type="email" name="email" placeholder="Email Anda" required>
            <textarea name="message" placeholder="Pesan Anda"></textarea>
            <button type="submit">Send</button>
        </form>
        """