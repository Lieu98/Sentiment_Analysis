import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np



d= pd.read_csv('C:/projects_&_practice/ibm-spss/project-AirBnb/Analysed_Comments.csv')
pos = d['pos']
neg = d['neg']
neu  = d['neu']

count_pos=0
count_neg=0
count_neu=0
for i in range(len(d)):




	if pos[i]>neg[i]:
		if pos[i]>neu[i]:
			count_pos +=1
		elif neu[i]>pos[i]:
			count_neu +=1
	else:

		count_neg +=1

print(count_pos)
print(count_neg)
print(count_neu)
label=['count_neu', 'count_neg', 'count_pos']
count = [count_neu, count_neg, count_pos]
index = np.arange(3)
plt.bar(index, count)
plt.xlabel('Polarity', fontsize=15)
plt.ylabel('Frequency', fontsize=15)   
plt.xticks(index, label, fontsize=10, rotation=0)
plt.show()

# index = np.arange(len(label))
#     plt.bar(index, no_movies)
#     plt.xlabel('Genre', fontsize=5)
#     plt.ylabel('No of Movies', fontsize=5)
#     plt.xticks(index, label, fontsize=5, rotation=30)
#     plt.title('Market Share for Each Genre 1995-2017')
#     plt.show()