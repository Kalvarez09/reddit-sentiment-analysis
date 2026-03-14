import json

input_path = '/home/kali/Desktop/reddit_posts2.json'
output_path = '/tmp/posts_text_only.txt'

with open(input_path, 'r', encoding='utf-8') as f_in:
    data = json.load(f_in)  #Loads JSON

with open(output_path, 'w', encoding='utf-8') as f_out:
    for entry in data:
        title = entry.get('title', '')
        selftext = entry.get('selftext', '')
        text = (title + ' ' + selftext).strip()
        if text:
            # change spaces for plain text
            f_out.write(text.replace('\n', ' ') + '\n')
