import streamlit as st
import preprocessor
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

c_name = ['South Africa','Australia','India','Canada','United States','New Zealand']
c_code=['za','au','in','ca','us','nz']
countries = {}
for i in range(len(c_name)):
  countries[c_name[i]] = c_code[i]

#Title, Author, Description, UrlToimg, Date_time, Content, Name = [],[],[],[],[],[],[]
if 'Title' not in st.session_state:
    st.session_state.Title = []
if 'Author' not in st.session_state:
    st.session_state.Author = []
if 'Description' not in st.session_state:
    st.session_state.Description = []
if 'Url_' not in st.session_state:
    st.session_state.Url_ = []
if 'Date_time' not in st.session_state:
    st.session_state.Date_time = []
if 'Content' not in st.session_state:
    st.session_state.Content = []
if 'Name' not in st.session_state:
    st.session_state.Name = []
if 'UrlToimg' not in st.session_state:
    st.session_state.UrlToimg = []


with st.sidebar:
    st.title("Welcome to the News API website!")
    st.header("Top headlines")
    country = st.selectbox("Select the country", sorted(c_name))
    headline = st.button("Top headlines")
    st.markdown("""---""")
    st.write("Search the news by Key words")
    response = st.sidebar.text_input("Enter the key word", " apple")
    search = st.button("Search news")
    st.markdown("""---""")
    st.write("select either top headlines or keyword and then analyze")
    analyze = st.button("Analyze")

code_c = preprocessor.countries[country]
if headline:
    st.sidebar.markdown("""---""")
    col1,col2 = st.columns(2)
    with col1:
        st.title("Top news from " + country)
    with col2:
        st.image(preprocessor.img_link[code_c])
    st.markdown("""---""")

    title, author, description, url_, urlToimg, date_time, content, name = preprocessor.content(preprocessor.countries[country])

    i = 0
    while i < 10:
        col1, col2 = st.columns(2)
        with col1:
            st.header(f"News from {name[i]}")
            st.session_state.Name.append(name[i])
            st.markdown('**Title:** ' + title[i])
            st.session_state.Title.append(title[i])
            st.markdown(f'**Author:** {author[i]}')
            st.session_state.Author.append(author[i])
            st.markdown('**Published on:** ' + date_time[i][:10])
            st.session_state.Date_time.append(date_time[i][:10])
            st.markdown(f'**Description:** {description[i]}')
            st.session_state.Description.append(description[i])
            if urlToimg[i] is not None:
                st.image(urlToimg[i])
                st.session_state.UrlToimg.append(urlToimg[i])
            else:
                st.write("No image available")
            expander = st.expander("Read More")
            expander.write(content[i])
            st.session_state.Content.append(content[i])
            expander = st.expander("Visit to News")
            expander.write(url_[i])
            st.session_state.Url_.append(url_[i])

        with col2:
            st.header(f"News from {name[i + 1]}")
            st.session_state.Name.append(name[i + 1])
            st.markdown('**Title:** ' + title[i + 1])
            st.session_state.Title.append(title[i + 1])
            st.markdown(f'**Author:** {author[i + 1]}')
            st.session_state.Author.append(author[i + 1])
            st.markdown('**Published on:** ' + date_time[i + 1][:10])
            st.session_state.Date_time.append(date_time[i + 1][:10])
            st.markdown(f'**Description:** {description[i + 1]}')
            st.session_state.Description.append(description[i + 1])
            if urlToimg[i + 1] is not None:
                st.image(urlToimg[i + 1])
                st.session_state.UrlToimg.append(urlToimg[i + 1])
            else:
                st.write("No image available")
            expander = st.expander("Read More")
            expander.write(content[i + 1])
            st.session_state.Content.append(content[i + 1])
            expander = st.expander("Visit to News")
            expander.write(url_[i + 1])
            st.session_state.Url_.append(url_[i + 1])

        i = i + 2

if search:
    st.header(f"News related to {response}")

    title, author, description, url_, urlToimg, date_time, content, name = preprocessor.search(response)

    i = 0
    while i < 10:
        col1, col2 = st.columns(2)
        with col1:
            st.header(f"News from {name[i]}")
            st.session_state.Name.append(name[i])
            st.markdown('**Title:** ' + title[i])
            st.session_state.Title.append(title[i])
            st.markdown(f'**Author:** {author[i]}')
            st.session_state.Author.append(author[i])
            st.markdown('**Published on:** ' + date_time[i][:10])
            st.session_state.Date_time.append(date_time[i][:10])
            st.markdown(f'**Description:** {description[i]}')
            st.session_state.Description.append(description[i])
            if urlToimg[i] is not None:
                st.image(urlToimg[i])
                st.session_state.UrlToimg.append(urlToimg[i])
            else:
                st.write("No image available")
            expander = st.expander("Read More")
            expander.write(content[i])
            st.session_state.Content.append(content[i])
            expander = st.expander("Visit to News")
            expander.write(url_[i])
            st.session_state.Url_.append(url_[i])

        with col2:
            st.header(f"News from {name[i + 1]}")
            st.session_state.Name.append(name[i+1])
            st.markdown('**Title:** ' + title[i + 1])
            st.session_state.Title.append(title[i+1])
            st.markdown(f'**Author:** {author[i + 1]}')
            st.session_state.Author.append(author[i+1])
            st.markdown('**Published on:** ' + date_time[i + 1][:10])
            st.session_state.Date_time.append(date_time[i + 1][:10])
            st.markdown(f'**Description:** {description[i + 1]}')
            if urlToimg[i + 1] is not None:
                st.image(urlToimg[i + 1])
                st.session_state.UrlToimg.append(urlToimg[i+1])
            else:
                st.write("No image available")
            expander = st.expander("Read More")
            expander.write(content[i + 1])
            st.session_state.Content.append(content[i+1])
            expander = st.expander("Visit to News")
            expander.write(url_[i + 1])
            st.session_state.Url_.append(url_[i + 1])

        i = i + 2



if analyze:
    number = 7
    c_text, sentence = preprocessor.get_data(st.session_state.Url_[number])
    #general Information
    st.header("General Information")
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.UrlToimg is not None:
            st.image(st.session_state.UrlToimg[number])
        else:
            st.write("No Image available")
    with col2:
        st.markdown(f"**News from** {st.session_state.Name[number]}")
        st.markdown('**Title:** ' + st.session_state.Title[number])
        st.markdown(f'**Author:** {st.session_state.Author[number]}')
        st.markdown('**Published on:** ' + st.session_state.Date_time[number][:10])

    st.markdown("""---""")

    st.header("Text Statistics")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("No of character",preprocessor.char_count(c_text))
    with col2:
        st.metric("No of letter",preprocessor.letter_count(c_text))
    with col3:
        st.metric("No of sentences",preprocessor.sentence_count(c_text))
    with col4:
        st.metric("No of Lexicons",preprocessor.lexicon_count(c_text))
    with col5:
        st.metric("No of Syllables",preprocessor.syllable_count(c_text))

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Ease of reading Score",preprocessor.ease_reading(c_text))
    with col5:
        st.metric("Grade Level",preprocessor.grade_level(c_text))
    with col3:
        st.metric("SMOG Index",preprocessor.smogindex(c_text))
    with col4:
        st.metric("Automated Readability Index",preprocessor.ari(c_text))
    with col2:
        st.metric("Reading Time (sec)",preprocessor.reading_time(c_text))

    st.markdown("""---""")

    st.header("Classification")
    result = preprocessor.classification(c_text)
    class_ = result.classification
    p_pos = result.p_pos
    st.write(f"Given News is {class_} with probability of {p_pos}")

    st.markdown("""---""")

    #sentiment
    st.header("Polarity and Subjectivity")
    df_textblob = preprocessor.sentiment(sentence)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Polarity",df_textblob["Polarity"].mean())
        fig = sns.displot(df_textblob["Polarity"], height=5, aspect=1.8)
        plt.xlabel("Sentence Polarity (Textblob)")
        plt.title("Polarity of Sentence")
        st.pyplot(fig)

    with col2:
        st.metric("Average Subjectivity", df_textblob["Subjectivity"].mean())
        fig = sns.displot(df_textblob["Subjectivity"], height=5, aspect=1.8)
        plt.xlabel("Sentence Subjectivity (Textblob)")
        plt.title("Subjectivity of Sentence")
        st.pyplot(fig)

    st.write("Polarity score can be positive or negative, and Subjectivity varies between 0 and 1.")

    st.markdown("""---""")
    #Word frequency and wordcloud
    st.header("Word frequency")
    frequency = preprocessor.word_frequency(c_text)
    topwords= frequency.most_common(20)
    x, y = [], []
    for i in range(len(topwords)):
        x.append(topwords[i][0])
        y.append(topwords[i][1])
    fig = plt.figure(figsize = (10, 5))
    plt.plot(x,y)
    plt.title("Word frequeecy (for 20 most frequent words)")
    plt.xticks(rotation=90)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    st.pyplot(fig)

    st.markdown("""---""")
    st.header("Word cloud")
    words_new=preprocessor.word_cloud(c_text)
    res = ' '.join([i for i in words_new if not i.isdigit()])
    fig = plt.figure(figsize=(16, 10))
    wordcloud = WordCloud(background_color='black',max_words=100,width=1400,height=1200).generate(res)
    plt.imshow(wordcloud)
    plt.title('NEWS ARTICLE (100 words)')
    plt.axis('off')
    st.pyplot(fig)


st.write("App created by Ronak Pandya")




