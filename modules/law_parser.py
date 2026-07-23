import re


def split_articles(text):

    pattern = r"\n([一二三四五六七八九十十一十二十三十四十五]+)、"

    matches = list(re.finditer(pattern, text))

    articles = []

    for i, match in enumerate(matches):

        start = match.start()

        if i == len(matches)-1:
            end = len(text)
        else:
            end = matches[i+1].start()

        article = text[start:end].strip()

        articles.append(article)

    return articles
