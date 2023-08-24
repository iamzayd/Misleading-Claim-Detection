import streamlit as st
from googleapiclient.discovery import build
import pandas as pd
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import praw
st.set_page_config(layout="wide")
# Your API key
api_key = "AIzaSyAncltA5JKsvH9PKJV3Tvz27EabFjWsYdw"
youtube = build('youtube', 'v3', developerKey=api_key)

sid = SentimentIntensityAnalyzer()

def sentiment_Vader(text):
            over_all_polarity = sid.polarity_scores(text)
            if over_all_polarity['compound'] >= 0.05:
                return "positive"
            elif over_all_polarity['compound'] <= -0.05:
                return "negative"
            else:
                return "neutral"


# Function to extract video ID
def extract_video_id(youtube_link):
    if "youtu.be" in youtube_link:
        video_id = youtube_link.split("/")[-1]
    else:
        query_string = youtube_link.split("?")[1]
        params = query_string.split("&")
        for param in params:
            key, value = param.split("=")
            if key == "v":
                video_id = value
                break
    return video_id



def clean_text(text):
    # Remove HTML tags
    cleaned_text = re.sub(r'<.*?>', '', text)
    
    # Remove non-alphanumeric characters except spaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)
    
    # Convert text to lowercase
    cleaned_text = cleaned_text.lower()
    
    return cleaned_text


# Recursive function to get all replies in a comment thread
def get_replies(comment_id, token):
    replies_response = youtube.comments().list(part='snippet', maxResults=100, parentId=comment_id, pageToken=token).execute()

    for reply in replies_response['items']:
        all_comments.append({
            'Comment': reply['snippet']['textDisplay'],
            'Likes': reply['snippet']['likeCount'],
            'Date': reply['snippet']['publishedAt']
        })

    if replies_response.get("nextPageToken"):
        return get_replies(comment_id, replies_response['nextPageToken'])
    else:
        return []


# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



st.sidebar.write("*Sample YouTube Link:*")
st.sidebar.write("https://www.youtube.com/watch?v=oGkM7XY3aus&ab_channel=PushkarRajThakur%3ABusinessCoach")

st.sidebar.write("*Sample Reddit Link:*")
st.sidebar.write("https://www.reddit.com/r/IndiaInvestments/comments/15y4st4/lets_talk_about_email_accounts_for_investments/")
st.sidebar.write("-----------------")
st.sidebar.markdown('''
Created with 💜 by [Najeeb](https://www.instagram.com/thiscloudbook/) And [Karthik](https://www.instagram.com/_mr_thop/).
''')

# Recursive function to get all comments
def get_comments(youtube, video_id, next_view_token):
    global all_comments

    if len(next_view_token.strip()) == 0:
        all_comments = []

    if next_view_token == '':
        comment_list = youtube.commentThreads().list(part='snippet', maxResults=100, videoId=video_id, order='relevance').execute()
    else:
        comment_list = youtube.commentThreads().list(part='snippet', maxResults=100, videoId=video_id, order='relevance', pageToken=next_view_token).execute()

    for comment in comment_list['items']:
        comment_data = {
            'Comment': comment['snippet']['topLevelComment']['snippet']['textDisplay'],
            'Likes': comment['snippet']['topLevelComment']['snippet']['likeCount'],
            'Date': comment['snippet']['topLevelComment']['snippet']['publishedAt']
        }
        all_comments.append(comment_data)
        reply_count = comment['snippet']['totalReplyCount']
        all_replies = []

        if reply_count > 0:
            replies_list = youtube.comments().list(part='snippet', maxResults=100, parentId=comment['id']).execute()
            for reply in replies_list['items']:
                all_replies.append({
                    'Comment': reply['snippet']['textDisplay'],
                    'Likes': reply['snippet']['likeCount'],
                    'Date': reply['snippet']['publishedAt']
                })

            while "nextPageToken" in replies_list:
                token_reply = replies_list['nextPageToken']
                replies_list = youtube.comments().list(part='snippet', maxResults=100, parentId=comment['id'], pageToken=token_reply).execute()
                for reply in replies_list['items']:
                    all_replies.append({
                        'Comment': reply['snippet']['textDisplay'],
                        'Likes': reply['snippet']['likeCount'],
                        'Date': reply['snippet']['publishedAt']
                    })

        comment_data['Replies'] = all_replies
        comment_data['NumReplies'] = reply_count  # New line to add the number of replies to comment_data

    if "nextPageToken" in comment_list:
        return get_comments(youtube, video_id, comment_list['nextPageToken'])
    else:
        return []

# Streamlit UI
def main():

    value = "False"

    st.title("Misleading Claim Detection")
    

    listTabs = ['Detection (Youtube)','Visualization','Detection (Reddit)']
    tab1, tab2, tab3 = st.tabs(listTabs)
    with tab1:
        st.write("*For Content related to Youtube*")
        youtube_link = st.text_input("Enter YouTube Video Link:")
        
        try:
            if st.button("Detect Claim"): 
            
                video_id = extract_video_id(youtube_link)

                # Print video details
                video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
                video_title = video_response['items'][0]['snippet']['title']
                channel_title = video_response['items'][0]['snippet']['channelTitle']  # Extract the channel title
                video_likes = int(video_response['items'][0]['statistics']['likeCount'])

                channel_id = video_response['items'][0]['snippet']['channelId']
                channel_response = youtube.channels().list(part='snippet,statistics', id=channel_id).execute()
                channel_title = channel_response['items'][0]['snippet']['title']
                channel_subscribers = int(channel_response['items'][0]['statistics']['subscriberCount'])
                




                st.write("Video Title: ",video_title)
                st.write("Name Of Youtuber: ",channel_title)
                st.write("Total Subscribers: ",channel_subscribers)
                st.write("Total Likes: ",video_likes)



                extracting_message = st.empty()
                extracting_message.write("*Extracting comments...*")


                
                comments = get_comments(youtube, video_id, '')
                
                #st.write("Comments extracted successfully!")

                # Create a DataFrame to store the data
                data = []

                for comment_data in all_comments:
                    replies = comment_data.get('Replies', [])
                    replies_text = "\n".join([reply['Comment'] for reply in replies])
                    data.append({
                        'Comment': comment_data['Comment'],
                        'Likes': comment_data['Likes'],
                        'Date': comment_data['Date'],
                        'Replies': replies_text,
                        'NumReplies': comment_data['NumReplies']
                    })
                extracting_message.empty()

                df = pd.DataFrame(data)

                sentences = list(df["Replies"].unique())
                
                # Split each value in the list into sentences
                split_sentences = [sentence.split('\n') for sentence in sentences]

                # Flatten the list of split sentences
                flattened_sentences = [sentence for sublist in split_sentences for sentence in sublist]

                # Create a new DataFrame
                df_replies = pd.DataFrame(flattened_sentences, columns=["Replies"])

                # Remove empty rows
                df_replies = df_replies[df_replies["Replies"] != ""]

                # Reset the index of the DataFrame
                df_replies.reset_index(drop=True, inplace=True)

                A = df["Comment"]

                B = df_replies["Replies"]

                C =list(A) + list(B)

                final = pd.DataFrame({'All Comments': C})

                df['Date'] = pd.to_datetime(df['Date'])

                # Extract 'Date' and 'Time' components
                df['Formatted Date'] = df['Date'].dt.strftime('%d-%m-%Y')
                df['Formatted Time'] = df['Date'].dt.strftime('%H:%M:%S')

                df.drop(["Date","Replies"], axis = 1, inplace = True)


                final['sentiment_vader'] = final['All Comments'].apply(lambda x: sentiment_Vader(x))

                st.write("Total Comments (using API)",final.shape[0])

                non_neutral_sentiments = final[final['sentiment_vader'] != 'neutral']

                # Count the occurrences of positive and negative sentiments
                sentiment_counts = non_neutral_sentiments['sentiment_vader'].value_counts()
                # Get the sentiment with the highest count (positive or negative)
                most_common_sentiment = sentiment_counts.idxmax()

                if most_common_sentiment == "positive":
                    st.subheader("Result:")
                    st.write("The following Content is Flagged As: **Valid** ✅")
                else:
                    st.subheader("Result:")
                    st.write("The following Content is Flagged As: **Misleading** ❌")

                st.write("---------")
                st.write("Want to know more about the analysis on this website? Click On **Visualization** Tab to get started!🎓")

                value = "True"
            else:
                st.write("")

        except IndexError:
            st.write("*Input valid URL* ❌")
####################################################################################################################################

        #input= "yes"
        #if input == "yes":
        #if st.button("Visualize"):

    

        with tab2:

            if value == "True":
                
                st.subheader('Sentiment Distribution')
                
                choice_counts = final['sentiment_vader'].value_counts()
                # Create a bar graph using Plotly Express
                fig = px.bar(x=choice_counts.index, y=choice_counts.values, labels={'x': 'Sentiment', 'y': 'Count'})

                # Set the title and axis labels
                fig.update_layout( xaxis_title='Sentiment', yaxis_title='Count', width=700, height=400)

                # Show the interactive plot using st.plotly_chart
                st.plotly_chart(fig)

                st.write("___________________________")




                df['sentiment_vader'] = df['Comment'].apply(lambda x: sentiment_Vader(x))


                # Assuming you already have 'Formatted Date' and 'sentiment_vader' columns in the DataFrame
                df['date'] = pd.to_datetime(df['Formatted Date'], format='%d-%m-%Y')

                # Group by month and year and calculate sentiment counts
                grouped = df.groupby([df['date'].dt.year, df['date'].dt.month, df['sentiment_vader']]).size().unstack(fill_value=0)
                grouped.columns.name = None  # Remove column name for better readability

                # Display the processed DataFrame (optio
                # Plot a line chart
                st.subheader('Sentiment Distribution Over Time')
                fig, ax = plt.subplots(figsize=(20, 6))
                grouped.plot(kind='line', ax=ax, marker='o')
                ax.set_xticks(range(len(grouped)))
                ax.set_xticklabels([f"{pd.to_datetime(str(year) + '-' + str(month), format='%Y-%m').strftime('%b %Y')}" for year, month in grouped.index], rotation=45)
                ax.set_xlabel('Month-Year')
                ax.set_ylabel('Sentiment Count')
                plt.legend(title='Sentiment')
                plt.tight_layout()

                # Display the chart using Streamlit
                st.pyplot(fig)

                st.write("___________________________")




                # Assuming you already have 'Formatted Date' and 'Likes' columns in the DataFrame
                df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], format='%d-%m-%Y')

                # Group by month and year and sum up likes
                grouped_likes = df.groupby([df['Formatted Date'].dt.year, df['Formatted Date'].dt.month])['Likes'].sum()


                # Display the processed DataFrame (optional)

                # Plot a line chart
                st.subheader('Likes Over Time')
                fig, ax = plt.subplots(figsize=(20, 6))
                grouped_likes.plot(kind='line', marker='o', ax=ax)
                ax.set_xticks(range(len(grouped_likes)))
                ax.set_xticklabels([f"{pd.to_datetime(str(year) + '-' + str(month), format='%Y-%m').strftime('%b %Y')}" for year, month in grouped_likes.index], rotation=45)
                ax.set_xlabel('Month-Year')
                ax.set_ylabel('Total Likes')
                plt.grid(True)
                plt.tight_layout()

                st.pyplot(fig)


                st.write("___________________________")



                df['Formatted Time'] = pd.to_datetime(df['Formatted Time'], format='%H:%M:%S')

                # Extract the hour from the datetime and calculate comment counts for each hour
                hourly_comment_counts = df['Formatted Time'].dt.hour.value_counts().sort_index()

                # Plot the distribution of comments by hour using a line plot
                st.subheader('Distribution of Comments by Hour')
                plt.figure(figsize=(15, 6))
                plt.plot(hourly_comment_counts.index, hourly_comment_counts.values, marker='o')
                plt.xlabel('Hour')
                plt.ylabel('Number of Comments')
                plt.title('Distribution of Comments by Hour')
                plt.xticks(hourly_comment_counts.index)
                plt.grid(True)
                plt.tight_layout()
                st.pyplot(plt)

                st.write("___________________________")



                st.subheader("Most used words - WordCloud")
                final['Cleaned_Comments'] = final['All Comments'].apply(clean_text)

                all_comments1 = ' '.join(final['Cleaned_Comments'])

                wordcloud = WordCloud(width=800, height=800, background_color='white', max_words=150).generate(all_comments1)

                # Create a WordCloud object
                fig, ax = plt.subplots(figsize=(8, 8), facecolor=None)
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis("off")
                plt.tight_layout(pad=0)

                background_color = 'white'
                font_path = 'path_to_your_font_file.ttf'  # Specify the path to a custom font file
                max_words = 150
                wordcloud_shape = "rectangle"  # Change to a custom shape if desired

                wordcloud = WordCloud(
                    width=800,
                    height=800,
                    background_color=background_color,
                    max_words=max_words,
                ).generate(all_comments1)

                st.pyplot(fig)


                st.write("___________________________")



                top_3_comments = df.nlargest(5, 'Likes')

                # Streamlit app
                st.subheader('Top 5 Most Liked Comments')

                st.table(top_3_comments[['Comment', 'Likes']])

                st.write("___________________________")



                top_3_replies = df.nlargest(3, 'NumReplies')

                # Streamlit app
                st.subheader('Top 3 Comments with Most Replies')
                st.table(top_3_replies[['Comment', 'NumReplies']])

            else:
                st.write("Please Enter a link, before you can view here!")

        with tab3:

            st.write("*For Content related to Reddit*")
            reddit_url = st.text_input("Enter Link To Reddit Post:")

            if st.button("Detect Claim",key="a"):

                #reddit_url = "https://www.reddit.com/r/IndiaInvestments/comments/15y4st4/lets_talk_about_email_accounts_for_investments/"

                # Subreddit name and post ID extraction using regex
                pattern = r"https://www.reddit.com/r/(\w+)/comments/(\w+)/"
                matches = re.match(pattern, reddit_url)

                if matches:
                    subreddit_name = matches.group(1)
                    post_id = matches.group(2)

                    extracting_message = st.empty()
                    extracting_message.write("*Extracting comments...*")

                    # Set up your Reddit API credentials
                    reddit = praw.Reddit(
                        client_id='5hkM-ZVUKNRa0M-Y2erQEg',
                        client_secret='PFhtb8C6a3Tg8TXEaOKcbOWqIKi1Cg',
                        user_agent = "script:Untold (EngineeringOld459)"
                    )



                    # Retrieve the post and its comments
                    submission = reddit.submission(id=post_id)
                    submission.comments.replace_more(limit=None)  # Retrieve all comments

                    # Create an empty list to store comments
                    all_comments_list = []

                    # Function to recursively extract comments
                    def extract_comments(comment_list):
                        for comment in comment_list:
                            comment_text = comment.body
                            all_comments_list.append(comment_text)  # Append comment to the list
                            extract_comment(comment.replies)  # Recursively extract replies

                    def extract_comment(comment_list):
                        for comment in comment_list:
                            comment_text = comment.body
                            all_comments_list.append(comment_text)  # Append reply to the list

                    # Start extracting comments
                    extract_comments(submission.comments)

                    # Create a DataFrame from the comments list
                    comments_df = pd.DataFrame({"All_Comments": all_comments_list})

                    comments_df['sentiment_vader'] = comments_df['All_Comments'].apply(lambda x: sentiment_Vader(x))

                    non_neutral_sentiments = comments_df[comments_df['sentiment_vader'] != 'neutral']

                    # Count the occurrences of positive and negative sentiments
                    sentiment_counts = non_neutral_sentiments['sentiment_vader'].value_counts()
                    # Get the sentiment with the highest count (positive or negative)
                    most_common_sentiment = sentiment_counts.idxmax()

                    extracting_message.empty()

                    if most_common_sentiment == "positive":
                        st.subheader("Result:")
                        st.write("The following Content is Flagged As: **Valid** ✅")
                    else:
                        st.subheader("Result:")
                        st.write("The following Content is Flagged As: **Misleading** ❌")


                else:
                    st.write("**Invalid Reddit URL** ❌")

                

if __name__ == "__main__":
    main()
