import re, math
from collections import Counter
from data_loader import data

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def compare_similarity(word_one, word_two):
    vector1 = text_to_vector(word_one.lower())
    vector2 = text_to_vector(word_two.lower())

    return get_cosine(vector1, vector2)

def find_most_similar(word):
    max = {"reply": None, "score": 0, "query": None}
    count=1
    for each in data:
        score = compare_similarity(word, data[str(count)]['query'])
        if score > max['score']:
            max['score'] = score
            max['reply'] = data[str(count)]['reply']
            max['query'] = data[str(count)]['query']
        count+=1
    return {"score": max['score'], "reply": max['reply'], "query": max['query']}
