import csv
from itertools import islice


movie_list = {}
with open('./ml-latest-small/movies.csv', "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for line in islice(reader, 1, None):
        (mid, title) = line[0:2]
        movie_list[mid] = title

pref_by_people = {}
with open('./ml-latest-small/ratings.csv', "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for line in islice(reader, 1, None):
        (uid, mid, rating) = line[0:3]
        if not uid in pref_by_people.keys():
            pref_by_people[uid] = {}
        pref_by_people[uid][movie_list[mid]] = float(rating)

f = open('people_movies.txt','w',encoding='utf-8')  
f.write(str(pref_by_people))  
f.close()

def TransfromPref(pref):
    re_pref = {}
    for k1, v1 in pref.items():
        for k2, v2 in v1.items():
            if not k2 in re_pref.keys():
                re_pref[k2] = {}
            re_pref[k2][k1] = v2
    return re_pref


pref_by_movie = TransfromPref(pref_by_people)