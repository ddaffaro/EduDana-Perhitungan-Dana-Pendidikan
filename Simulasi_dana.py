import streamlit as st
import pandas as pd
import math

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")
    
# ==========================================
# KONFIGURASI HALAMAN UTAMA
# ==========================================
st.set_page_config(
    page_title="EduDana - Simulasi & Edukasi Dana Pendidikan",
    page_icon="🎓",
    layout="wide",
)

# Kustomisasi CSS untuk Styling, Smooth Scroll, dan STICKY NAVBAR
st.markdown("""
    <style>
    /* Membuat scroll halaman menjadi halus */
    html {
        scroll-behavior: smooth;
    }
    
    /* Mengubah warna background utama aplikasi (Menggunakan warna #111318) */
    .stApp {
        background-color: #111318;
        color: #E2E8F0;
    }
    
    /* Menghilangkan padding bawaan Streamlit agar navbar menempel rapi */
    .block-container {
        padding-top: 70px !important;
    }
    
    /* STYLING HORIZONTAL STICKY NAVBAR MURNI HTML */
    .custom-navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #282A35; /* Warna abu-abu pilihanmu */
        z-index: 999999;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 40px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        border-bottom: 1px solid #334155;
    }
    .navbar-brand {
        color: #3B82F6 !important;
        font-size: 22px;
        font-weight: bold;
        text-decoration: none;
    }
    .navbar-menu {
        display: flex;
        gap: 25px;
    }
    .navbar-item {
        color: #E2E8F0 !important;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        padding: 8px 16px;
        border-radius: 6px;
        transition: all 0.3s ease;
    }
    .navbar-item:hover {
        background-color: #3B82F6;
        color: white !important;
    }
    
    /* UTILITY STYLES */
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #3B82F6;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px;
        color: #94A3B8;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 26px;
        font-weight: bold;
        color: #3B82F6;
        margin-top: 60px; /* Jarak aman agar header tidak tertutup navbar saat discroll */
        margin-bottom: 15px;
        border-bottom: 2px solid #334155;
        padding-bottom: 8px;
    }
    .card-info {
        background-color: #282A35;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin-bottom: 15px;
    }
    .card-faq {
        background-color: #282A35;
        padding: 18px;
        border-radius: 10px;
        margin-bottom: 12px;
        border: 1px solid #334155;
    }
    .footer-note {
        background-color: #78350F;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #FCD34D;
        font-size: 14px;
        color: #FDE68A;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# RENDER FIXED NAVBAR
# ==========================================
st.markdown("""
    <div class="custom-navbar">
        <a href="#home" class="navbar-brand">🎓 EduDana</a>
        <div class="navbar-menu">
            <a href="#home" class="navbar-item">🏠 Beranda</a>
            <a href="#faq" class="navbar-item">❓ FAQ</a>
        </div>
    </div>
""", unsafe_allow_html=True)



# ==========================================
# HALAMAN 1: HOME / BERANDA
# ==========================================
# Element Anchor Target
st.markdown('<div id="home" style="padding-top: 20px;"></div>', unsafe_allow_html=True)

# --- SECTION 1: HERO BANNER ---
col_hero1, col_hero2 = st.columns([1.8, 1.2])
with col_hero1:
    st.markdown('<div class="main-title">🎓 EduDana</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Sistem Perencanaan Keuangan & Simulasi Dana Pendidikan Anak</div>', unsafe_allow_html=True)
    st.write(
        "Biaya pendidikan merupakan salah satu pengeluaran terbesar yang sering kali membuat orang tua terkejut "
        "saat anak memasuki jenjang perkuliahan. EduDana hadir sebagai platform edukasi interaktif berbasis web "
        "yang membantu Anda mengkalkulasi, merencanakan, dan mengantisipasi lonjakan biaya sekolah di masa depan "
        "secara presisi menggunakan metode ilmiah keuangan."
    )
    st.markdown('<br><a href="#simulasi" style="text-decoration:none;"><button style="background-color:#3B82F6; color:white; border:none; padding:12px 24px; border-radius:8px; font-weight:bold; cursor:pointer; transition: 0.3s; box-shadow: 0 4px 6px rgba(59, 130, 246, 0.4);">Mulai Simulasi Perhitungan ➔</button></a>', unsafe_allow_html=True)

with col_hero2:
    st.markdown(f"""
    <div style="background-color: #282A35; padding: 22px; border-radius: 12px; border: 1px solid #334155; box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
        <h4 style="color: #3B82F6; margin-top:0; border-bottom: 1px solid #334155; padding-bottom: 5px;">📚 Inti Teori Finansial</h4>
        <ul style="color:#E2E8F0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
            <li><b>Future Value (FV):</b> Rumus untuk menghitung nilai masa depan uang setelah memperhitungkan faktor persentase inflasi tahunan.</li>
            <li><b>Sinking Fund:</b> Metode pengumpulan dana secara bertahap dan konsisten untuk target spesifik demi menjaga stabilitas arus kas bulanan.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- SECTION 2: STATISTIK & URGENSI (Biar Full) ---
st.markdown("<h3 style='color: #3B82F6; text-align: center;'>Kenapa Harus Merencanakan Dana Pendidikan Sekarang?</h3>", unsafe_allow_html=True)
st.write("")

stat_col1, stat_col2, stat_col3 = st.columns(3)
with stat_col1:
    st.markdown(f"""
    <div style="background-color: #282A35; padding: 20px; border-radius: 10px; text-align: center; border-top: 4px solid #EF4444;">
        <h2 style="color: #EF4444; margin: 0;">10% - 15%</h2>
        <p style="font-weight: bold; margin: 5px 0 0 0; color: #E2E8F0;">Rata-rata Inflasi Pendidikan</p>
        <p style="font-size: 13px; color: #94A3B8; margin-top: 5px;">Kenaikan biaya sekolah per tahun di Indonesia jauh melampaui inflasi ekonomi nasional.</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col2:
    st.markdown(f"""
    <div style="background-color: #282A35; padding: 20px; border-radius: 10px; text-align: center; border-top: 4px solid #F59E0B;">
        <h2 style="color: #F59E0B; margin: 0;">2 Kali Lipat</h2>
        <p style="font-weight: bold; margin: 5px 0 0 0; color: #E2E8F0;">Lonjakan Biaya</p>
        <p style="font-size: 13px; color: #94A3B8; margin-top: 5px;">Hanya dalam waktu 6-7 tahun, biaya masuk universitas atau sekolah pilihan bisa naik hingga dua kali lipat.</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col3:
    st.markdown(f"""
    <div style="background-color: #282A35; padding: 20px; border-radius: 10px; text-align: center; border-top: 4px solid #10B981;">
        <h2 style="color: #10B981; margin: 0;">Sinking Fund</h2>
        <p style="font-weight: bold; margin: 5px 0 0 0; color: #E2E8F0;">Solusi Cerdas</p>
        <p style="font-size: 13px; color: #94A3B8; margin-top: 5px;">Menabung di instrumen investasi yang tepat membantu melawan erosi daya beli akibat inflasi.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- SECTION 3: ALUR KERJA SISTEM (HOW IT WORKS) ---
st.markdown("<h3 style='color: #3B82F6; text-align: center;'>Alur Kerja Aplikasi</h3>", unsafe_allow_html=True)
st.write("")

flow_col1, flow_col2, flow_col3, flow_col4 = st.columns(4)
with flow_col1:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 30px;">⚙️</div>
        <h5 style="margin: 5px 0; color:#3B82F6;">1. Atur Parameter</h5>
        <p style="font-size: 13px; color: #94A3B8;">Tentukan asumsi inflasi tahunan dan persentase imbal hasil investasi di panel samping.</p>
    </div>
    """, unsafe_allow_html=True)

with flow_col2:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 30px;">📝</div>
        <h5 style="margin: 5px 0; color:#3B82F6;">2. Input Biaya Riil</h5>
        <p style="font-size: 13px; color: #94A3B8;">Masukkan estimasi uang pangkal dan uang SPP/UKT berdasarkan harga survei saat ini.</p>
    </div>
    """, unsafe_allow_html=True)

with flow_col3:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 30px;">📊</div>
        <h5 style="margin: 5px 0; color:#3B82F6;">3. Kalkulasi Otomatis</h5>
        <p style="font-size: 13px; color: #94A3B8;">Sistem memproses nilai masa depan (Future Value) berdasarkan target tahun masuk anak.</p>
    </div>
    """, unsafe_allow_html=True)

with flow_col4:
    st.markdown("""
    <div style="text-align: center; padding: 10px;">
        <div style="font-size: 30px;">💡</div>
        <h5 style="margin: 5px 0; color:#3B82F6;">4. Dapatkan Solusi</h5>
        <p style="font-size: 13px; color: #94A3B8;">Aplikasi mengeluarkan nominal rekomendasi tabungan bulanan wajib demi mencapai target.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)



# ==========================================
# HALAMAN 2: KALKULATOR SIMULASI
# ==========================================
st.markdown('<div id="simulasi" style="padding-top: 40px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">🚀 Kalkulator Simulasi Dana Pendidikan</div>', unsafe_allow_html=True)

# --- PANEL PENGATURAN ASUMSI ---
st.markdown("""
<div style="background-color: #282A35; padding: 20px; border-radius: 12px; border: 1px solid #334155; margin-bottom: 25px;">
    <h4 style="color: #3B82F6; margin-top:0;">⚙️ Parameter & Asumsi Finansial Dinamis</h4>
    <p style="font-size: 13px; color: #94A3B8;">Sesuaikan persentase di bawah untuk memperbarui hasil kalkulasi Future Value secara otomatis.</p>
</div>
""", unsafe_allow_html=True)

# Membuat grid 3 kolom untuk kontrol parameter keuangan
asumsi_col1, asumsi_col2, asumsi_col3 = st.columns(3)

with asumsi_col1:
    persen_inflasi = st.slider("Asumsi Inflasi Pendidikan (%)", min_value=0, max_value=20, value=10, step=1)
with asumsi_col2:
    persen_investasi = st.slider("Asumsi Keuntungan Investasi (%)", min_value=0, max_value=15, value=6, step=1)
with asumsi_col3:
    tabungan_sekarang = st.number_input("Tabungan Saat Ini (Rp)", min_value=0, value=0, step=1000000)
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(tabungan_sekarang)}")

st.markdown("---")

# FORM INPUT DATA SEKOLAH (GRID 4 KOLOM)
col_sd, col_smp, col_sma, col_kuliah = st.columns(4)
data_jenjang = {}

with col_sd:
    st.markdown("### 🎒 Jenjang SD")
    sd_m = st.number_input("Mulai dalam (Tahun)", min_value=0, value=1, key="SD_m")
    sd_d = st.number_input("Lama Sekolah (Tahun)", min_value=0, value=6, key="SD_d")
    sd_p = st.number_input("Uang Pangkal Hari Ini (Rp)", min_value=0, value=3000000, step=1000000, key="SD_p")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(sd_p)}")
    sd_s = st.number_input("SPP Bulanan Hari Ini (Rp)", min_value=0, value=500000, step=100000, key="SD_s")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(sd_s)}")
    data_jenjang['SD'] = {"mulai": sd_m, "durasi": sd_d, "pangkal": sd_p, "spp": sd_s}

with col_smp:
    st.markdown("### 🧑‍🎓 Jenjang SMP")
    smp_m = st.number_input("Mulai dalam (Tahun)", min_value=0, value=7, key="SMP_m")
    smp_d = st.number_input("Lama Sekolah (Tahun)", min_value=0, value=3, key="SMP_d")
    smp_p = st.number_input("Uang Pangkal Hari Ini (Rp)", min_value=0, value=4000000, step=1000000, key="SMP_p")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(smp_p)}")
    smp_s = st.number_input("SPP Bulanan Hari Ini (Rp)", min_value=0, value=750000, step=100000, key="SMP_s")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(smp_s)}")
    data_jenjang['SMP'] = {"mulai": smp_m, "durasi": smp_d, "pangkal": smp_p, "spp": smp_s}

with col_sma:
    st.markdown("### 🧑‍🔬 Jenjang SMA")
    sma_m = st.number_input("Mulai dalam (Tahun)", min_value=0, value=10, key="SMA_m")
    sma_d = st.number_input("Lama Sekolah (Tahun)", min_value=0, value=3, key="SMA_d")
    sma_p = st.number_input("Uang Pangkal Hari Ini (Rp)", min_value=0, value=5000000, step=1000000, key="SMA_p")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(sma_p)}")
    sma_s = st.number_input("SPP Bulanan Hari Ini (Rp)", min_value=0, value=1000000, step=100000, key="SMA_s")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(sma_s)}")
    data_jenjang['SMA'] = {"mulai": sma_m, "durasi": sma_d, "pangkal": sma_p, "spp": sma_s}

with col_kuliah:
    st.markdown("### 🎓 Jenjang Kuliah")
    kul_m = st.number_input("Mulai dalam (Tahun)", min_value=0, value=13, key="Kuliah_m")
    kul_d = st.number_input("Lama Studi (Tahun)", min_value=0, value=4, key="Kuliah_d")
    kul_p = st.number_input("Uang Pangkal Hari Ini (Rp)", min_value=0, value=30000000, step=5000000, key="Kuliah_p")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(kul_p)}")
    kul_s = st.number_input("UKT Semester Hari Ini (Rp)", min_value=0, value=12000000, step=200000, key="Kuliah_s")
    st.caption(f"Nominal yang dimasukkan: {format_rupiah(kul_s)}")
    data_jenjang['Kuliah'] = {"mulai": kul_m, "durasi": kul_d, "pangkal": kul_p, "spp": kul_s}


# LOGIKA PERHITUNGAN
total_biaya_masa_depan = 0
daftar_hasil = []
tahun_maksimal = 0

# Hitung Future Value untuk setiap jenjang pendidikan (FV)
# FV = PV * (1 + i)^n
for nama, data in data_jenjang.items():
    inflasi_faktor = math.pow(1 + (persen_inflasi / 100), data['mulai'])
    pangkal_depan = data['pangkal'] * inflasi_faktor
    
    total_spp_depan = 0
    for tahun in range(data['durasi']):
        faktor_tahun = math.pow(1 + (persen_inflasi / 100), data['mulai'] + tahun)
        biaya_tahun = data['spp'] * faktor_tahun
        if nama == "Kuliah":
            total_spp_depan += biaya_tahun * 2
        else:
            total_spp_depan += biaya_tahun * 12

#Hitung Total Dana Masa Depan 
# Jumlah 
    subtotal_jenjang = pangkal_depan + total_spp_depan
    total_biaya_masa_depan += subtotal_jenjang
    tahun_maksimal = max(tahun_maksimal, data['mulai'])

    daftar_hasil.append({
        "Jenjang": nama,
        "Mulai (Thn)": data['mulai'],
        "Uang Pangkal Masa Depan": f"Rp {pangkal_depan:,.0f}",
        "Total SPP/UKT Masa Depan": f"Rp {total_spp_depan:,.0f}",
        "Sub-Total": subtotal_jenjang
    })

# Hitung Tabungan Bulanan yang Dibutuhkan (sinking fund)
# FV = pV(1 + r)^n
nilai_tabungan_akhir = tabungan_sekarang * math.pow(1 + (persen_investasi / 100), tahun_maksimal)
# KD = max(0, TB - FV)
kekurangan_dana = max(0, total_biaya_masa_depan - nilai_tabungan_akhir)
#konversi return tahunan ke bulan 
# i = return tahunan / 12
bunga_bulanan = (persen_investasi / 100) / 12
jumlah_bulan = tahun_maksimal * 12

# Validasi agar target menabung tidak 0 tahun 
if tahun_maksimal <= 0:
    st.warning("⚠️ Target durasi menabung harus lebih dari 0 tahun. Silakan periksa kembali input data jenjang pendidikan.")
    st.stop()

# Menghitung tabungan bulanan yang harus di setor 
# PMT = FV x i / (1 + i)^n - 1 (Future Value Annuity)(tabungan Berkala)
if bunga_bulanan > 0:
    tabungan_bulanan = (kekurangan_dana * bunga_bulanan) / (math.pow(1 + bunga_bulanan, jumlah_bulan) - 1)
else:
    tabungan_bulanan = kekurangan_dana / jumlah_bulan if jumlah_bulan > 0 else 0

# TAMPILAN DASHBOARD METRIK
st.write("")
m1, m2, m3 = st.columns(3)
m1.metric("Total Dana Dibutuhkan (Future Value)", f"Rp {total_biaya_masa_depan:,.0f}")
m2.metric("Rekomendasi Tabungan / Bulan", f"Rp {tabungan_bulanan:,.0f}")
m3.metric("Target Durasi Menabung", f"{tahun_maksimal:,.0f} Tahun")

st.write("")
df_hasil = pd.DataFrame(daftar_hasil)
st.table(df_hasil.style.format({"Sub-Total": "Rp {:,.0f}"}))

st.success(f"**💡 Edu-Summary:** Total biaya riil masa depan anak Anda diekspektasikan sebesar **Rp {total_biaya_masa_depan:,.0f}**. Apabila dialokasikan pada instrumen investasi bernilai return tahunan **{persen_investasi}%**, maka Anda cukup mengalokasikan **Rp {tabungan_bulanan:,.0f} / bulan** secara disiplin.")

st.markdown("""
<div class="footer-note">
    <strong>⚠️ Disclaimer Teknis:</strong> Perhitungan di atas berbasis metode matematis <i>Future Value (Annual Compound Inflation)</i> dan <i>Sinking Fund Method</i>.
</div>
""", unsafe_allow_html=True)


# ==========================================
# HALAMAN 3: FAQ / PUSAT PEMBELAJARAN
# ==========================================
# Element Anchor Target
st.markdown('<div id="faq" style="padding-top: 40px;"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-header">❓ FAQ & Pusat Edukasi Finansial</div>', unsafe_allow_html=True)

faq_col1, faq_col2 = st.columns(2)
with faq_col1:
    st.markdown("""
    <div class="card-faq">
        <h4 style="color:#3B82F6; margin-top:0;">Q: Apa itu Inflasi Pendidikan dan mengapa nilainya sangat tinggi?</h4>
        <p style="color:#CBD5E1; font-size:14px; margin-bottom:0;">
        <b>A:</b> Inflasi pendidikan adalah persentase kenaikan biaya sekolah atau kuliah setiap tahunnya. Berbeda dengan inflasi bahan pokok, inflasi pendidikan di Indonesia jauh lebih tinggi (10-12%) karena peningkatan kualitas kurikulum, sarana, dan prasarana.
        </p>
    </div>
    <div class="card-faq">
        <h4 style="color:#3B82F6; margin-top:0;">Q: Mengapa menabung biasa di celengan/rekening bank kurang efektif?</h4>
        <p style="color:#CBD5E1; font-size:14px; margin-bottom:0;">
        <b>A:</b> Karena bunga tabungan bank biasa umumnya di bawah 1%, sementara biaya sekolah naik 10% per tahun. Solusinya adalah beralih ke instrumen investasi yang imbal hasilnya melampaui tingkat inflasi.
        </p>
    </div>
    """, unsafe_allow_html=True)

with faq_col2:
    st.markdown("""
    <div class="card-faq">
        <h4 style="color:#3B82F6; margin-top:0;">Q: Apa yang dimaksud dengan Sinking Fund Method pada simulasi ini?</h4>
        <p style="color:#CBD5E1; font-size:14px; margin-bottom:0;">
        <b>A:</b> <i>Sinking Fund</i> adalah metode menabung terarah untuk tujuan spesifik dengan nominal dan tenggat waktu yang pasti. Rumus kalkulator ini otomatis menghitung target bulanan Anda agar terkumpul pas pada waktunya.
        </p>
    </div>
    <div class="card-faq">
        <h4 style="color:#3B82F6; margin-top:0;">Q: Instrumen investasi apa yang cocok untuk dana pendidikan?</h4>
        <p style="color:#CBD5E1; font-size:14px; margin-bottom:0;">
        <b>A:</b> Jangka pendek (< 3 thn) cocok di Reksa Dana Pasar Uang. Jangka menengah (3-5 thn) di Reksa Dana Pendapatan Tetap / Obligasi. Jangka panjang (> 5 thn) bisa memanfaatkan Reksa Dana Saham atau Emas.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer Watermark Lembut
st.markdown("""
    <br><hr style="border-color: #334155;">
    <div style='display: flex; justify-content: space-between; font-size: 12px; color: #64748B;'>
        <span>Bersiap hari ini, tenang di masa depan.</span>
    </div>
""", unsafe_allow_html=True)
