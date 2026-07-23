import re

from modules.law_model import LawArticle


def split_articles(text):

    pattern = r"\n([一二三四五六七八九十]+)、"

    matches = list(re.finditer(pattern, text))

    articles = []

    for i, match in enumerate(matches):

        start = match.start()

        if i == len(matches)-1:
            end = len(text)
        else:
            end = matches[i+1].start()

        article_text = text[start:end].strip()

        no = match.group(1)

        articles.append(
            LawArticle(
                no=no,
                title=f"第{no}點",
                content=article_text
            )
        )

    return articles
