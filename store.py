import numpy as np
import pandas as pd
import openpyxl 
import xlsxwriter

def stor(z):
	b=[]
	g=[]
	r=[]
	for i in range(0,len(z)):
		b.append(z[i][0])
		g.append(z[i][1])
		r.append(z[i][2])
	data = {'B':b, 'G':g, 'R':r}
	da = pd.DataFrame(data)
	da.to_excel('Blue_bgr_U.xlsx',sheet_name ='Blue')
	#da.to_excel('Green_bgr_U_R.xlsx',sheet_name ='Green')
	#da.to_excel('Red_bgr_U.xlsx',sheet_name ='White')
	
