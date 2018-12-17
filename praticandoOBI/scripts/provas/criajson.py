#!/usr/bin/python
# coding=utf-8
import os
ano = "2017"
path = "/home/ana/PS2/praticandoOBI/praticandoOBI/scripts/criajson/enunciados/"+ano+"/"
outputfile = "/home/ana/PS2/praticandoOBI/praticandoOBI/scripts/criajson/jsons/"+ano+"/"
header = "{\n\t\"anoprova\":"+ ano + ",\n\t\"nivelprova\": 1,\n\t\"faseprova\": 2,\n\t\"problemas\": [{\n\t\t\"tituloproblema\": \""
regras = ""
resto = "/home/ana/PS2/praticandoOBI/praticandoOBI/scripts/criajson/resto.json"
anotext = "{\n\"anoprova\": "
niveltext = ",\n\"nivelprova\": "
fasetext= ",\n\"faseprova\": "
header = ",\n\"problemas\": ["
headerprob = "{\n\t\t\"tituloproblema\": \""

for filename in sorted(os.listdir(path)):
	print(filename)
	if(filename == "f1n1"):
		fase = "1"
		nivel = "1"
	elif(filename == "f1n2"):
		fase = "1"
		nivel = "2"
	elif(filename == "f2n1"):
		fase = "2"
		nivel = "1"
	else:
		fase = "2"
		nivel = "2"
	with open(outputfile+filename+".json", "w") as out:
		out.write(anotext+ano+niveltext+nivel+fasetext+fase+header)
		for filename1 in sorted(os.listdir(path+filename)):
			print(filename1)
			out.write(headerprob)
			path2 = path+filename+"/"+filename1

			with open(path2) as f:
				titulo = f.readline().replace('\n','')
				out.write(titulo+"\",\n\t\t\"enunciadoproblema\": \"")
				enunciado = f.readline().replace('\n','')
				out.write(enunciado+"\",\n\t\t\"regrasproblema\": \"")
				while True:
					regras = f.readline().replace('\n','\\n')
					out.write(regras)
					if not regras:
						break
				out.write("\",\n")
				with open(resto, "r") as f1:
					t = f1.readlines()
				out.writelines(t)
		out.write("]\n}")
