import os
import gzip
import csv
import pandas as pd


#find list of folders (1 folder = 1 register) that need to be combined
folder_list = os.listdir('data')
if '.DS_Store' in folder_list: folder_list.remove('.DS_Store')

filename = '1.gz'  
headers = ['date', 'time', 'x-edge-location', 'sc-bytes', 'c-ip', 'cs-method', 'cs(Host)', 'cs-uri-stem', 'sc-status', 'cs(Referer)', 'cs(User-Agent)', 'cs-uri-query', 'cs(Cookie)', 'x-edge-result-type', 'x-edge-request-id', 'x-host-header', 'cs-protocol', 'cs-bytes', 'time-taken', 'x-forwarded-for', 'ssl-protocol', 'ssl-cipher', 'x-edge-response-result-type', 'cs-protocol-version', 'fle-status', 'fle-encrypted-fields']


main_data = pd.read_csv('headers.tsv',delimiter='\t',encoding='utf-8')

#read file and remove first 2 rows
def read_from_gz(filename, foldername):
	l = []
	with gzip.open(foldername + '/' + filename) as f:
		data_to_append = pd.read_csv(foldername + '/' +filename,names=headers,delimiter='\t',skiprows=2,encoding='utf-8',compression='gzip')
		#data_to_append= data_to_append.replace('-','')
		#data_to_append=data_to_append.fillna('')
		return pd.concat([main_data,data_to_append])


counter = 0
count = 0
for folder in folder_list:
	file_list = os.listdir('data/'+folder)
	if '.DS_Store' in file_list: file_list.remove('.DS_Store')
	for file in file_list:
		main_data=read_from_gz(file,'data/'+folder)
		main_data = main_data.replace('-','')
		main_data = main_data.fillna('')
		counter +=1
		if counter >100:
			count +=1
			print(str(count) + '00 files have been added and I am currently importing '+ folder)
			counter = counter-100
	main_data.to_csv('dataworker_files/'+folder+'.csv',encoding='utf-8')
	main_data=pd.read_csv('headers.tsv',delimiter='\t',encoding='utf-8')













"""
file_list = [[]]
for i in folder_list:
	file_list =[i, os.listdir('data/' + i)]
	print(file_list)


file_list = []
for foldername in folder_list:
	file_list = os.listdir('data/' + foldername)
	while '.DS_Store' in file_list: 
		file_list.remove('.DS_Store')
	os.walk(foldername)
	for filename in file_list:
		data=pd.read_csv(filename)



"""
print('done')	
