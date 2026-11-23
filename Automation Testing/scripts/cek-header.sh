#!/usr/bin/env bash
# TC-SC-01 dan TC-SC-02 (bagian pasif). Hanya membaca header halaman login, satu permintaan per perintah.
BASE="${BASE_URL:-https://ppdb-slbsanadharma.up.railway.app/ppdb-slb}"
echo "== HTTP ke HTTPS =="
curl -sI "${BASE/https:/http:}/auth/login.php" | head -n 5
echo "== Header respons HTTPS =="
curl -sI "$BASE/auth/login.php" | grep -iE '^(HTTP|strict-transport|x-frame|x-content-type|content-security|set-cookie)'
