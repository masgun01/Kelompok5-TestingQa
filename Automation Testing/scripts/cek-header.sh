#!/usr/bin/env bash
# TC-SC-01 dan TC-SC-02 (bagian pasif). Hanya membaca header halaman login, satu permintaan per perintah.
BASE="${BASE_URL:-https://ppdb-slbsanadharma.up.railway.app/ppdb-slb}"
echo "== HTTP ke HTTPS (TC-SC-01) =="
curl -sI "${BASE/https:/http:}/auth/login.php" | head -n 5
echo "== Header respons HTTPS & Cookie PHPSESSID (TC-SC-01 & TC-SC-02) =="
HEADERS=$(curl -sI "$BASE/auth/login.php")
echo "$HEADERS" | grep -iE '^(HTTP|strict-transport|x-frame|x-content-type|content-security|set-cookie|x-powered-by)'
for h in "strict-transport-security" "x-frame-options" "x-content-type-options" "content-security-policy"; do
  if ! echo "$HEADERS" | grep -qi "^$h:"; then
    echo "[TEMUAN] Header $h: TIDAK ADA"
  fi
done
