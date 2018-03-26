import math
from data import pref_by_movie


def Pearson(pref, movie1, movie2):
    # 找出对两部电影都评论的人
    people_list = [person for person in pref[movie1].keys()
                   if person in pref[movie2].keys()]
    n = len(people_list)
    if n == 0:
        return 0
    # 计算评价和
    sum1 = sum([pref[movie1][person] for person in people_list])
    sum2 = sum([pref[movie2][person] for person in people_list])
    # 计算评价平方和
    sumSq1 = sum([pref[movie1][person] ** 2 for person in people_list])
    sumSq2 = sum([pref[movie2][person] ** 2 for person in people_list])
    # 计算评价成绩和
    psum = sum([pref[movie1][person] * pref[movie2][person]
                for person in people_list])
    # 皮尔逊相关系数计算
    num = psum - sum1 * sum2 / n
    den = math.sqrt((sumSq1 - (sum1 ** 2) / n) * (sumSq2 - (sum2 ** 2) / n))

    if den == 0:
        return 0
    return num / den

def TopMatch(pref, movie, n = 10):
    #计算给电影和每部电影的皮尔逊相关系数
    scores = [(Pearson(pref_by_movie, movie, mov), mov) for mov in pref_by_movie.keys() if mov != movie]
    #根据系数进行排序，并由大到小排序
    scores.sort(key = lambda x:x[0], reverse = True)
    return scores[0:n]

def CreateMatchList(pref = pref_by_movie):
    match_list = {}
    for movie in pref.keys():
        match_list[movie] = TopMatch(pref, movie, 10)
    return match_list

match_list = CreateMatchList()


f = open('temp.txt','w',encoding='utf-8')  
f.write(str(match_list))  
f.close()