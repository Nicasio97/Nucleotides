def one_word_please(list):
	word = ""
	for x in list:
		word = word + x
	return word
def one_list_please(word):
	list=[]
	for x in word:
		list.append(x)
	return list		

def _get_file_lines_in_one(file,deleteFirstLine = False):
	a = ""
	with open(file, "r") as f:
		f_lines = f.readlines()
	if deleteFirstLine == True:	
		del f_lines[0]
	a=one_word_please(f_lines) 
	return a
def get_file_characters(file,deleteFirstLine=False,toWord=False):
	a = _get_file_lines_in_one("sequence1.dna",deleteFirstLine)
	list1=one_list_please(a)
	list2 = [a for a in list1 if a != '\n']
	if toWord==False:
		return list2
	else:
		return one_word_please(list2)

def _get_complementary_nucleotide(nucleotid):
	if nucleotid == "a" or nucleotid == "A":
		return "t"
	elif nucleotid == "t" or nucleotid == "T":
		return "a"
	elif nucleotid == "c" or nucleotid == "C":
		return "g"
	elif nucleotid == "g" or nucleotid == "G":
		return "c"
	else:
		pass	
def get_complementary_sequence(word):
	word2 = ''	
	for x in word:						
		word2=word2+_get_complementary_nucleotide(x) #changing order of sum elements altere order					
	return word2
def get_reversed_list(list):
	list.reverse()
	return list

def add_something_every_70bp(string,something,beginning=0,every=70):
	#Something=" " or "\n" or "\\n"
	word=""	
	i=1
	for item in string:
		word = word + item
		num=i-beginning		
		if num % every == 0:
			word = word + something
		i+=1
	return word			
	