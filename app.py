import streamlit as st
import preprocess
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("WhatsApp Chat Analyzer")
uploaded_data = st.sidebar.file_uploader('upload your file')

if uploaded_data is not None:
    chat = uploaded_data.getvalue()
    st.sidebar.write("File uploaded successfully!")
    data = chat.decode('utf-8')
    df = preprocess.preprocess(data)
    # st.dataframe(df)
    st.title('Top statistics')
    # fetch the unique users
    sender_list = df['Sender'].unique().tolist()
    sender_list.sort()
    sender_list.insert(0, 'Overall')
    selected_user = st.sidebar.selectbox('Show analysis wrt', sender_list)

    # starting the analysis
    if st.sidebar.button('Show Analysis'):
        num_messages, words, media_mess, link = helper.fetch_stats(selected_user, df)
        # st.sidebar.write("Total Messages: ", num_messages)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header('total messages')
            st.title(num_messages)
        with col2:
            st.header('total words')
            st.title(words)
        with col3:
            st.header('total media messages')
            st.title(media_mess)
        with col4:
            st.header('total links')
            st.title(link)
        # Timeline
        st.title('Monthly timeline')
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['count'], color='blue')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)
        # Activity map
        st.title('Activity map')
        col1, col2 = st.columns(2)
        with col1:
            st.header('most busy day')
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='orange')
            ax.set_xticklabels(busy_day.index, rotation=90)
            st.pyplot(fig)
        with col2:
            st.header('most busy month')
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='red')
            ax.set_xticklabels(busy_month.index, rotation=90)
            st.pyplot(fig)

        # Activity heatmap
        st.title('Activity heatmap')
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap, cmap='Blues')
        st.pyplot(fig)
        # fetching the most active users
        if selected_user == 'Overall':
            x, new_df = helper.most_velle(df)
            
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)
            with col1:
                st.title('Most active users')
                ax.bar(x.index, x.values)
                plt.xticks(rotation=90)
                st.pyplot(fig)
            with col2:
                st.title('Contribution of users')
                st.dataframe(new_df)
        st.title('Most common words')
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Emoji analysis

        emoji_df = helper.emoji_helper(selected_user, df)
        st.title('Emoji analysis')
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct='%1.1f%%')
            st.pyplot(fig)