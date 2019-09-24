
# import pandas as pd
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from nltk import tokenize
# import csv
# import matplotlib.pyplot as plt
# import nltk 
# #nltk.download('vader_lexicon')

# data = pd.read_csv('C:/Users/mayank/Desktop/reviews_1.csv')
# Comments = data['ReviewText'].head(100)
# sid = SentimentIntensityAnalyzer()

# w = csv.writer(open("Comments.csv", "w", encoding = 'utf-8', newline = ''))
# count = 1
# for comment in Comments:
# 	if count == 1:
# 		w.writerow(['Comment', 'pos', 'neg', 'neu'])
# 		count += 1
# 	else:
# 		ss = sid.polarity_scores(comment)
# 		values = []
# 		for key,value in ss.items():
# 			values.append((value))
			
# 		w.writerow([comment, values[2], values[0], values[1]])


import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import csv
import matplotlib.pyplot as plt
import nltk 
#nltk.download('vader_lexicon')

data = pd.read_csv('C:/Users/mayank/Desktop/reviews_1.csv')
Comments = data['ReviewText'].head(100)
print(Comments)
sid = SentimentIntensityAnalyzer()

w = csv.writer(open("Comments.csv", "a", newline = ''))
count = 1
for comment in Comments:
	if count == 1:
		w.writerow(['Comment', 'pos', 'neg', 'neu'])
		count += 1
	else:
		if(str(comment) != 'nan'):

			ss = sid.polarity_scores(comment)
			values = []
			for key,value in ss.items():
				values.append((value))
				
			w.writerow([comment, values[2], values[0], values[1]])
# for i in Comments:
    
#     if (str(i) != 'nan'):


#         print((i))
