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
    #new_text = re.sub(r"\.|,|;|:|-|!|\?|´|`|^|'", "", text)
    new_text = re.sub(r"\s|\n", '', text)
    #new_text = re.sub(r"[0-9]+", "", new_text)
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


def main(text: str):
    text = text.lower()
    content = {
        'parameters': {
            'letters': int(letterCounter(text)),
            'characteres': int(charCounter(text)),
            'words': int(wordCounter(text)),
            'sentences': int(setenceCount(text)),
            'syllables': int(syllableCounter(text)),
            'complex_words': int(complex_wordCounter(text))
        },
        'indexes': {
            'flesch_pt': float(flesh_pt(text)),
            'gulpease': float(gulpease(text)),
            'flesch_kincaid': float(flesh_kincaid_pt(text)),
            'gunning_pt': float(gunning_pt(text)),
            'automated_readability': float(automated_readability_pt(text)),
            'coleman_liau': float(coleman_liau_index_pt(text))
        }
    }

    return content


"""
if __name__ == '__main__':
    #main()
    #string_test = '''É importante observar que ao realizar a raspagem de dados é fundamental respeitar os termos de serviço do site alvo e os direitos autorais.'''
    #string_test_en = 'It is important to note that when performing data scraping, it is essential to respect the target site\'s terms of service and copyright'

    string_test = '''Bahia/Cultura
O estado apresenta uma grande riqueza em termos culturais. No campo da música, forneceu grandes nomes para a música brasileira, especialmente a partir de meados do século XX, como Dorival Caymmi, João Gilberto, Tom Zé, Caetano Veloso, Raul Seixas, Pepeu Gomes, Armandinho, Dodô e Osmar, Gilberto Gil, Gal Costa, Maria Bethânia, Moraes Moreira, Daniela Mercury, Carlinhos Brown, Ivete Sangalo, Chiclete com Banana, Asa de Águia, Cheiro de Amor, Banda Eva, entre outros. Famosos estilos musicais surgiram no estado, como o samba de roda e a "axé music" dos anos 1990. 
Os trios elétricos foram criados no carnaval de Salvador de 1951 e, de lá, se espalharam pelo país. Grande parte dessa riqueza musical se expressa no carnaval, que ainda exibe tradicionais blocos de rua, como o Olodum, o Ilê Aiyê e o Filhos de Gandhy. No campo religioso, as religiões predominantes no estado são o catolicismo e o candomblé, muitas vezes praticados de forma conjunta. No campo esportivo, a manifestação mais característica do estado é a capoeira, misto de música, luta e jogo, de origem africana, que é praticado por grande parte da população. As cidades do estado possuem muitas construções da época colonial em estilo barroco, de quando Salvador constituía a capital da colônia do Brasil.
O estado também sempre foi pródigo em grandes escritores: Gregório de Matos, Castro Alves, Jorge Amado e João Ubaldo Ribeiro nasceram no estado. A culinária do estado tem acentuada influência africana, expressa em pratos típicos do candomblé, como o acarajé, o bobó de camarão, o vatapá, o abará, o xinxim de galinha etc. No interior do estado, a maior influência culinária é a da típica cozinha sertaneja, com carne de sol, carne de bode, manteiga de garrafa, jabá (carne-seca), jerimum (abóbora), umbu, maxixe, mandioca, milho etc. . Os times de futebol com maiores torcidas no estado são o Esporte Clube Bahia e o Esporte Clube Vitória, ambos sediados na capital estadual, Salvador. Os confrontos entre os dois clubes são apelidados de "Ba-Vi". Além do carnaval, outras datas são muito comemoradas no estado:'''

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
    ''')"""