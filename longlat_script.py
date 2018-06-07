import csv
#readLat = csv.reader(open('longlat_data.csv', 'rb')) #opens in binary mode
#readWrite = csv.reader(open('food_access_2015.csv', 'rb'))


# readLat.next(); #skip first line
# readWrite.next(); #skip first line
# for row1 in readWrite:
# 	for row2 in readLat:
# 		if row1[1] == row2[]
# print row

csv_in = open("new_data.csv", 'r')
myreader = csv.reader(csv_in)

csv_lat = open("longlat_data.csv", 'r')
reader2 = csv.reader(csv_lat)

csv_out = open("output_newdata.csv",'w', newline='')
mywriter = csv.writer(csv_out)


State = []
County = []
Population = []
OHU = []
LA_Pop = []
Lat = []
Lon = []

County_lat = []
Latitude = []
Longitude = []


#reads in lat, long, and county_lat
for row in reader2:
	usps, geoid, ancode, county_name, l1, l2, l3, l4, lati, longi = row
	if(usps != "USPS"):
		County_lat.append(county_name.rstrip())
		Latitude.append(lati)
		Longitude.append(longi)


for row in myreader:
	census, st, coun, pop, oh, lapop  = row
	if(census != "CensusTract"):
		if(coun in County):
			getindex = County.index(coun)
			Population[getindex] += float(pop)
			OHU[getindex] += float(oh)
			LA_Pop[getindex] += float(lapop)
		else:
			State.append(st)
			County.append(coun)
			Population.append(float(pop))
			OHU.append(float(oh))
			LA_Pop.append(float(lapop))

			if(coun in County_lat):
				getCIndex = County_lat.index(coun)
				Lat.append(Latitude[getCIndex])
				Lon.append(Longitude[getCIndex])
			else:
				Lat.append("na")
				Lon.append("na")

for row in zip(State, County, Population, OHU, LA_Pop, Lat, Lon):
	mywriter.writerow(row)

csv_out.close()
csv_in.close()