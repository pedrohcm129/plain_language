import re
import pyphen
import syllables
from nltk.tokenize import word_tokenize

def letterCounter(text):
    new_text = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚçÇãõâêà]', '', text) 
    count = len(new_text)
    return count

# Refatorar de acordo com o a descrição da contagem do artigo
def charCounter(text):
    new_text = re.sub(r"\.|,|;|:|-|!|\?|´|`|^|'", "", text)
    new_text = re.sub(r"[0-9]+", "", new_text)
    count = len(new_text)
    return count

def wordCounter(text):
    list_words = re.split(r'\s+', text)
    count = len(list_words)
    return count


def setenceCount(text):
    list_sentences = re.split(r'[\.\!\?\;]', text)
    count = 0
    for sentence in list_sentences:
        if sentence != '':
            count += 1 
    return count

def syllableCounter(text):
    vogal = ['a', 'ã', 'â', 'á', 'à', 'e', 'é', 'ê', 'i', 'í', 'o', 'ô', 'õ', 'ó', 'u', 'ú']
    ditongo = ['ãe', 'ai', 'ão', 'au', 'ei', 'eu', 'éu', 'ia', 'ie', 'io', 'iu', 'õe', 'oi', 'ói', 'ou', 'ua', 'ue', 'uê', 'ui']
    tritongo = ['uai', 'uei', 'uão', 'uõe', 'uiu', 'uou']

    count = 0

    for i in range(0, len(text)):
        if text[i] in vogal:
            count += 1
            
        if i >= 1 and (text[i-1]+ text[i]) in ditongo:
            count -= 1
        elif i >= 2 and (text[i-2] + text[i-1] + text[i]) == tritongo:
            count -= 1
    return count

# def syllableCounter(text):
#     language = 'portuguese'
#     new_text = text.lower()
#     tokens = word_tokenize(new_text)
#     count_syb = 0
#     dic = pyphen.Pyphen(lang = 'pt_BR')
#     for w in tokens:
#         try:
#             count_syb+= len(dic.inserted(w).split("-"))
#         except:
#             count_syb+= syllables.estimate(w)
#     return count_syb

def complex_wordCounter(text):
    words_tokened = word_tokenize(text)
    count = 0
    for word in words_tokened:
        if syllableCounter(word) > 2:
            count += 1
    return count

def flesh_pt(text):
    legibility = 227 - (1.04 * wordCounter(text) / setenceCount(text)) - (72 * syllableCounter(text) / wordCounter(text))
    return legibility

def gunning_pt(text):
    legibility = (0.49 * wordCounter(text) / setenceCount(text)) + (19 * complex_wordCounter(text) / wordCounter(text))
    return legibility

def automated_readability_pt(text):
    legibility = (0.44 * wordCounter(text) / setenceCount(text)) + (4.6 * charCounter(text) / wordCounter(text)) - 20
    return legibility

def flesh_kincaid_pt(text):
    legibility = (0.36 * wordCounter(text) / setenceCount(text)) + (10.4 * syllableCounter(text) / wordCounter(text)) - 18
    return legibility

def coleman_liau_index_pt(text):
    legibility = (5.4 * charCounter(text) / wordCounter(text)) - (21 * setenceCount(text) / wordCounter(text)) - 14
    return legibility

def gulpease(text):
    legibility = 89 + (300 * setenceCount(text) / wordCounter(text)) - (10 * letterCounter(text) / wordCounter(text))
    return legibility

if __name__ == '__main__':
    string_test = '''É importante observar que ao realizar a raspagem de dados é fundamental respeitar os termos de serviço do site alvo e os direitos autorais.'''
    string_test_en = 'It is important to note that when performing data scraping, it is essential to respect the target site\'s terms of service and copyright'

    string_test = '''A prática de mineração de dados.'''

    string_test = string_test.lower()

    print(f'''
        Letras: {letterCounter(string_test)}
        Characteres: {charCounter(string_test)}
        Palavras: {wordCounter(string_test)}
        Sentenças: {setenceCount(string_test)}
        Sílabas: {syllableCounter(string_test)}
        Palavras complexas: {complex_wordCounter(string_test)}
        
        Flesh PT: {flesh_pt(string_test)}
        Gulpease: {gulpease(string_test)}
        Flesch-Kincaid: {flesh_kincaid_pt(string_test)}
        Gunning PT: {gunning_pt(string_test)}
        Legibilidade Automatizado: {automated_readability_pt(string_test)}
        Coleman-Liau: {coleman_liau_index_pt(string_test)}
    ''')