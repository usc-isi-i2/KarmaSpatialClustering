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
import datetime
f = open("GPSData.txt")
outputFile = open("GPSoutput.txt", 'w')
contents = f.read()
lines = contents.splitlines()
nlines = len(lines)
j = 1
outputFile.write('index,time,latitude,longitude,accuracy,bearing\n')
for i in range(nlines):
	line = lines[i]
	if line.count(',') >= 2:
		newline = line.replace('|', ',')
		idx = newline.find(',')
		timestamp = newline[:idx]
		newline = newline[idx+1:]
		# idx = newline.find(',',idx+1)
		# # dt = (datetime.datetime.fromtimestamp(float(timestamp)/1000.0) + datetime.timedelta(hours=16))
		dt = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
		# dt = (datetime.datetime.fromtimestamp(float(timestamp)/1000.0) + datetime.timedelta(hours=16)).strftime("%m-%d-%Y %H:%M:%S")
		# # ds_hour = dt.strftime("%H")
		# # ds_day = dt.strftime("%A")
		# # # ts = dt.strftime("%H:%M:%S %d/%m/%Y")
		# # d = timestamp + ',' + ds_hour + ',' + ds_day
		# # newline = '\n' + str(j) + ',' + d + newline[idx:]
		newline = str(j) + ',' + dt + ',' + newline + '\n'
		outputFile.write(newline)
		j = j + 1
f.close()
outputFile.close()

# f = open("CellLocationData.txt")
# outputFile = open("CellLocationDatamedium.txt", 'w')
# contents = f.read()
# lines = contents.splitlines()
# nlines = len(lines)
# j = 1
# for i in range(nlines):
# 	line = lines[i]
# 	if line.count('|') == 4:
# 		newline = line.replace('|', ',')
# 		idx = newline.find(',')
# 		timestamp = newline[:idx]
# 		# dt = (datetime.datetime.fromtimestamp(float(timestamp)/1000.0) + datetime.timedelta(hours=16))
# 		dt = (datetime.datetime.fromtimestamp(float(timestamp)/1000.0) + datetime.timedelta(hours=16)).strftime("%m-%d-%Y %H:%M:%S")
# 		# ds_hour = dt.strftime("%H")
# 		# ds_day = dt.strftime("%A")
# 		# # ts = dt.strftime("%H:%M:%S %d/%m/%Y")
# 		# d = timestamp + ',' + ds_hour + ',' + ds_day
# 		# newline = '\n' + str(j) + ',' + d + newline[idx:]
# 		newline = str(j) + ',' + dt + newline[idx:] + '\n'
# 		outputFile.write(newline)
# 		j = j + 1
# f.close()
# outputFile.close()

# f = open("wifi_scan.txt")
# outputFile = open("wifi_scanmedium.txt", 'w')
# contents = f.read()
# lines = contents.splitlines()
# nlines = len(lines)
# j = 1
# for i in range(nlines):
# 	line = lines[i]
# 	if line.count('|') >= 2:
# 		idx = line.find('|')
# 		timestamp = line[:idx]
# 		# dt = (datetime.datetime.fromtimestamp(float(timestamp)/1000.0) + datetime.timedelta(hours=16))
# 		dt = (datetime.datetime.fromtimestamp(float(timestamp)/1000.0) + datetime.timedelta(hours=16)).strftime("%m-%d-%Y %H:%M:%S")
# 		# ds_hour = dt.strftime("%H")
# 		# ds_day = dt.strftime("%A")
# 		# # ts = dt.strftime("%H:%M:%S %d/%m/%Y")
# 		# d = timestamp + ',' + ds_hour + ',' + ds_day
# 		# newline = '\n' + str(j) + ',' + d + newline[idx:]
# 		newline = str(j) + ',' + dt + line[idx:] + '\n'
# 		outputFile.write(newline)
# 		j = j + 1
# f.close()
# outputFile.close()
