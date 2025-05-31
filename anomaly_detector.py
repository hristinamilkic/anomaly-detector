from scapy.all import rdpcap, IP
import pandas as pd
import matplotlib.pyplot as plt

packets = rdpcap("captures/EdimaxCam2/Setup-C-1-STA.pcap")

data = []
for pkt in packets:
    if IP in pkt:
        data.append((pkt[IP].src, pkt[IP].dst))

df = pd.DataFrame(data, columns=["SrcIP", "DstIP"])

src_counts = df["SrcIP"].value_counts()
dst_counts = df["DstIP"].value_counts()

print("\nBroj zahteva po izvornoj IP adresi:\n", src_counts)
print("\nBroj zahteva po odredišnoj IP adresi:\n", dst_counts)

mean = src_counts.mean()
std = src_counts.std()
threshold = mean + 3 * std
print(f"\n📊 Prag za anomaliju: {threshold:.2f} (srednja vrednost + 3σ)")

anomalous_src = src_counts[src_counts > threshold]
print("\n⚠️ Anomalous source IPs:\n", anomalous_src)

plt.figure(figsize=(12, 6))
src_counts.plot(kind="bar", color="skyblue")
plt.axhline(threshold, color='red', linestyle='--', label=f'Prag: {threshold:.2f}')
plt.title("Broj zahteva po izvornoj IP adresi")
plt.xlabel("IP adresa")
plt.ylabel("Broj zahteva")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
