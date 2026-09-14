# Krabbafel 1)  
  
* 1. Observation *  Datorer i samma VLAN når varandra inom en switch men inte mellan switcharna. Andra VLAN fungerar.  
  
2. Hypotes  
- Troligen missat att tillåta vlan’et på trunken på någon av switcharna på vardera sida om trunken.  
  
3. Test  
- Körde `show interfaces trunk` på båda switcharna och kolla att vlan-nummret står med över allowed vlan’s.  
  
4. Slutsats   
- Jag har själv missat detta på ena switchen när jag labbat och det visade sig vara just detta felet. Symtomet är ganska tydligt när lan’et funkar på den egna switchen men inte på andra sidan trunken.  
  
5. Åtgärd  
- :bulb Kör `switchport trunk allowed vlan add <nummer>`. Obs, alternativet  `switchport trunk allowed vlan <lista>` ersätter helt samtliga tidigare tillåtna vlan.  
  
  
  
#Krabbafel 2)  
1. Observation  
- Två VLAN slutar fungera över trunken medan de andra fungerar. Felmeddelande RECV_PVID_ERR eller NATIVE_VLAN_MISMATCH  
  
2. Hypotes  
Olika nativ vlan på olika switchar.  
  
3. Test  
- Kör `show interfaces trunk`och kolla vilket vlan som står under “Native vlan”  
  
4. Slutsats  
- Har testat i CPT med att ändra på ena sidan, och “NATIVE_VLAN_MISMATCH” är exakt vad som hände.  
  
5. Åtgärd  
- :bulb Sätt samma native vlan (lämpligen 999) på båda switcharnas trunkport genom ´switchport trunk native vlan 999´
