#include <iostream>
#include <exception>
#include <cmath>
#include <GeographicLib/Geocentric.hpp>
#include <GeographicLib/LocalCartesian.hpp>
#include <fstream>


using namespace std;
using namespace GeographicLib;
struct obj{
 double x;
 double y;
 double z;
 };
struct obj func(double a,double b,double c)
{
  struct obj m;
  try {
    Geocentric earth(Constants::WGS84_a(), Constants::WGS84_f());
    // Alternatively: const Geocentric& earth = Geocentric::WGS84();
    const double lat0 = 48 + 50/60.0, lon0 = 2 + 20/60.0; // Paris
    double lat = a, lon = b, h = c;
    LocalCartesian proj(lat0, lon0, 0, earth);
    {
      // Sample forward calculation
      double x, y, z;
      proj.Forward(lat, lon, h, m.x, m.y, m.z);
      //cout << x << " " << y << " " << z << "\n";
    }
 
  }
  catch (const exception& e) {
    cerr << "Caught exception: " << e.what() << "\n";
}
return m;
}
int main() {
 struct obj result; 
 std::ifstream infile("obstacle_raw.txt");
 std::ofstream ofile("obstacle_localcartesian.txt");
 double a,b,c;
 while (infile >> a >> b >> c)
 {
 result=func(a,b,c);
 std::cout<<result.x<<" "<<result.y<<" "<<result.z<<endl;
 ofile<<result.x<<" "<<result.y<<" "<<result.z<<"\n";
}
}







//g++ -c -g -O3 -I/usr/local/include obstacle_raw_to_local.cpp
//g++ -g -o obstacle_raw_to_local obstacle_raw_to_local.o -L/usr/local/lib -lGeographic
//g++ -g -o obstacle_raw_to_local obstacle_raw_to_local.o -Wl,-rpath=/usr/local/lib \-L/usr/local/lib -lGeographic
