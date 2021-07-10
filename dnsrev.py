import socket, sys

def DnsRev(host,wordlist):
	domains = open(str(wordlist), 'r')
	for d in domains.readlines():
		try:
			print(d.strip('\n')+"."+host,"===>",socket.gethostbyname(d.strip('\n')+"."+host))
		except socket.gaierror:
			continue
		except KeyboardInterrupt:
			sys.exit()
def main():
	if len(sys.argv)<=2:
		print("use: python3 script.py [host] [wordlist]")
	else:
		host = sys.argv[1]
		wordlist = sys.argv[2]
		DnsRev(host, wordlist)

if __name__ == "__main__":
	main()
