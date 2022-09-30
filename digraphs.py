import itertools, string

# We assume any two-consonant combo is a digraph.
consonants = set(string.ascii_lowercase) - set("aeiou")
digraphs = set(''.join(t) for t in itertools.product(consonants, consonants))

counts = {}
# Linux, unfortunately, doesn't come with an Australian dictionary, and sadly,
# Macquarie subscribers don't get access to the word list. But it seems Wordle
# uses a US dictionary anyhow, and devs are free to use whatever dictionary they
# want.
dict_path = '/usr/share/dict/british-english'
for word in open(dict_path):
    word = word.strip()
    # Remove the following condition, to count all words.
    if len(word) != 5:
        continue
    for digraph in digraphs:
        if digraph in word:
            counts[digraph] = counts.get(digraph, 0) + 1

for digraph in sorted(counts, key=counts.get):
    print(digraph, counts[digraph])
