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
#split the data
import datetime
f = open("GPSoutput.txt")
contents = f.read()
lines = contents.splitlines()
nlines = len(lines)
filename = ' '
j = 1 
for i in range(1, nlines):
	line = lines[i]
	if line.count(',') >= 2:
		newline = line.replace('|', ',')
		idx = newline.find(',')
		newline = newline[idx+1:]
		idx = newline.find(',')
		timestamp = newline[:idx]
		newline = newline[idx+1:]
		if filename == timestamp[:10]:
			j = j + 1
			outputFile.write(str(j) + ',' + timestamp + ',' + newline + '\n' )
		else:
			outputFile = open("GPSoutput" + timestamp[:10] + ".txt", 'w')
			outputFile.write('index,time,latitude,longitude,accuracy,bearing\n')
			j = 1
			outputFile.write(str(j) + ',' + timestamp + ',' + newline + '\n' )
			filename = timestamp[:10]
f.close()
