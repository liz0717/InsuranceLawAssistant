import re


REMOVE_PATTERNS = [

    r"金融監督管理委員會主管法規共用系統",

    r"列印時間.*",

    r"https://.*",

    r"資料來源.*",

    r"\d+/\d+$",

    r"\d+/\d+"

]


def clean_text(text):

    cleaned = text

    for pattern in REMOVE_PATTERNS:

        cleaned = re.sub(pattern, "", cleaned)

    return cleaned
