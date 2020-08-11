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
class Graph:
    pass
'''
#Build our graph
## Could filter our word list by lenght
## remember to lower case stuff

filtered_word_list = filter()
for word1 in word_list:
    for word2 in word_list:
        if one_letter_off(word1, word2):
            Graph.add_edge
'''
# For every letter in the word,
## Swap out a letter in the alphabet
### if the result is in our words list, it's a neighbor
# len(word) * 26 -- o(n * 26) -- O(26n) -- O(n)
import string 
word_list = set()
for word in word_list:
    word_list.add(word.lower())
def get_neighbors(start_word):
    neighbors = []
    #for every letter in the word,
    for letter_index in range(len(start_word)):
        ## swap out a letter in the alphabet
        for letter in string.ascii_lowercase:
            word_list = list(start_word)
            word_list[letter_index] = letter

            word = "".join(word_list)
            if word in word_list and word != start_word:

                neighbors.append(word)
    return neighbors

def word_ladders(start_word, end_word):
    q = Queue()
    visited = set()
    q.enqueue([start_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path
        
        if current_word not in visited:
            visited.add(current_word)
            neighbors = get_neighbors(current_word)

            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                q.enqueue(new_path)

