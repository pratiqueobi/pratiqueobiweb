#!/usr/bin/python
# coding=utf-8
import os
new = ""
path = "/home/ana/PS2/praticandoOBI/praticandoOBI/scripts/criajson/enunciados/"
for filename in os.listdir(path):
	print (filename)
	for filename1 in os.listdir(path+filename):
		print (filename1)
		path2 = path+filename+"/"+filename1+"/"
		for filename2 in os.listdir(path2):
			print (filename2)
			with open(path2+filename2) as f:
				with open(path2+filename2, "w") as f1:
					titulo = f.readline()
					print(titulo)
					f1.write(titulo)
					while True:
						new = f.readline().replace('\n','')
						print(new)
						f1.write(new)
						if not new:
							break
			
			#	f1.write(titulo)
			#	f1.write(new)


