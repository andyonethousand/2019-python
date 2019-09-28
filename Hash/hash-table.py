hash_table = [[] for l in range(10)]

def hash_function(key):
    index = len(key) % 10
    return index

def insert(key, value):
    index = hash_function(key)
    hash_table[index].append([key, value])

def search(key):
    index = hash_function(key)
    for i in range(len(hash_table[index])):
        if hash_table[index][i][0] == key:
            return hash_table[index][i][1]
    
def delete(key):
    index = hash_function(key)
    for i in range(len(hash_table[index])):
        if hash_table[index][i][0] == key:
            del hash_table[index][i]
            return 

insert('John', 35000)
print(search('John'))

insert('John', 12)
print(search('John'))