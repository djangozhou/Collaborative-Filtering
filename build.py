#!/usr/bin/python3
from data import pref_by_people



f = open('./temp.txt','r',encoding='utf-8')
a = f.read()
match_list = eval(a)
f.close()

def get_recommanded_items(pref = pref_by_people, match_list = match_list, user = '1'):
    try:
        user_ratings = pref[user] #找出用户看过的电影与评价
    except KeyError:
        print("no user")
        return 0
    scores = {} #记录加权和
    totalsim = {} #记录评分和

    for movie, rating in user_ratings.items(): #遍历当前用户评分电影
        for sim, sim_movie in match_list[movie]: #遍历当前电影相近电影
            if sim_movie in user_ratings.keys(): #如果用户看过该电影，跳出本次循环
                continue
             #记录加权和与评分和
            if not sim_movie in scores.keys():
                scores[sim_movie] = sim * rating
                totalsim[sim_movie] = sim 
            scores[sim_movie] += sim * rating
            totalsim[sim_movie] += sim

    rankings = [(scores[sim_movie]/totalsim[sim_movie], sim_movie) for sim_movie in scores.keys() if totalsim[sim_movie] != 0]
    #排序并取前5
    rankings.sort(key=lambda x:x[0], reverse=True)
    return rankings[0:5]

userID = input('请输入用户ID：')
print(get_recommanded_items(pref_by_people,match_list,userID))