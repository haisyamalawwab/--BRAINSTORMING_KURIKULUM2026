# RUBRIK PENILAIAN — STA-602 SISTEM AGEN CERDAS

**Kode:** STA-602 | **3 SKS / +P** | **Semester:** 7 | **Prasyarat:** STI-307 Sistem Cerdas
**CPL:** KK1, KK2 (Rekayasa Sistem Cerdas & Data Engineering) | **CPMK:** CPMK-1 C4, CPMK-2 C6, CPMK-3 C4, CPMK-4 C5, CPMK-1 C4, CPMK-2 C6, CPMK-3 C5
**Bobot:** 20% Tugas1 + 25% UTS + 25% Tugas2 + 30% UAS =100% | **Revisi:** 07112026

---

## A. RUBRIK TUGAS1 — Milestone 1 / Analisis Awal (20% — Mg4)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **Fungsionalitas/Kebenaran Konsep (30%)** | Service/endpoint berfungsi 100% + validasi + error handler + test pass | Berfungsi 80% + test 1 gagal minor | Berfungsi 60% + error handler missing | Tidak berfungsi / crash |
| **Kebenaran Teknis/Analisis (30%)** | Kebenaran 90%+ (benchmark, arsitektur benar, docs resmi diikuti) | Kebenaran 75-89% | Kebenaran 55-74% | <55% atau salah total |
| **Dokumentasi (20%)** | README/laporan lengkap: instruksi runnable, diagram jelas, sitasi lengkap | Lengkap tetapi instruksi kurang 1 langkah | Tidak lengkap (tanpa diagram/sitasi) | Tidak ada docs |
| **Runnable/Struktur (20%)** | Repo runnable copy-paste + Dockerfile/compose + tag milestone1 | Runnable tetapi manual step | Sebagian runnable (1 fail) | Tidak runnable |

---

## B. RUBRIK UTS — Live Coding Lab Test (25% — Mg8)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **Fungsionalitas/Kebenaran (40%)** | Endpoint/pipeline 200 + JSON valid + benchmark < baseline | 200 tetapi 1 validasi missing | 200 tetapi sync/blocking | Tidak 200/crash |
| **Analisis & Trade-off (30%)** | Jelaskan trade-off dengan angka & contoh (mis. latency vs accuracy, cost vs risk) | Jelaskan 2 trade-off tanpa angka | Jelaskan 1 trade-off | Tidak mampu jelaskan |
| **Benchmark/Evaluasi (20%)** | Benchmark lengkap: P95, RPS, grafik | Benchmark 2 metrik | Benchmark 1 metrik | Tidak ada benchmark |
| **Wawancara/Esai (10%)** | Lisan/esai jelas, struktur, data | Cukup jelas | Ragu-ragu | Tidak terjawab |

---

## C. RUBRIK TUGAS2 — Milestone 2 / Proyek Integrasi (25% — Mg12)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **Integrasi/Kedalaman (35%)** | Integrasi E2E sukses (service+queue/monitoring/compose) + faithfulness/audit ≥80% | Integrasi 80% + 1 service missing | Integrasi 60% (2 fail) | Tidak terintegrasi / tidak ada kajian |
| **Evaluasi/Metrik (30%)** | Evaluasi kuantitatif (P95/RPS/faithfulness) + analisis bottleneck + rekomendasi | Evaluasi 2 metrik | Evaluasi 1 metrik | Tidak ada evaluasi |
| **Runnable/Docs (20%)** | Compose up sukses + healthchecks + E2E curl | Compose up tanpa healthcheck | Compose 3/4 services | Compose gagal |
| **Analisis & Laporan (15%)** | Laporan 2-3 hal: trade-off, lesson learned, instruksi lengkap | 1-2 hal tanpa lesson | <1 hal | Tidak ada laporan |

---

## D. RUBRIK UAS — Demo Day / Presentasi Akhir (30% — Mg16)

| Aspek (Bobot) | Skor 4 (85-100) | Skor 3 (70-84) | Skor 2 (55-69) | Skor 1 (0-54) |
|---|---|---|---|---|
| **Fungsionalitas/Kedalaman (30%)** | FE→BE→DB→service→response sukses live + handle 2 concurrent + error UX | Sukses tanpa streaming/persist | Sebagian gagal | Gagal total / video saja |
| **Performa/Audit (20%)** | P95<500ms-1s, RPS≥30-50, Locust HTML + bottleneck analysis | P95 1-2s, RPS 15-29 | P95 2s+ / RPS 10-14 | Tidak ada performa/audit |
| **Analisis/Keamanan (20%)** | Keamanan aktif (rate limit/guardrails/COBIT controls) + evaluasi | Keamanan ada tanpa uji | Keamanan lemah | Tidak ada keamanan |
| **Docs & Video (15%)** | PORTFOLIO/laporan PDF rapi (TOC) + repo + video 3m HD unlisted + Turnitin≤20% | PDF tanpa TOC, video 2m | PDF berantakan, video <2m | Tidak ada video/Turnitin>20% |
| **Presentasi & Teamwork (15%)** | Presentasi 10-12m jelas + Q&A jawab trade-off dengan angka + peer eval seimbang (20-25%/org) | Jelas tetapi Q&A ragu | Melebihi waktu, Q&A banyak tidak terjawab | Tidak terstruktur, konflik peer |

**Peer eval:** Jika <10% kontribusi → nilai individu -30%. **Syarat lulus UAS:** Minimal skor 2 di semua aspek.

---

## E. Formatif & Kehadiran

| Kriteria | Lulus | Tidak Lulus |
|---|---|---|
| Kehadiran | ≥80% (13/16) | <80% → tugas pengganti/tidak boleh UAS |
| Formatif | ≥6-8/12 pass | <6 → remedial 7 hari |

---

## F. Konversi NA

```
NA = 0.20×Tugas1 + 0.25×UTS + 0.25×Tugas2 + 0.30×UAS + bonus (max +3)
```

| NA | Huruf | Keterangan |
|---|---|---|
|85-100|A|Sangat memuaskan|
|70-84|B|Memuaskan|
|60-69|C|Cukup|
|55-59|D|Tidak lulus remedial|
|<55|E|Gagal|

Aturan: NA≥55 (C) dengan UAS≥50 & hadir≥80%. Remedial Tugas 7 hari (maks B), UAS 14 hari (maks B).

---

*Rubrik mengikat — perubahan via rapat prodi.*
