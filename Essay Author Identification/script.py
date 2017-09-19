from __future__ import division


import pickle



import os 


no_roculmns = -1

dict_1 = {}

file_names = []

def get_folder_names():	

	global no_roculmns
	global dict_1


	base_path = os.getcwd()

	for file in os.listdir(os.getcwd()):
		if file!="script.py":
			l=file.split(".zip")
			if len(l)!=2:
				if l[0][:2]=="SS":
					file_names.append(l[0])
					no_roculmns+=1
					dict_1[l[0]]=[]




no_rows = -1

roll_numbers = range(1,149)

roll_numbers = [str(num) for num in roll_numbers]

def generate_roll_numbers():
	global roll_numbers

	for j in xrange(len(roll_numbers)):
		n = roll_numbers[j]
		if len(n)==3:
			pass
		if len(n)==2:
			n="0"+n
		if len(n)==1:
			n="00"+n
		roll_numbers[j]="IH201685"+n



suspects = []


def get_file_names():

	global suspects

	global dict_1
	global file_names
	global count_2

	sub = 0
	for t in file_names:
		path = os.getcwd()+"\ ".strip()+t
	
		list_1 = dict_1[t]
		try:
			for d in os.listdir(path):
				fail = True
				for numbers in roll_numbers:
					if numbers in d:
						fail = False
						list_1.append(numbers)
				if fail:
					suspects.append([d,path])
				sub+=1	
			dict_1[t]=list_1
		except WindowsError:
			pass

dict_2 = {}

def form_dict2():

	global roll_numbers
	global dict_1
	global dict_2


	for nub in roll_numbers:
		dict_2[nub]=-1

	r=0
	for tas in dict_1:
		r+=len(dict_1[tas])
		for number in dict_1[tas]:
			# print number
			dict_2[number]+=1

	for student in sorted(dict_2.keys()):
		if dict_2[student]!=-1:
			pass

	
def copy_objects_to_file():
	project_file_1 = open("student_details","w")

	global dict_1
	global dict_2
	# global project_file_1
	global file_names

	pickle.dump(dict_1,project_file_1)
	pickle.dump(dict_2,project_file_1)
	pickle.dump(file_names,project_file_1)
	project_file_1.close()

def convert_to_csv():
	global dict_1
	global dict_2
	global file_names
	global roll_numbers

	try:
		p=open("files.csv","w")
		p.write("roll_numbres,"+",".join(sd for sd in file_names)+"\n")
		for numbers_ in roll_numbers:
			list_1 = []
			for b in file_names:
				if numbers_ in dict_1[b]:
					list_1.append(1)
				else:
					list_1.append(0)
			if dict_2[numbers_]!=-1:
				p.write(numbers_+","+",".join(str(g) for g in list_1)+"\n")
		# print "done"
		p.close()
	except IOError:
		pass





get_folder_names()

generate_roll_numbers()


get_file_names()

form_dict2()

copy_objects_to_file()


convert_to_csv()
