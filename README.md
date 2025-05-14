# WhatsApp Chat Analyzer

A powerful and interactive Streamlit-based web application to analyze WhatsApp chat histories. Upload your WhatsApp exported `.txt` chat file and explore insightful visualizations and statistics.

## 📌 **Features**

* Total messages, words, media, and links statistics
* Monthly and weekly activity analysis
* Visual representation of the most active days and months
* Heatmap of daily and hourly chat activity
* Top senders analysis and contribution percentages
* Wordcloud visualization for the most common words
* Emoji analysis with frequency breakdown

## 🚀 **How to Run Locally**

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/whatsapp_chat_analyzer.git
   cd whatsapp_chat_analyzer
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

4. Open [http://localhost:8501](http://localhost:8501) in your browser.

## 🌐 **Deploying on Streamlit Cloud**

1. Push your project to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Click **New App** → Select your GitHub repo.
4. Choose the branch and `app.py` as the main file.
5. Deploy and share your app link!

## 📂 **File Structure**

```
whatsapp_chat_analyzer/
│
├── app.py                # Main Streamlit app
├── helper.py             # Helper functions for analysis
├── preprocess.py         # Preprocessing logic
├── requirements.txt      # Dependencies list
└── README.md             # Project description (this file)
```

## 📜 **Requirements**

* Python 3.8+
* Streamlit
* Pandas
* Matplotlib
* Seaborn
* WordCloud
* Emoji

## 🤝 **Contributing**

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## 📞 **Contact**

For any issues or feature requests, open an issue or contact me at [your-email@example.com](mailto:your-email@example.com).

---

**Happy Analyzing! 🎉**
