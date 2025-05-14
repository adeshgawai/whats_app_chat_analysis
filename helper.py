import re
from wordcloud import WordCloud
from collections import Counter
import emoji
import pandas as pd
def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Sender'] == selected_user]
    # 1. we are fetching the no of messages
    num_messages = df.shape[0]
    # 2. we are fetching the no of words
    word = []
    for message in df['Message']:
        word.extend(message.split())
    # 3. fetching the no of media messages
    media_message = df[df['Message'] == '<Media omitted>'].shape[0]

    # 4. fetching the no of links
    link = []
    pattern = r'(https?://\S+|www\.\S+)'
    for message in df['Message']:
        if re.findall(pattern, message):
            link.append(message)
    return num_messages, len(word), media_message, len(link)
def most_velle(data):
    u = data['Sender'].value_counts().head()
    df = round((data['Sender'].value_counts()/data.shape[0])*100, 2).reset_index().rename(columns={'count':'percent'})

    return u, df
def create_wordcloud(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Sender'] == selected_user]
    df = df[~df['Message'].str.lower().str.contains('media omitted')]
    # configure wordcloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    # generate wordcloud
    df_wc = wc.generate(df['Message'].str.cat(sep=''))
    return wc
def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Sender'] == selected_user]
    
    emojis = []
    for message in df['Message']:
        emojis.extend([char for char in message if emoji.is_emoji(char)])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Sender'] == selected_user]
    timeline = df.groupby(['year','month_num', 'month']).count()['Message'].reset_index().rename(columns={'Message':'count'})
    # we will merge month and year
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + '-'+ str(timeline['year'][i]))
    timeline['time'] = time
    return timeline
def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Sender'] == selected_user]
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Sender'] == selected_user]
    return df['month'].value_counts()
def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['Sender'] == selected_user]
    activityHmap=df.pivot_table(index='day_name', columns='period', values='Message', aggfunc='count').fillna(0)
    return activityHmap


    