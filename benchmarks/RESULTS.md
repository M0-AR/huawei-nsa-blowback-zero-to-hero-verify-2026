# RESULTS — 2026-10-16 live run (all 4 live fetches TRUE)

- Claims: **12/12 CONFIRMED (100%), mean 4.67/5, falsified 0**
- Blowback mid: **$16.0B** (WannaCry $4–8B + NotPetya $10B+); free leak → worm **28 days**
- NVD live totals: **Huawei 1062 vs Cisco 6985** (≈6.6×) — hygiene attack surface is universal
- SEC live: Cisco CIK 858877 OK; Yahoo 12y chart OK
- Tests: **4 passed**
- Reproduce: `docker compose up --build` or `bash scripts/repro.sh`

See `RESULTS.json`, `verification_report.json`, `blowback_benchmark.json`, `market_benchmark.json`, `cve_benchmark.json`.
