// TC-PF-03. Load testing kecil. Jalankan hanya setelah pemilik website mengizinkan.
// k6 run -e BASE_URL=https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/ load-login.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '60s',
  thresholds: {
    http_req_failed: ['rate==0'],
    http_req_duration: ['p(95)<3000'],
  },
};

const BASE = __ENV.BASE_URL || 'https://ppdb-slbsanadharma.up.railway.app/ppdb-slb/';

export default function () {
  for (const p of ['auth/login.php', 'auth/register.php']) {
    const r = http.get(BASE + p);
    check(r, { 'status 200': (x) => x.status === 200 });
    sleep(1);
  }
}
