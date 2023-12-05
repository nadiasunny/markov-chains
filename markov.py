"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """    
    f = open(file_path)
    return f.read()



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    text_string = text_string.split()
    chains = {}
    bigram_tuples = []

    for i in range(len(text_string)-2):
        #Add bigrams to chains as keys
        word1 = text_string[i]
        word2 = text_string[i+1]
        word3 = text_string[i+2]
        
        key = (word1, word2)
        if key in chains:
            chains[key].append(word3) 
        else: 
            chains[key] = [word3]
        #chains[key] = (word1, word2, word3)
    # your code goes here
    print(bigram_tuples)
    return chains
text = open_and_read_file('green-eggs.txt')
print(make_chains(text))

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
