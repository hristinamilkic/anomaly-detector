from scapy.all import rdpcap, IP
import pandas as pd
import matplotlib.pyplot as plt


packets = rdpcap("Setup-A-2-STA.pcap")

data = []
for pkt in packets:
    if IP in pkt:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        data.append((src_ip, dst_ip))

df = pd.DataFrame(data, columns=["SrcIP", "DstIP"])


src_counts = df["SrcIP"].value_counts()
dst_counts = df["DstIP"].value_counts()

print("\nBroj zahteva po izvornoj IP adresi:\n", src_counts)
print("\nBroj zahteva po odredišnoj IP adresi:\n", dst_counts)


anomalous_src = src_counts[src_counts > 50]
print("\n⚠️ Anomalous source IPs:\n", anomalous_src)


plt.figure(figsize=(10, 6))
src_counts.plot(kind="bar", color="skyblue")
plt.title("Broj zahteva po izvornoj IP adresi")
plt.xlabel("IP adresa")
plt.ylabel("Broj zahteva")
plt.grid(True)
plt.tight_layout()
plt.show()
