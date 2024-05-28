Project 2 – Simple Company Networking Project - Devs Config

## Switch 0 ## 

en
conf t
hostname S0

vlan 10
name Admin-IT
vlan 20
name Fin-HR
vlan 30
name CS-Recp
exit

int fa0/1
switchport mode trunk
exit

int ran fa0/2-4
switchport mode access
switchport access vlan 10

int ran fa0/5-7
switchport mode access
switchport access vlan 20

int ran fa0/8-10
switchport mode access
switchport access vlan 30

exit
do wr


## Router 0 ##

//Inter-Vlan Routing – All traffic among VLANs will pass through R0

en
conf t
hostname R0

int g0/0
no shut
exit

int g0/0.10
encapsulation dot1Q 10
ip address 192.168.1.1 255.255.255.192
exit

int g0/0.20
encapsulation dot1Q 20
ip address 192.168.1.65 255.255.255.192
exit

int g0/0.30
encapsulation dot1Q 30
ip address 192.168.1.129 255.255.255.192

do wr
exit

//DHCP

service dhcp

ip dhcp pool Admin-Pool
network 192.168.1.0 255.255.255.192
default-router 192.168.1.1
dns-server 192.168.1.1
domain-name Admin.com
exit

ip dhcp pool Finance-Pool
network 192.168.1.64 255.255.255.192
default-router 192.168.1.65
dns-server 192.168.1.65
domain-name Finance.com
exit

ip dhcp pool CS-Pool
network 192.168.1.128 255.255.255.192
default-router 192.168.1.129
dns-server 192.168.1.129
domain-name CS.com

exit
do wr
