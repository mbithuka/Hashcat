from hashlib import sha256
import subprocess as um

def ash(text):
	return sha256(text.encode("ascii")).hexdigest()



um.run(['hashcat','-a','0','-m','1400','ash('password')','/bin/shared/wordlists/rockyou.txt'])
