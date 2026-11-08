# 091_4 — RENCANA EVALUASI DAN ASESMEN

## STA-702 — AI Percakapan dan Asisten Cerdas

**Identitas:** `STA-702` AI Percakapan dan Asisten Cerdas · Semester 7 · 3 SKS (+P) · Prasyarat `STI-413`, `STI-416` · PL PL-1 · PEO PEO-1, PEO-2 · IRM M.

## Empat titik evaluasi

| Instrumen | Pekan | Bobot | CPMK | Tugas dan bukti |
| --- | --- | --- | --- | --- |
| Tugas 1 | 4 | 20% | CPMK-1 | Rancang dan uji prompt terstruktur untuk kumpulan pertanyaan berizin. Bukti: prompt, kasus uji dan analisis jawaban |
| UTS | 8 | 25% | CPMK-2 | Bangun RAG multi-dokumen dengan retrieval, reranking dan evaluasi. Bukti: kode, corpus berizin, sitasi dan metrik retrieval |
| Tugas 2 | 12 | 25% | CPMK-3 | Lakukan QLoRA pada model kecil atau simulasi jika perangkat terbatas dan evaluasi hasilnya. Bukti: konfigurasi, log latihan atau rencana simulasi dan evaluasi |
| UAS | 16 | 30% | CPMK-4 | Integrasikan tool calling dan kanal uji, uji kesalahan serta batas keamanan. Bukti: kode, demo, pengujian dan kartu sistem |

## Pemetaan CPMK

| CPMK | CPL | Tugas 1 | UTS | Tugas 2 | UAS | Total |
| --- | --- | --- | --- | --- | --- | --- |
| CPMK-1 | `CPL-09` (`KK1`) | 20% | — | — | — | 20% |
| CPMK-2 | `CPL-06` (`P2`), `CPL-09` (`KK1`) | — | 25% | — | — | 25% |
| CPMK-3 | `CPL-09` (`KK1`) | — | — | 25% | — | 25% |
| CPMK-4 | `CPL-09` (`KK1`) | — | — | — | 30% | 30% |
| Total | — | 20% | 25% | 25% | 30% | 100% |

Skor instrumen = jumlah skor kriteria × bobot rubrik. Nilai akhir = jumlah bobot instrumen × skor instrumen / 100. Skor CPMK = jumlah bobot instrumen terkait × skor instrumen / jumlah bobot instrumen terkait. Skor CPL prodi menggunakan agregasi lintas MK sesuai Dok 008, bukan penjumlahan CPL pada tabel ini.

**Rencana IKU 7:** Tugas 1 (20%) + Tugas 2 (25%) + UAS (30%) direncanakan berbasis kasus/proyek kolaboratif = 75% bobot MK. Target indikatif mata kuliah peminatan Dok 004 adalah 70%; bukti diskusi, kontribusi individual dan produk disimpan. Komposisi metode aktual harus diverifikasi oleh prodi.

## Rencana tugas dan kisi-kisi

### Tugas 1 — pekan 4, 20%

**CPMK-1 / `CPL-09` (`KK1`).** Rancang dan uji prompt terstruktur untuk kumpulan pertanyaan berizin. **Bukti:** prompt, kasus uji dan analisis jawaban.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UTS — pekan 8, 25%

**CPMK-2 / `CPL-06` (`P2`), `CPL-09` (`KK1`).** Bangun RAG multi-dokumen dengan retrieval, reranking dan evaluasi. **Bukti:** kode, corpus berizin, sitasi dan metrik retrieval.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Ujian individual dengan klarifikasi lisan. Rubrik ada pada dokumen 5.

### Tugas 2 — pekan 12, 25%

**CPMK-3 / `CPL-09` (`KK1`).** Lakukan QLoRA pada model kecil atau simulasi jika perangkat terbatas dan evaluasi hasilnya. **Bukti:** konfigurasi, log latihan atau rencana simulasi dan evaluasi.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

### UAS — pekan 16, 30%

**CPMK-4 / `CPL-09` (`KK1`).** Integrasikan tool calling dan kanal uji, uji kesalahan serta batas keamanan. **Bukti:** kode, demo, pengujian dan kartu sistem.

**Kisi-kisi:** ketepatan metode dan asumsi; kualitas hasil; pengujian atau analisis bukti; dokumentasi, etika dan penjelasan batas. Tugas berbasis kasus atau proyek dengan catatan kontribusi dan pembelaan individual. Rubrik ada pada dokumen 5.

## Umpan balik dan PPEPP

Dosen mencatat skor tiap CPMK dan umpan balik, memberikan remediasi sesuai peraturan institusi, merekap ketercapaian dan menindaklanjuti penyebab capaian rendah melalui siklus PPEPP. Jadwal dan nilai resmi ditetapkan pengampu.

## Batas, keselamatan dan acuan

**BoK Dok 043:** `BK-IS16` *Artificial Intelligence*, `BK-IT02` *Applied AI*.

* 🟢 **IN-SCOPE (Wajib Diajarkan):** Arsitektur LLM Modern, Prompt Engineering Lanjut (Few-shot, CoT), Arsitektur RAG (Chunking, Vector Database Chroma/Milvus), Framework LangChain/LlamaIndex, Fine-tuning Efisien (LoRA/QLoRA).
* ❌ **OUT-OF-SCOPE (Dilarang Diajarkan):** ❌ Dilarang mengulang rumus TF-IDF dasar, algoritma Naive Bayes teks klasik, pembuatan scraper web berita umum.
* 🔄 **HANDOFF ANCHOR (Titik Serah Terima):** Membangun sistem asisten cerdas berbasis model bahasa besar tingkat korporat.

**Keterangan pelaksanaan:** Seluruh pemrosesan memakai data dan lingkungan berizin; simulasi lokal tidak membuktikan kinerja atau kepatuhan produksi. Jika GPU tidak tersedia, praktik QLoRA dapat berupa demonstrasi terbatas atau rencana teruji; keterbatasannya harus dinyatakan. Dok 043 menempatkan fine-tuning pada Sub-CPMK-1.1 meskipun rumusan CPMK-3 menilai fine-tuning; dan tool-use pada Sub-CPMK-2.2 meskipun rumusan CPMK-4 membahas agen. Bukti dinilai berdasarkan rumusan CPMK.

**Sumber:** Dok 003/004 (CPL, IRM), 005/051 (identitas, prasyarat), 007 (materi), 008/018 (asesmen), 037/043 (CPMK dan boundary). Materi mingguan disesuaikan dengan urutan capaian dan aturan batas.
