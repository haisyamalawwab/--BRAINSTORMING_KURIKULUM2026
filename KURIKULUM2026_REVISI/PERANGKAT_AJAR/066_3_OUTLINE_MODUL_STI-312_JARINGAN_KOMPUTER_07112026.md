# 066_3 — OUTLINE BUKU MODUL PEMBELAJARAN & PRAKTIKUM BERBASIS OBE
## STI-312 — JARINGAN KOMPUTER (*Computer Networks*)

**Program Studi:** S1 Sistem dan Teknologi Informasi (SISTEKIN) — FSTI Universitas Widyagama Malang  
**Nomor Dokumen Induk RPS:** `071030.B4.5.2.RPS-STI312` · **Bobot:** 3 SKS (`T=2, P=1`) · **Semester:** 3  
**CPL:** `CPL-07` (`P3` = 45%) & `CPL-11` (`KK3` = 55%) [Level `R`] · **BoK:** `BK-IS03`, `BK-IT03`, `BK-IT14`  
**Tanggal Penyusunan:** 07 November 2026  

---

## 1. IDENTITAS & SPESIFIKASI BUKU MODUL AJAR + PRAKTIKUM

| Atribut Modul | Spesifikasi Teknis & Akademik |
|---|---|
| **Judul Buku Modul** | *Rekayasa Jaringan Komputer Modern: Analisis Paket Wireshark, Pengalamatan IPv4 VLSM & IPv6, Switching VLAN, Routing OSPF, Layanan Jaringan, & Keamanan ACL* |
| **Target Tebal Naskah** | 14 Bab Materi + 14 Modul Praktikum Laboratorium + 2 Unit Evaluasi ($\pm 215\text{–}250\text{ halaman}$ A4 dilengkapi bedah paket **Wireshark**, tabel perhitungan **VLSM & IPv6**, topologi jaringan, dan referensi perintah CLI konfigurasi/verifikasi) |
| **Pagar Pembatas Buku (*Guardrail*)** | Fokus murni pada arsitektur protokol, pengalamatan, *switching/routing*, layanan dasar jaringan, dan penyaringan paket ACL lokal; tidak melebar ke *pentesting/IDS enterprise* (`STI-418` / `STB-501`), *Cloud VPC* (`STI-417`), maupun fisika gelombang RF. |

---

## 2. PETA KESELARASAN 14 BAB & 14 MODUL PRAKTIKUM TERHADAP CPMK & SUB-CPMK

| Bagian | Bab & Lab | Judul Bab Materi & Modul Praktikum | Pekan | CPMK | Sub-CPMK | Asesmen |
|---|:---:|---|:---:|:---:|:---:|---|
| **Bagian I:<br>Arsitektur OSI/TCP-IP & Analisis Paket Wireshark** | **Bab 1 / Lab 1** | Arsitektur Jaringan, Metrik Kinerja Transmisi, & Model **OSI 7-Layer vs TCP/IP** | Mg 1 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 2 / Lab 2** | Proses **Enkapsulasi PDU**, Standar **Ethernet (`802.3`)**, WLAN, & Resolusi **ARP** | Mg 2 | `CPMK-1` | `Sub-CPMK-1.1` | Tugas 1 (20%) |
| | **Bab 3 / Lab 3** | Protokol *Transport Layer* (**TCP vs UDP**) & Bedah *Handshake* di **Wireshark** | Mg 3 | `CPMK-1` | `Sub-CPMK-1.2` | Tugas 1 (20%) |
| | **Bab 4 / Lab 4** | Forensik Komunikasi Lintas Lapisan (*ARP–DNS–TCP–HTTP–ICMP*) dengan **Wireshark** | Mg 4 | `CPMK-1` | `Sub-CPMK-1.2` | **Tugas 1 (Mg 4)** |
| **Bagian II:<br>Perancangan Pengalamatan IPv4 VLSM & IPv6** | **Bab 5 / Lab 5** | Struktur Paket **IPv4**, Alamat Privat RFC 1918, & Perhitungan **CIDR Subnetting** | Mg 5 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 6 / Lab 6** | Perancangan Efisien **VLSM (*Variable Length Subnet Mask*)** Multi-Divisi Bebas Konflik | Mg 6 | `CPMK-2` | `Sub-CPMK-2.1` | UTS (25%) |
| | **Bab 7 / Lab 7** | Arsitektur Pengalamatan **IPv6** (*GUA, ULA, Link-Local, SLAAC*) & Jaringan *Dual-Stack* | Mg 7 | `CPMK-2` | `Sub-CPMK-2.2` | **UTS (Mg 8)** |
| *Evaluasi I* | *Unit E1* | *Bank Studi Kasus Perancangan Pengalamatan IPv4 VLSM/CIDR & IPv6 Organisasi (UTS)* | *Mg 8* | *`CPMK-2`* | *`2.1–2.2`* | *UTS (25%)* |
| **Bagian III:<br>Switching VLAN & Routing Statis/OSPF** | **Bab 8 / Lab 8** | Segmentasi *Layer-2 Switching*: **VLAN**, **IEEE 802.1Q Trunking**, & Dasar **STP** | Mg 9 | `CPMK-3` | `Sub-CPMK-3.1` | Tugas 2 (25%) |
| | **Bab 9 / Lab 9** | **Inter-VLAN Routing** (*Router-on-a-Stick & SVI*) serta **Static / Default Routing** | Mg 10 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | Tugas 2 (25%) |
| | **Bab 10 / Lab 10** | *Dynamic Link-State Routing* dengan **OSPF** (*Adjacency, Cost Metric, & Failover*) | Mg 11 | `CPMK-3` | `Sub-CPMK-3.2` | Tugas 2 (25%) |
| | **Bab 11 / Lab 11** | Metodologi Diagnostik & *Troubleshooting* Konektivitas Terpadu **VLAN + OSPF** | Mg 12 | `CPMK-3` | `Sub-CPMK-3.1, 3.2` | **Tugas 2 (Mg 12)** |
| **Bagian IV:<br>Layanan Jaringan Dasar & Keamanan ACL** | **Bab 12 / Lab 12** | Konfigurasi Layanan Infrastruktur Jaringan: **DHCP (+ Relay)**, **DNS**, & **HTTP** | Mg 13 | `CPMK-4` | `Sub-CPMK-4.1` | UAS (30%) |
| | **Bab 13 / Lab 13** | Translasi Alamat **NAT (*Static NAT, Dynamic NAT, PAT*)** & Dasar **Standard ACL** | Mg 14 | `CPMK-4` | `Sub-CPMK-4.1, 4.2` | UAS (30%) |
| | **Bab 14 / Lab 14** | Kebijakan Penyaringan **Extended ACL** Multi-Segmen & *Handoff* ke `STI-417`/`STI-418` | Mg 15 | `CPMK-4` | `Sub-CPMK-4.2` | **UAS (Mg 16)** |
| *Evaluasi II* | *Unit E2* | *Panduan Proyek Jaringan Enterprise & Ujian Praktik Konfigurasi Layanan/ACL (UAS)* | *Mg 16* | *`CPMK-4`* | *`4.1–4.2`* | *UAS (30%)* |

---

## 3. RINCIAN SUBSTANSI TIAP BAB & MODUL PRAKTIKUM

#### BAB 1 & LAB 1: Arsitektur Jaringan, Metrik Kinerja Transmisi, & Model OSI 7-Layer vs TCP/IP (Pekan 1)
* **Materi & Praktikum:** Klasifikasi LAN/MAN/WAN, *Packet Switching*, perhitungan 4 komponen *nodal delay*, pemetaan fungsi **OSI 7-Layer** dan **TCP/IP**, serta diagnostik dasar `ping` dan `traceroute`.

#### BAB 2 & LAB 2: Proses Enkapsulasi PDU, Standar Ethernet (`802.3`), WLAN, & Resolusi ARP (Pekan 2)
* **Materi & Praktikum:** Pembungkusan *header/trailer* tiap lapisan, kabel UTP/serat optik & dasar `802.11`, bingkai **Ethernet II**, cara kerja *MAC Address Table* pada switch, dan pertukaran **ARP**.

#### BAB 3 & LAB 3: Protokol *Transport Layer* (TCP vs UDP) & Bedah *Handshake* di Wireshark (Pekan 3)
* **Materi & Praktikum:** Penomoran port soket, struktur *header* **UDP** vs **TCP**, **TCP 3-Way Handshake**, *Sequence/Ack*, kontrol aliran, serta penyaringan paket langsung di **Wireshark**.

#### BAB 4 & LAB 4: Forensik Komunikasi Lintas Lapisan (*ARP–DNS–TCP–HTTP–ICMP*) dengan Wireshark (Pekan 4)
* **Materi & Praktikum:** Rekonstruksi urutan paket lengkap transaksi web nyata dari rekaman `.pcapng` serta pembacaan pesan kontrol/diagnostik **ICMP**.

#### BAB 5 & LAB 5: Struktur Paket IPv4, Alamat Privat RFC 1918, & Perhitungan CIDR Subnetting (Pekan 5)
* **Materi & Praktikum:** Bedah kolom *IPv4 Header* (TTL, Protocol, Checksum), aritmetika biner *Subnet Mask*, notasi **CIDR**, dan perhitungan cepat batas subnet.

#### BAB 6 & LAB 6: Perancangan Efisien VLSM Multi-Divisi Bebas Konflik (Pekan 6)
* **Materi & Praktikum:** Prosedur alokasi hierarkis **VLSM** dari segmen terbesar ke tautan titik-ke-titik `/30`, pemeriksaan anti-konflik alamat, dan *route summarization*.

#### BAB 7 & LAB 7: Arsitektur Pengalamatan IPv6 & Jaringan *Dual-Stack* (Pekan 7)
* **Materi & Praktikum:** Format 128-bit **IPv6**, aturan kompresi nol, *Global Unicast / Unique Local / Link-Local*, subnetting `/64`, **ICMPv6 Neighbor Discovery**, **SLAAC**, dan konfigurasi *Dual-Stack*.

#### BAB 8 & LAB 8: Segmentasi *Layer-2 Switching*: VLAN, IEEE 802.1Q Trunking, & Dasar STP (Pekan 9)
* **Materi & Praktikum:** Pemisahan *broadcast domain* dengan **VLAN**, *Access vs Trunk Port*, *VLAN Tagging* **802.1Q**, pengamanan *Native VLAN*, dan pencegahan *loop* **STP/RSTP**.

#### BAB 9 & LAB 9: Inter-VLAN Routing (*Router-on-a-Stick & SVI*) serta Static / Default Routing (Pekan 10)
* **Materi & Praktikum:** Konfigurasi sub-antarmuka `dot1Q` pada router dan SVI pada *Multilayer Switch*, aturan *Longest Prefix Match*, *Administrative Distance*, serta **Static, Floating Static, & Default Route**.

#### BAB 10 & LAB 10: *Dynamic Link-State Routing* dengan OSPF (*Adjacency, Cost Metric, & Failover*) (Pekan 11)
* **Materi & Praktikum:** Algoritma SPF Dijkstra, status tetangga **OSPF**, perhitungan *Cost* antarmuka, pemilihan *DR/BDR*, `passive-interface`, dan pengujian pemulihan otomatis jalur putus.

#### BAB 11 & LAB 11: Metodologi Diagnostik & *Troubleshooting* Konektivitas Terpadu VLAN + OSPF (Pekan 12)
* **Materi & Praktikum:** Pendekatan *Bottom-Up* dan *Divide-and-Conquer* menemukan kesalahan konfigurasi L1–L3 menggunakan perintah `show`, `ping`, dan `traceroute`.

#### BAB 12 & LAB 12: Konfigurasi Layanan Infrastruktur Jaringan: DHCP (+ Relay), DNS, & HTTP (Pekan 13)
* **Materi & Praktikum:** Siklus **DHCP DORA**, penerusan lintas subnet dengan `ip helper-address` (*DHCP Relay*), rekaman zona **DNS**, dan pengujian akses layanan **HTTP**.

#### BAB 13 & LAB 13: Translasi Alamat NAT (*Static NAT, Dynamic NAT, PAT*) & Dasar Standard ACL (Pekan 14)
* **Materi & Praktikum:** Pemetaan `inside local ↔ inside global` pada **Static NAT** dan **PAT (*NAT Overload*)**, mekanisme *Wildcard Mask*, dan penyaringan sumber dengan **Standard ACL**.

#### BAB 14 & LAB 14: Kebijakan Penyaringan Extended ACL Multi-Segmen & *Handoff* ke `STI-417`/`STI-418` (Pekan 15)
* **Materi & Praktikum:** Penyusunan aturan **Extended Named ACL** berbasis IP, protokol, dan nomor port untuk mengisolasi segmen sensitif organisasi, pengujian matriks izin/blokir, serta jembatan menuju *Security Group Cloud VPC* (`STI-417 Komputasi Awan`) dan pertahanan berlapis (`STI-418 Dasar Keamanan Informasi` & `STB-501 Keamanan Jaringan dan Forensik Digital`).
