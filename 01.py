file=r"C:\Users\k1-on\Documents\Python World\bank 2\month.txt"
f = open(file, "r")

j=f.read()
month='2409'

#miles=[x for x in j if 'miles' in x.casefold()]

by61=j.split('61:')


def caller (name):
	inmiles=[x for x in by61 if name in x.casefold()]
	datesnmoneys=[x[:22] for x in inmiles if month in x]
	datesnmoneys=map(lambda x:x.partition('DR')[2],datesnmoneys)
	numbers=[]
	for i in datesnmoneys:
		jj=[x for x in i if x.isdigit() or x == ',']
		jj=''.join(jj)
		jj=jj.replace(',','.')

		numbers.append(float(jj))
	return(f'Total for {name} is {sum(numbers):.2f}')

def empty ():
	inmiles=[x for x in by61]
	
	datesnmoneys=[x[:22] for x in inmiles if month in x]

	datesnmoneys=map(lambda x:x.partition('DR')[2],datesnmoneys)
	#print(list(datesnmoneys))
	numbers=[]

	for i in datesnmoneys:
		if not i =='':
			jj=[x for x in i if x.isdigit() or x == ',']

			jj=''.join(jj)

			jj=jj.replace(',','.')
			numbers.append(float(jj))

	
	
	return(f'Overall expenses total {sum(numbers):.2f}')



print(caller('miles'),caller('wolt'),caller('lidl'),caller('budni'),empty(),sep='\n')