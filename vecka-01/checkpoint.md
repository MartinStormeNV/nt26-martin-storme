# Uppgift<br><br>

checkpoint.md med skärmdumpen av prompten och utdatan från `show startup-config | include hostname`<br><br>

### Kommentar<br>
Jag gjorde denna uppgiften i Cisco Packet Tracer.<br><br>
Dessvärre verkar inte simuleringsverktyget klara `|`, som min skärmdump visar. Intressant att `| include` funkar med `show running-config` men inte med `show startup-config` (se bild 1). <br><br>

Dock kan man med `show startup-config` ändå visa att min konfiguration med `hostname` i configureringsläget och `copy running-config startup-config` (copy run start) anternativt `write memory` (wr) slagit igenom (se bild 2).<br><br>

Bild 1.<br>
<img width="455" height="428" alt="Bild startup-config hostname" src="https://github.com/user-attachments/assets/68f350fb-a4c6-4580-9e88-b9be502e1fa3" />

Bild 2.<br>
<img width="371" height="513" alt="Bild jämför running-config och startup-config" src="https://github.com/user-attachments/assets/289fb73b-c9e5-441b-8dbb-7e90d435dcd4" />

