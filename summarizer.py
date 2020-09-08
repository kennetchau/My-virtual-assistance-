from newspaper import Article

def summarizer(link):
    article = Article(link)
    article.download()
    article.parse()
    article.nlp()

    print("Summary: {}".format(article.summary))

