import os
def menu():

	print ("""
	___________              __               .__       .__   
	\_   _____/____    _____/  |_  ___________|__|____  |  |  
	 |    __) \__  \ _/ ___\   __\/  _ \_  __ \  \__  \ |  |  
	 |     \   / __ \\  \___|   | (  <_> )  | \/  |/ __ \|  |__
	 \___  /  (____  /\___  >__|  \____/|__|  |__(____  /____/
	     \/        \/     \/                          \/      
	___________.__            .___            		  
	\_   _____/|__| ____    __| _/___________ 		  
	 |    __)  |  |/    \  / __ |/ __ \_  __ \ 		  
	 |     \   |  |   |  \/ /_/ \  ___/|  | \/                
	 \___  /   |__|___|  /\____ |\___  >__|    made by:Kr0nuzz
	     \/            \/      \/    \/                      """) 

	p = (int(input("Masukkan Nilai Awal>> ")))
	x = (int(input("Masukkan Nilai Akhir>> ")))
	text = ("~ {}\n~ {}\n".format(p,x))
	z = p-x+1
	o = p+1
	friend = []
	for j in range (z,o):
		friend.append(j)
	if x == 2:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1])
	if x == 3:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2])
	if x == 4:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2]*friend[3])
	if x == 5:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2]*friend[3]*friend[4])
	if x == 6:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2]*friend[3]*friend[4]*friend[5])
	if x == 7:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2]*friend[3]*friend[4]*friend[5]*friend[6])
	if x == 8:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2]*friend[3]*friend[4]*friend[5]*friend[6]*friend[7])
	if x == 9:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2]*friend[3]*friend[4]*friend[5]*friend[6]*friend[7]*friend[8])
	if x == 10:
		print ("maka hasil akhirnya adalah>>",friend[0]*friend[1]*friend[2]*friend[3]*friend[4]*friend[5]*friend[6]*friend[7]*friend[8]*friend[9])
menu()
if __name__=="__main__":
	while (True):
		(input("tekan apapun untuk mengulang"))
		os.system("clear")
		menu()
