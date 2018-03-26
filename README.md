# 《基于协同过滤算法的电影推荐系统》

### 本科毕业设计《基于协同过滤算法的电影推荐系统》

样本数据来源：[Movielens](https://grouplens.org/datasets/movielens/)

- ## 样本数据详情(10,000条评价，9,000部电影，700用户)
    - ### ml-latest-small/ratings.csv: 用户评价详情，包含4个title：userId,movieId,rating,timestamp
    - ### ml-latest-small/movies.csv: 电影详情，包含三个title：movieId,title,genres

- ## 计算方法
    - ### 采用基于项目的协同滤波算法（item-based collaborative filtering ,itemCF）,步骤如下：

        - data.py

            - 从两个.csv文件中读取相关数据，存入两个字典中：movie_list、pref_by_people。
            - 将数据按照 电影：[评价用户]构造一个新的字典：pref_by_movie。

        - file.py（主要步骤）

            -计算出每部电影的相似度，根据皮尔逊相似系数将每部电影的最相似的10部电影筛选出来，存入一个字典
        - build.py

            - 处理用户输入，将与每个用户观看过的影片近似程度高的5部电影筛选出来，推荐给用户。

