'''
Write a Pandas Program To Add Some Data To An Existing Series. 
'''

import pandas as pd

if __name__=="__main__":
	ps = pd.Series([1,2,3,4,5,6])
	print(ps)
	ps_updated = ps.append(pd.Series([7,8,9]))
	print(ps_updated)
