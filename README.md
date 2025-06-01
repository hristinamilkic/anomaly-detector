# IoT Anomaly Detection – Python Program

## 🛠️ Alati i biblioteke
- **Scapy** – za čitanje .pcap fajlova i dekodovanje paketa
- **pandas** – za jednostavno upravljanje podacima
- **matplotlib** – za vizuelizaciju saobraćaja

## 🎯 Kako skripta radi
1️⃣ Učitava snimak saobraćaja (`capture.pcap`)  
2️⃣ Analizira svaki IP paket i izdvaja izvorne i odredišne IP adrese  
3️⃣ Broji koliko zahteva je poslato ka/polazilo sa svake IP adrese  
4️⃣ Prikazuje anomalne IP adrese
5️⃣ Vizuelizuje broj zahteva radi lakšeg uvida  

## 🧠 Zašto dinamički prag?
Prema istraživanjima IoT bezbednosti (npr. OWASP IoT Top 10), uređaji obično šalju stabilan broj zahteva. Ako jedan uređaj počne da šalje više od mean + 3 * std zahteva u kratkom periodu, to može biti:  
- Napad (DDoS, brute-force, scanning)  
- Maliciozni firmware  
- Kompromitovan uređaj

## Kako pokrenuti program?

bash command -> python anomaly_detector.py
