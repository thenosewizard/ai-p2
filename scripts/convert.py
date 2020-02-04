#converts json to csv
import json  
import pandas as pd  
from pandas.io.json import json_normalize 

fileNamePath = "./overCooked"
extensionJs = ".json"
exttensionCsv = ".csv"

def convertFile(fileNamePath):
	with open(fileNamePath + extensionJs) as f:
		d = json.load(f)
	df_steam = []
	for i in range(len(d)):
		df_1 = json_normalize(d[i])
		df_steam.append(df_1)
	df = pd.concat(df_steam)
	print(df)
	df.to_csv(r''+fileNamePath+exttensionCsv)

convertFile(fileNamePath)