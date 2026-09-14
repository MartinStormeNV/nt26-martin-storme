import ipaddress

# Byt ut mot det nat du vill rakna pa.
# text = "192.168.1.64/26"

# Bytar ut och sätter den adressen från övning 3.3
# Ja, det blir samma nät som tidigare eftersom blocksteget är 64.
# Subnätet startar på 64 och sista adress är 127. Därmed hamnar ".100" inom det spannet/nätet.
text = "192.168.1.100/26"

# Modulen ipaddress raknar ut korrekt relevanta adresser för natet
net = ipaddress.ip_network(text, strict=False)

# Lagrar en lista på de adresser som kan användas som hosadresser
# (ej första och sista adressen som är paxade till nätverk och broadcast)
usable = list(net.hosts())

print(f"Nat: {net.network_address}")
print(f"Natmask: {net.netmask}")
print(f"Broadcast: {net.broadcast_address}")
print(f"Forsta adress: {usable[0]}")
print(f"Sista adress: {usable[-1]}")
print(f"Antal enheter: {len(usable)}")
