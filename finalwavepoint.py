lat=[]
lon=[]
alt=[]
flag=0
for line in open("output3.txt"):
	line = line.strip()
	parts = line.split(" ")
	if(flag==0):
		homelat=float(parts[0])
		homelon=float(parts[1])		
		homealt=float(parts[2])
		lat.append(float(parts[0]))
		lon.append(float(parts[1]))
		alt.append(float(parts[2]))
		flag=1
	else:
		lat.append(float(parts[0]))
		lon.append(float(parts[1]))
		alt.append(float(parts[2])-homealt)
f = open("finaloutput.txt","w") #opens file with name of "test.txt"
f.write("QGC WPL 110\n")
f.write("0\t1\t0\t16\t0\t0\t0\t0\t")
f.write(str(lat[0]))
f.write("       ")
f.write(str(lon[0]))
f.write("       ")
f.write(str(alt[0]))
f.write("       ")
f.write("1\n")
for i in range(1,len(lat)):
	f.write(str(i))
	f.write("\t0")
	f.write("\t")
	f.write("3")
	f.write("\t")
	f.write("16\t")
	f.write("0.0000000")
	f.write("\t")
	f.write("0.0000000")
	f.write("\t")
	f.write("0.0000000")
	f.write("\t")
	f.write("0.0000000")
	f.write("\t")
	f.write(str(lat[i]))
	f.write("       ")
	f.write(str(lon[i]))
	f.write("       ")
	f.write(str(alt[i]))
	f.write("\n")
	f.write("1\n")
f.close()

		
	



