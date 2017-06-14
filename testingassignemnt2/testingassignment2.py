from pandas import DataFrame, Series
import pandas as pd

tab_movies = pd.read_table('movies.dat', sep='::', engine='python', header=0, names=['movie_id', 'title', 'genres'])
tab_ratings = pd.read_table('ratings.dat', sep='::', engine='python', header=0, names=['user_id', 'movie_id', 'rating', 'timestamp'])
tab_users = pd.read_table('users.dat', sep='::', engine='python', header=0, names=['user_id', 'gender', 'age', 'occupation', 'zip'])

df_movies = DataFrame(tab_movies)
df_ratings = DataFrame(tab_ratings)
df_users = DataFrame(tab_users)

df_combined = df_movies.merge(df_ratings, how='inner', on='movie_id').merge(df_users, how='inner', on='user_id')


#1
#print(len(df_movies.drop_duplicates()))

#2 belakangan
#print(df_combined)

#3
#print(len(df_users['occupation'].unique()))

#4
#print(df_users['occupation'].value_counts())

#5
# grouped = df_combined.groupby('gender')
# male_group = DataFrame(grouped.get_group('M'))
# female_group = DataFrame(grouped.get_group('F'))
# mean_rating_male = male_group['rating'].mean()
# mean_rating_female = female_group['rating'].mean()
# print(mean_rating_male)
#6
#print(abs(mean_rating_female-mean_rating_male))

#7
def categorize(x):
    return ('Young' if (x <= 10) else 'Youth' if(11 <= x <= 20) else 'Adult' if (21 <= x <= 65) else 'Senior')

df_users['category'] = df_users['age'].map(categorize)
print(df_users['category'].value_counts())

#8
# print(df_users.groupby(['category','gender']).size())