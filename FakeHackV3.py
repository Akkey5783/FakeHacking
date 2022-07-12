import random
import secrets
import string
import time
from faker import Faker

fake = Faker("ja_JP")

def main(hack_type):
	if hack_type == "BlockATK":
		logs = [
			"Malware Detection | Trojan.MSIL.WHISPERGATE.YXCAQ - Deleted",
			"Spyware Detection | TrojanSpy.MSIL.REDLINESTEALER.YXBDM - Deleted",
			"RansomWare Detection | Ransom.MSIL.POVLSOM.THBAOBA - Deleted", 
			"Spyware Detection | Backdoor.MSIL.SUNBURST.A - Deleted",
			"Malware Detection | Trojan.PS1.POWLOAD.JKP - Deleted",
			"Spyware Detection | Backdoor.MSIL.REMCOS.AOJ - Deleted",
			"Bluteforce Detection - Added Blacklist",
			"DNS Spoofing Detection - Fixed DNS",
			"ARP Spoofing Detection - Running AntiARPoof.exe",
			"Layer3 Attack Detection - Blocked Connection"
		]
		for count in range(3):
			generated_ip = fake.ipv4()
			logs.append(f"{generated_ip} Access Denied")
		while True:
			print(random.choice(logs))
			time.sleep(random.uniform(0.1, 0.5))
  elif hack_type == "SendATK":
    logs = []
    for count in range(100):
      generated_ip = fake.ipv4()
      logs.append(f"Connecting to {generated_ip}...")
      logs.append(f"Connected {generated_ip}!")
      logs.append(f'Sent Command to BOTNET "atk slowloris --address {generated_ip} --error ignore --anonymous true"')
    while True:
      print(random.choice(logs))
      time.sleep(random.uniform(0.1, 0.3))
  else:
    return False
