from os import listdir, makedirs
from os.path import isfile, join, exists

import sys

mypath=raw_input("maps directory:");
files=[f for f in listdir(mypath) if isfile(join(mypath,f))]
#create schema
filename=files[0];
f=open(mypath+"/"+filename,"r");
schema_path=raw_input("schema name:");
w=open(schema_path,"w");
width=0;
height=0;
line=f.readline();
coords=[];
while(line !=""):
	cells=line.split(' ');
	width=0;
	for cell in cells:
		if(cell!='NA'):
			try:
				floatvalue=float(cell);
				coords.append((width,height));
			except ValueError:
				continue;
		width+=1;
	height+=1;
	line=f.readline();
print len(coords);
print "width="+str(width);
print "height="+str(height);
w.write(str(width)+" "+str(height)+"\n");

for item in coords:
	w.write(str(item[0])+" "+str(item[1]));
	w.write("\n");

w.close();
converted_path=raw_input("converted maps directory name:");
if not exists(converted_path):
    	makedirs(converted_path)
#convert files
fileindex=0;
for filename in files:
	digits=2
	print "{0}{1:{2}}%".format(
					"\b" * (digits + 1+1), 
					int((fileindex+0.0)/(len(files))*100),
					digits),
	fileindex=fileindex+1;
	sys.stdout.flush()
	f=open(mypath+"/"+filename,"r");
	w=open(converted_path+"/"+filename,"w");
	for line in f:
		cells=line.split(' ');
		for cell in cells:
			if(cell!='NA'):
				try:
					value=float(cell);
					w.write(cell+" ");
				except ValueError:
					continue;
	f.close();
	w.close();