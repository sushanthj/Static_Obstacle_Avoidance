#import interop
import csv
import simplekml
import csv
from polycircles import polycircles
#client = interop.Client(url='http://127.0.0.1:8000',
 #                       username='testuser',
  #                      password='testpass')
#missions = client.get_missions()
#print missions
final_list=[[12.9512174,77.4421549,50],[12.9531622,77.4439573,50]]
#stationary_obstacles, moving_obstacles = client.get_obstacles()
#for i in range(0,len(stationary_obstacles)):
	#temp=[stationary_obstacles[i].latitude,stationary_obstacles[i].longitude,stationary_obstacles[i].cylinder_radius]
	#final_list.append(temp)
print final_list

with open("obstacle_1.csv","wb") as f:
	writer=csv.writer(f)
	writer.writerows(final_list)
obs=csv.reader(open('obstacle_1.csv','r'))

f=open("obstacle_raw.txt","w")
for i in range(0,len(final_list)):
	f.write(str(final_list[i][0]))
	f.write(" ")
	f.write(str(final_list[i][1]))
	f.write(" ")
	f.write(str(final_list[i][2]))
	f.write("\n")

kml = simplekml.Kml()
for row in obs:
      print type(row[0])
      polycircle = polycircles.Polycircle(latitude=float(row[0]),
                                    longitude=float(row[1]),
                                    radius=float(row[2]),
                                    number_of_vertices=36)
      
      pol = kml.newpolygon(name="OBS",
                                         outerboundaryis=polycircle.to_kml())
      pol.style.polystyle.color = \
        simplekml.Color.changealphaint(200, simplekml.Color.blue)
kml.save("test_kml_polygon.kml")


