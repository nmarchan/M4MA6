'''Note: could not find file named world_fires_1_day.csv on the website
used https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv
and saved it as that filename instead. It seems to have the same kind of data.'''

from matplotlib import pyplot as plt #needed for plotting
import csv      #needed to work with csv

firefile = 'world_fires_1_day.csv' #set filename for file

latitude = []
longitude = []

with open(firefile) as f:   #make a file object
    fires = csv.reader(f)   #fires will read through the file
    header = next(fires)   #grabs the first line as header without fire data

    for row in fires:
        latitude.append(float(row[0]))      #store latitude as float
        longitude.append(float(row[1]))     #store longitude as float
        
#labels and axis scale
plt.title('Worldwide Fire Data (Last 24 Hours)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis([-180.0, 180.0, -90.0, 90.0])

#plot fires in orange
plt.scatter(longitude, latitude, c='orange', linewidth=0, edgecolors='none',s=5)
plt.show()
