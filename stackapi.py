import requests
import json
from bs4 import BeautifulSoup 
#import pandas as pd
from googlesearch import search

staccoverflow="  stackoverflow"
# to search
query =input('Enter your question\n')
query=query+staccoverflow
print(query)
#query = "Keyerror items  stackoverflow"
list_ids=[]
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    if "stackoverflow.com" in j:
        print(j)
        l=j.split('/')
        print(l[4])
        list_ids.append(l[4])


    
'''
#search=input('Enter your question\n')

search='what pointer?'
response = requests.get(f'https://api.stackexchange.com/2.2/similar?order=desc&sort=relevance&title={search}&site=stackoverflow')
df=pd.DataFrame.from_dict(response.json()['items'])
#finaldata=df.sort_values('view_count',ascending=True)
print(df.iloc[0])



for ques in response.json()['items']:
    print(ques['is_answered'])
    if ques['is_answered']==True:
        print(ques['title'],ques['link'],"\n")
        id=ques['question_id']
        print(id)
        break
'''
for id in range(0,2): 
    url=f'https://api.stackexchange.com/2.2/questions/{list_ids[id]}?&site=stackoverflow&filter=%21T%2ahPNRA69ofM1izkPP'
    response1 = requests.get(url)
    print(response1)
    for ans in response1.json()['items'] :
        print(ans['link'])
        for i in ans['answers']:
            #print(i['title'])
            soup = BeautifulSoup(i['body'],features="html.parser")
            print(soup.get_text())
            #print(i['body'].content)
            break
