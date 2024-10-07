file=r"C:\Users\k1-on\Documents\Python World\bank 2\month.txt"
f = open(file, "r")

j=f.read()
month='2409'
items=['miles','wolt','lidl','budni','urban sports']


#data base preperation, output is filered entries that start with a date and amounts
generalentries=j.split('61:')
filteredentries=[x for x in generalentries if x[:10].isdigit()]


def analyser(entries,month,categories):
	focused=[x for x in entries if x[:4]==month]
	listofcategories=[]
	mydict=dict()

	for i in categories:
		thislist=[]
		for j in focused:
			if i in j.casefold():
				thislist.append(j)
		mydict.update({i:thislist})

	#TODO: need to create a category for OTHER 
	return(mydict)
		


	

for key, value in analyser(filteredentries,month,items).items():
    print(key+'\n\n',*value,'\n\n **********END*******')

