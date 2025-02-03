from fuzzywuzzy import fuzz
from fuzzywuzzy import process
s1 = "I love fuzzywuzzys"
s2 = "I am loveing fuzzywuzzys"
print ("Fuzzywuzzy Ratio:", fuzz.ratio(s1,s2))
print ("FuzzywuzzyParialRatio:" ,fuzz.partial_ratio(s1,s2))
print ("FuzzywuzzyTokenSortRatio:" ,fuzz.token_sort_ratio(s1,s2))
print ("FuzzywuzzyTokenSortRatio:", fuzz.token_sort_ratio(s1,s2))
print ("FuzzywuzzyWRatio:" ,fuzz.WRatio(s1,s2))
query ='fuzzy for fuzzys'
choices=['fuzzy for fuzzy' , 'fuzzy fuzzy','g. for fuzzys']
print("list of ratio:") 
print(process.extract(query,choices),'\n')
print("best among the above list:",process.extractOne(query,choices))

#pip install fuzzywuzzy
