import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Data from csv file
df = pd.read_csv(r'D:\Py Lib. 21Aug25\3Matplotlib\Netflix Dataset.csv', encoding='latin1')

#clean Data
df=df.dropna(subset=['Category','Title','Director','Cast','Country','Release_Date','Rating','Duration','Type','Description'])

#Bar Chart
type_counts=df['Category'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('Number of Movies Vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('moviesVsTV.png')
#plt.show()

#Pie Chart
rating_counts=df['Rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title('Percentage of Content Ratings')
plt.savefig('Content Rating')
#plt.show()

#H    Comedies



movie_df=df[df['Type']=='Comedies'].copy()
movie_df['duration_int']=movie_df['Duration'].str.replace(' min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='Black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movies_duration_histogram.png')
plt.show()


# Release date movies Count
release_counts=df['Release_Date'].value_counts().sort_index().head(20)
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title('Release Year Vs number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release_year_Scatter.png')
plt.show()

# Contry by Realese Movies Per Years

country_counts=df['Country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color='teal')
plt.title('Top 10 contries by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('contry')
plt.tight_layout()
plt.savefig('Top10_Contries.png')
plt.show()

#

content_by_year=df.groupby(['Release_Date','Type']).size().unstack().fillna(0)

fig, ax=plt.subplots(1,2,figsize=(12,5))

#first subplot : movies
ax[0].plot(content_by_year.index,content_by_year['Comedies'],color='blue')
ax[0].set_title('Comedies Released per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')


#Second subplot : movies
ax[0].plot(content_by_year.index,content_by_year['Dramas'],color='Red')
ax[0].set_title('Dramas Released per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

fig.suptitle('Comparision of movies and Tv Shows Released Over Years')

plt.tight_layout()
plt.savefig('Movies_Tv_Shows_Comparison.png')
plt.show()
