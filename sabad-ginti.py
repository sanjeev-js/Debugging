def word_count(str):
    counts = dict()
    word = str.split()

    for word in word:
        if word in counts:
            counts[word] =+ 1
        else:
            counts[word] =+ 1
    return counts

print(word_count('the quick brown fox jumps over the lazy dog.'))





def word_count(str):
    counts = dict()
    word = str.split('')

    for word in word:
        if word in counts:
            counts[word] =+ 1
        else:
            counts[word] =+ 1
    return counts
print(word_counts("the quick brown fox jumps over the lazy dog.))