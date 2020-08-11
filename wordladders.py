import string
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

#Read words in from the file, add to set of words
word_set = set()
for w in word_set:
    l = 0
with open("words.text") as f:
    for word in f: #for each line of the file
        word_set.add(word.strip().lower())
print(word_set)
words_by_length = {}
def get_neighbors(word):
    neighbors = []
    word_letters = list(word)
    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase): #this will bring the alphabeth lower case
            #Make a copy of the word
            temp_word = list(word_letters)
            #substitute the letter into the word copy
            temp_word[i] = letter
            #Make it a string
            temp_word_str = "".join(temp_word)
            #if it's a real word, add it to the return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)
    return neighbors

def get_neighbors_2(word):
    def word_diff_by_1(w1, w2):
        if len(w1) != len(w2):
            return False
        diff_count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff_count += 1
        return diff_count == 1
    neighbors = []
    #look for words of the same length
    #If they differ by one letter, add to return set
    for word2 in words_by_length(len(word)):
        if word_diff_by_1(word, word2):
            neighbors.append(word2)

    return neighbors

def find_word_ladder(begin_word, end_word): #BFS
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    #visit all words
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
