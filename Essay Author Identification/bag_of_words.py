def text_extraction():
	import os

	import pickle

	dict_1 = {}


	import docx
	
	Document = docx.Document

	two = 0
	docs__ = 0

	current_dir = os.getcwd()

	current_folder = "DUMP"



	dict_2 = open("dictionary","w")

	dict_3 = open("dictionary-3","w")

	temp_dict = {}


	for folders in os.listdir(current_dir+"\ ".strip()+current_folder):
		sa = 0
		for files in os.listdir(current_dir+"\ ".strip()+current_folder+"\ ".strip()+folders):	
			file_format = files[len(files)-4:]
			sa+=1

			file_name = os.getcwd()+"\ ".strip()+"DUMP"+"\ ".strip()+folders+"\ ".strip()+files
			
			docs__+=1

			document = Document(file_name)

			text_ = ' '.join(paragraph.text.encode('utf-8').replace("\n",' ').replace(".",' ').replace(",",' ') for paragraph in document.paragraphs)

			try:
				temp_dict[folders]+=" "+text_
			except KeyError:
				temp_dict[folders]=text_

			try:
				dict_1[folders].append(text_)
			except KeyError:
				dict_1[folders]=[text_]

	pickle.dump(dict_1,dict_2)
	pickle.dump(temp_dict,dict_3)

	dict_2.close()
	dict_3.close()




