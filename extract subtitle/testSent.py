from textblob import TextBlob
from nltk.util import pr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv(r'C:\Users\world\Downloads\data\data_test.csv')
print(df)
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
print(df['Emotion'].value_counts())
plt.plot(kind='bar')
print(df['Emotion'].value_counts().plot(kind='bar'))
plt.show()
#sns.countplot(df['Emotion'])
plt.figure(figsize=(20,10))
sns.countplot(x='Emotion', data=df)
plt.show()


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment >0:
        result= "pos"
    elif sentiment <0:
        result= "neg"
    else:
        result = "neutral"
        
    return result

print(get_sentiment("i love coding"))

df['Sentiment'] = df['Text'].apply(get_sentiment)

print(df.head())


print(df.groupby(['Emotion', 'Sentiment']).size())
print(df.groupby(['Emotion', 'Sentiment']).size().plot(kind='bar'))

# sns.factorplot
# sns.catplot
# sns.factorplot(x= 'Emotion',hue='Sentiment',data=df, kind='count',size=6, aspect=1.5)


