#!/usr/bin/env python3
import sys
import json
import re
import string

stop_words = {
    "a", "about", "above", "after", "again", "against", "ain", "all", "am",
    "an", "and", "any", "are", "aren", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can", "could",
    "couldn", "d", "did", "didn", "do", "does", "doesn", "doing", "don", "down",
    "during", "each", "few", "for", "from", "further", "had", "hadn", "has",
    "hasn", "have", "haven", "having", "he", "her", "here", "hers", "herself",
    "him", "himself", "his", "how", "i", "if", "in", "into", "is", "isn", "it",
    "it's", "its", "itself", "just", "ll", "m", "ma", "me", "mightn", "more",
    "most", "mustn", "my", "myself", "needn", "no", "nor", "not", "now", "o",
    "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves",
    "out", "over", "own", "re", "s", "same", "shan", "she", "she's", "should",
    "shouldn", "so", "some", "such", "t", "than", "that", "that'll", "the",
    "their", "theirs", "them", "themselves", "then", "there", "these", "they",
    "this", "those", "through", "to", "too", "under", "until", "up", "very",
    "was", "wasn", "we", "were", "weren", "what", "when", "where", "which",
    "while", "who", "whom", "why", "will", "with", "won", "would", "wouldn",
    "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves", "get", "got", "gets", "gotten", "also", "just",
    "still", "ever", "yet", "maybe", "however", "well", "yes", "nope", "nah",
    "uh", "oh", "okay", "ok", "yeah", "hmm", "huh", "right", "sure", "alright",
    "actually", "basically", "literally", "seriously", "totally", "really",
    "thing", "things", "stuff", "something", "anything", "nothing", "everything",
    "everyone", "someone", "anyone", "nobody", "everybody", "kinda", "sorta",
    "lot", "lots", "bit", "guy", "guys", "girl", "girls", "man", "woman",
    "people", "person", "thing", "things", "way", "ways", "mean", "means",
    "say", "says", "said", "use", "used", "using", "like", "just", "maybe",
    "gonna", "wanna", "gotta", "lemme", "dunno", "cuz", "cause", "tho", "though",
    "even", "either", "neither", "yeah", "nah", "yep", "nope", "uh", "um", "hes", "im", 
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

for line in sys.stdin:
    try:
        data = json.loads(line)
        text = data.get('selftext', '') + " " + data.get('title', '')
        if not text or not isinstance(text, str):
            continue
        text = clean_text(text)
        for word in text.split():
            if word and word not in stop_words:
                # Skip pure numbers
                if word.isdigit():
                    continue
                print(f"{word}\t1")
    except json.JSONDecodeError:
        continue
