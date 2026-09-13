# Gör det själv - frågor & svar

5. Ta bort VLAN 30 från trunkens allowed-lista iena änden. Pinga igen. Vad händer, och vad säger show interfaces trunk på respektive sida?  
💡Ping får "Request timed out".  
show interfaces trunk visar på ena sidan: `Vlans allowed on trunk 10,20,30,99` och på andra sidan: `Vlans allowed on trunk 10,20,99`  
  
7. Sätt tillbaka det. Ändra sedan native VLAN på ena sidan till 1. Vad säger loggen?  
💡%CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on GigabitEthernet0/1 (1), with SW-Nordvik-1 GigabitEthernet0/2 (999).
