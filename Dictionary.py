from PyDictionary import PyDictionary as pd

py_dict = pd()
meaning = py_dict.meaning("programming")
for i in meaning:
	print(i + ' : ')
	for j in meaning[i]:
		print('\t'*3 + j)
