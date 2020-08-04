import math

def Linear_search(text,data):
    for info in data:
        if text == info:
            print(info)
    else:
        print("not found")

def euclidean_similarity(x,y):
    x,y = x.lower(),y.lower()
    a = set(x.split())
    b = set(y.split())
    c = float(len(a&b))
    d = float(len(a|b))
    try:similarity_ratio = round(((c/d)*100/1),2)
    except:similarity_ratio = 0
    return(similarity_ratio)

def levenshtein_distance(word1,word2):
    """ levenshetein distance algorithm in python """
    word2 = word2.lower()
    word1 = word1.lower()
    matrix = [[0 for x in range(len(word2) + 1)] for x in range(len(word1) + 1)]
    #print(matrix)
    #print("Length of matrix :",len(matrix))
    #print("Length of index 0 :",len(matrix[0]))
    for x in range(len(word1) + 1):
        matrix[x][0] = x   
    for y in range(len(word2) + 1):
        matrix[0][y] = y
    for x in range(1, len(word1) + 1):
        for y in range(1, len(word2) + 1):
            if word1[x - 1] == word2[y - 1]:
                matrix[x][y] = min(matrix[x - 1][y] + 1,matrix[x - 1][y - 1],matrix[x][y - 1] + 1)
            else:
                matrix[x][y] = min(matrix[x - 1][y] + 1,matrix[x - 1][y - 1] + 1,matrix[x][y - 1] + 1)        
    levenshtein_distance = (matrix[len(word1)][len(word2)])    
    return (levenshtein_distance)   

""" cosine similarity index """
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def cosine_similarity(v, w):
    try:return(dot(v, w) / math.sqrt(dot(v, v) * dot(w, w)))
    except:dot(v, w) /0.1

common_words = None
def string_vector(string_list):
        "given a list of string_list, produce a vector whose i-th element is 1 if common_words[i] is in the list, 0 otherwise "
        return [1 if interest in string_list else 0 for interest in common_words]
           
def cosine_similarity_index(text1,text2):
    global common_words
    space = []    
    space.append(text1.lower().split())
    space.append(text2.lower().split())
    common_words = sorted(list({ common_word for common_words in space for common_word in common_words }))
    string_matrix = map(string_vector,space)
    string_similarities = [[cosine_similarity(common_word_i, common_word_j)for common_word_j in string_matrix]for common_word_i in string_matrix]
    try:cosine_similarity_index = round(sum(string_similarities[0])*100,1)
    except:cosine_similarity_index = 0
    return(cosine_similarity_index)


a = "hello world I am a programmer"
b = "hello world I am not a programmer"
c = "how are you doing today"


print("levenshtein_distance :",levenshtein_distance(a,b))
print("cosine_similarity_index :",cosine_similarity_index(a,b))
print("euclidean_similarity :",euclidean_similarity(a,b))