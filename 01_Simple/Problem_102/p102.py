'''
Write A Python Program To Sort Student Name 
In Ascending Order In List And Student Should 
Display Which Contain Only 5 Character
'''

if __name__=="__main__":
	std_list = ['aliee','kami','faisa','faiz','yash']
	std_list.sort()
	print(std_list)
	
	for i in std_list:
		  if(len(i) == 5):
		      print(i)
