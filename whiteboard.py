# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “), return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.
# Example Input: “Hello World”
# Example Output: 5
# Example Input: “We’re learning about a great full-stack web application called Flask”
# Example Output: 5


def lenWord(str):
    list = str.split()
    print(len(list[-1]))

lenWord('“We’re learning about a great full-stack web application called Flask')