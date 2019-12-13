import os
from time import sleep
def konak():
	print(""" /$$   /$$ /$$$$$$       /$$$$$$$$ /$$                 /$$                    """)
	sleep(0.3)
	print("""| $$  / $$|_  $$_/      | $$_____/|__/                | $$                    """)
	sleep(0.3)
	print("""|  $$/ $$/  | $$        | $$       /$$ /$$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ """)
	sleep(0.3)
	print(""" \  $$$$/   | $$        | $$$$$   | $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$""")
	sleep(0.3)
	print("""  >$$  $$   | $$        | $$__/   | $$| $$  \ $$| $$  | $$| $$$$$$$$| $$  \__/""")
	sleep(0.3)
	print(""" /$$/\  $$  | $$        | $$      | $$| $$  | $$| $$  | $$| $$_____/| $$      """)
	sleep(0.3)
	print("""| $$  \ $$ /$$$$$$      | $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$| $$      """)
	sleep(0.3)
	print("""|__/  |__/|______/      |__/      |__/|__/  |__/ \_______/ \_______/|__/      """)
	sleep(0.3)
	p = (int(input("Masukkan TB>> ")))
	a = (int(input("Masukkan TA>> ")))
	
	def xi():
		mean1 = p+0.5
		mean2 = a-0.5
		lol = mean1+mean2
		fixx = lol/2
		print ("maka hasil Xi nya adalah", fixx)
	xi()
konak()
if __name__=="__main__":
	while(True):
		input("tekan apapun untuk mengulang")
		os.system("clear")
		konak()
