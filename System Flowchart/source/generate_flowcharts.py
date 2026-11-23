"""Generate flowchart PNGs (Graphviz) in the same visual style as the reference repo."""
import subprocess, sys, os

STYLE = {
    "start":    'shape=ellipse, style=filled, fillcolor="#d5e8d4", color="#82b366", width=1.6, height=0.6',
    "proc":     'shape=box, style=filled, fillcolor="#dae8fc", color="#6c8ebf", width=2.6, height=0.6',
    "io":       'shape=parallelogram, style=filled, fillcolor="#fff2cc", color="#d6b656", width=2.6, height=0.6',
    "dec":      'shape=diamond, style=filled, fillcolor="#f8cecc", color="#b85450", width=3.0, height=1.1',
}
YA = 'fontcolor="#1a7f37", fontname="Helvetica-Bold"'
TIDAK = 'fontcolor="#c62828", fontname="Helvetica-Bold"'


def build(name, title, nodes, edges, out_dir):
    L = ['digraph F {',
         '  graph [rankdir=TB, splines=spline, nodesep=0.7, ranksep=0.45, fontname="Helvetica", '
         f'label="{title}", labelloc=t, labeljust=l, fontsize=16, pad=0.4, bgcolor="white"];',
         '  node [fontname="Helvetica", fontsize=12, penwidth=1.3];',
         '  edge [fontname="Helvetica", fontsize=11, color="#222222", arrowsize=0.8];']
    for nid, kind, label in nodes:
        L.append(f'  {nid} [{STYLE[kind]}, label="{label}"];')
    for e in edges:
        a, b = e[0], e[1]
        opt = e[2] if len(e) > 2 else {}
        attrs = []
        lab = opt.get("label")
        if lab:
            col = YA if lab == "Ya" else TIDAK if lab == "Tidak" else 'fontcolor="#333333", fontname="Helvetica-Bold"'
            attrs.append(f'label="{lab}", {col}')
        if opt.get("back"):
            attrs.append('constraint=false')
        for k in ("tailport", "headport"):
            if k in opt:
                attrs.append(f'{k}={opt[k]}')
        L.append(f'  {a} -> {b} [{", ".join(attrs)}];')
    L.append('}')
    src = os.path.join(out_dir, "source", name + ".dot")
    os.makedirs(os.path.dirname(src), exist_ok=True)
    open(src, "w").write("\n".join(L))
    png = os.path.join(out_dir, "images", name + ".png")
    os.makedirs(os.path.dirname(png), exist_ok=True)
    subprocess.run(["dot", "-Tpng", "-Gdpi=150", src, "-o", png], check=True)
    return png


OUT = sys.argv[1]

# ---------- 1a. Registrasi ----------
build("Registrasi_flowchart", "FLOWCHART REGISTRASI AKUN", [
    ("s", "start", "Mulai"),
    ("r0", "proc", "Buka halaman Buat Akun Baru"),
    ("r1", "io", "Isi nama, email, no. HP,\\npassword & konfirmasi"),
    ("r2", "dec", "Data lengkap, password\\n≥ 6 & cocok, syarat\\ndicentang?"),
    ("r3", "proc", "Klik Daftar Sekarang"),
    ("r4", "dec", "Email sudah\\nterdaftar?"),
    ("r5", "proc", "Akun disimpan (belum aktif)\\n& email aktivasi dikirim"),
    ("r6", "proc", "Klik link aktivasi di email"),
    ("r7", "proc", "Akun aktif, diarahkan\\nke halaman Login"),
    ("e", "start", "Selesai"),
], [
    ("s", "r0"), ("r0", "r1"), ("r1", "r2"),
    ("r2", "r1", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("r2", "r3", {"label": "Ya"}), ("r3", "r4"),
    ("r4", "r1", {"label": "Ya", "back": 1, "tailport": "e", "headport": "e"}),
    ("r4", "r5", {"label": "Tidak"}), ("r5", "r6"), ("r6", "r7"), ("r7", "e"),
], OUT)

# ---------- 1b. Login ----------
build("Login_flowchart", "FLOWCHART LOGIN DAN LOGOUT", [
    ("s", "start", "Mulai"),
    ("l0", "proc", "Buka halaman Login"),
    ("l1", "io", "Isi email & password"),
    ("l2", "dec", "Email & password\\nbenar?"),
    ("l3", "dec", "Akun sudah\\ndiaktivasi?"),
    ("l4", "dec", "Role admin?"),
    ("a1", "proc", "Masuk Dashboard Admin"),
    ("u1", "proc", "Masuk Beranda Pendaftar"),
    ("lo", "proc", "Logout: sesi diakhiri"),
    ("e", "start", "Selesai"),
], [
    ("s", "l0"), ("l0", "l1"), ("l1", "l2"),
    ("l2", "l1", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("l2", "l3", {"label": "Ya"}),
    ("l3", "l1", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("l3", "l4", {"label": "Ya"}),
    ("l4", "a1", {"label": "Ya"}), ("l4", "u1", {"label": "Tidak"}),
    ("a1", "lo"), ("u1", "lo"), ("lo", "e"),
], OUT)

# ---------- 1c. Lupa Password ----------
build("Lupa_Password_flowchart", "FLOWCHART LUPA DAN RESET PASSWORD", [
    ("s", "start", "Mulai"),
    ("f0", "proc", "Buka halaman Lupa Password"),
    ("f1", "io", "Isi email"),
    ("f2", "dec", "Email terdaftar?"),
    ("f3", "proc", "Link reset dikirim\\n(berlaku 1 jam)"),
    ("f4", "proc", "Buka link reset di email"),
    ("f5", "io", "Isi password baru\\n& konfirmasi"),
    ("f6", "dec", "Token valid, password\\n≥ 6 & cocok?"),
    ("f7", "proc", "Password diperbarui"),
    ("f8", "proc", "Login dengan password baru"),
    ("e", "start", "Selesai"),
], [
    ("s", "f0"), ("f0", "f1"), ("f1", "f2"),
    ("f2", "f1", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("f2", "f3", {"label": "Ya"}), ("f3", "f4"), ("f4", "f5"), ("f5", "f6"),
    ("f6", "f5", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("f6", "f7", {"label": "Ya"}), ("f7", "f8"), ("f8", "e"),
], OUT)

# ---------- 2. Pendaftar ----------
build("Pendaftar_flowchart", "FLOWCHART ROLE PENDAFTAR", [
    ("s", "start", "Mulai"),
    ("p0", "proc", "Login"),
    ("p1", "proc", "Melihat Beranda\\n(progress & status)"),
    ("f0", "io", "Pilih jenjang\\n(TKLB / SDLB / SMPLB)"),
    ("d0", "dec", "Jenjang dipilih?"),
    ("f1", "io", "Isi data pribadi"),
    ("d1", "dec", "Field wajib\\nterisi?"),
    ("f2", "io", "Pilih surat keterangan"),
    ("f3", "io", "Isi data orang tua / wali"),
    ("u1", "io", "Upload berkas"),
    ("du", "dec", "Format JPG/JPEG/PNG/PDF\\n& ukuran ≤ 2 MB?"),
    ("u2", "proc", "Berkas tersimpan,\\nmenunggu verifikasi admin"),
    ("g1", "proc", "Melihat Pengumuman"),
    ("dg", "dec", "Hasil seleksi?"),
    ("g2", "proc", "Tampil pesan\\ntidak lolos"),
    ("r1", "proc", "Daftar Ulang: lihat berkas\\n& informasi pembayaran"),
    ("lo", "proc", "Logout"),
    ("e", "start", "Selesai"),
], [
    ("s", "p0"), ("p0", "p1"), ("p1", "f0"), ("f0", "d0"),
    ("d0", "f0", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("d0", "f1", {"label": "Ya"}), ("f1", "d1"),
    ("d1", "f1", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("d1", "f2", {"label": "Ya"}), ("f2", "f3"), ("f3", "u1"), ("u1", "du"),
    ("du", "u1", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("du", "u2", {"label": "Ya"}), ("u2", "g1"), ("g1", "dg"),
    ("dg", "g1", {"label": "Pending", "back": 1, "tailport": "e", "headport": "e"}),
    ("dg", "g2", {"label": "Gagal"}), ("dg", "r1", {"label": "Lolos"}),
    ("g2", "lo"), ("r1", "lo"), ("lo", "e"),
], OUT)

# ---------- 3. Admin ----------
build("Admin_flowchart", "FLOWCHART ROLE ADMIN", [
    ("s", "start", "Mulai"),
    ("a0", "proc", "Login"),
    ("a1", "proc", "Melihat Dashboard\\n(statistik pendaftar)"),
    ("a2", "proc", "Buka menu Verifikasi"),
    ("a3", "io", "Cari / saring pendaftar"),
    ("a4", "proc", "Buka detail pendaftar"),
    ("a5", "io", "Verifikasi tiap berkas\\n(valid / tolak)"),
    ("d1", "dec", "Data & berkas\\nlayak diterima?"),
    ("t1", "io", "Isi catatan penolakan"),
    ("t2", "proc", "Klik Tolak: status ditolak,\\nemail dikirim"),
    ("a6", "proc", "Klik Terima"),
    ("d2", "dec", "Semua berkas wajib\\nterverifikasi?"),
    ("a7", "proc", "Status diterima,\\nemail konfirmasi dikirim"),
    ("a8", "proc", "Buka menu Kelola Pengumuman"),
    ("a9", "io", "Pilih hasil seleksi\\n& isi catatan"),
    ("d3", "dec", "Hasil seleksi?"),
    ("h1", "proc", "Simpan & kirim email\\nhasil seleksi"),
    ("h2", "proc", "Simpan tanpa email"),
    ("lo", "proc", "Logout"),
    ("e", "start", "Selesai"),
], [
    ("s", "a0"), ("a0", "a1"), ("a1", "a2"), ("a2", "a3"), ("a3", "a4"), ("a4", "a5"), ("a5", "d1"),
    ("d1", "t1", {"label": "Tidak"}), ("t1", "t2"), ("t2", "lo"),
    ("d1", "a6", {"label": "Ya"}), ("a6", "d2"),
    ("d2", "a5", {"label": "Tidak", "back": 1, "tailport": "e", "headport": "e"}),
    ("d2", "a7", {"label": "Ya"}), ("a7", "a8"), ("a8", "a9"), ("a9", "d3"),
    ("d3", "h1", {"label": "Lolos / Gagal"}), ("d3", "h2", {"label": "Pending"}),
    ("h1", "lo"), ("h2", "lo"), ("lo", "e"),
], OUT)
print("ok")
