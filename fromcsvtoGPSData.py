/*******************************************************************************


 * Copyright 2013 University of Southern California
 * 


 * Licensed under the Apache License, Version 2.0 (the "License");


 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at


 * 
 * 	http://www.apache.org/licenses/LICENSE-2.0


 * 
 * Unless required by applicable law or agreed to in writing, software


 * distributed under the License is distributed on an "AS IS" BASIS,


 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and


 * limitations under the License.
 * 


 * This code was developed by the Information Integration Group as part 


 * of the Karma project at the Information Sciences Institute of the 
 * University of Southern California.  For more information, publications, 


 * and related projects, please see: http://www.isi.edu/integration


 ******************************************************************************/
import csv
import datetime

outputfile = open("GPSData.txt", 'w')
csvfile =  open('SimpleLocationProbe.csv', 'rU')
f = csv.DictReader(csvfile)
single = []
for row in f:
    lat = row['mLatitude']
    lng = row['mLongitude']
    timestamp = str(int(float(row['timestamp'])))
    accuracy = row['mAccuracy']
    bearing = row['mBearing']
    data = timestamp+','+lat+','+lng
    if data not in single:
		single.append(data)
		outputfile.write(timestamp+','+lat+','+lng+','+accuracy+','+bearing+'\n')
outputfile.close()
csvfile.close()
