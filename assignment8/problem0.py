# Define a class and a static method that receives a string (word) and reverses it and returns
# it.

class ReverseString:
    @staticmethod
    def reversedWord(word):
        if len(word) <= 1:
            return word
        return word[-1] + reversedWord(word[0:len(word)-1])

print(ReverseString.reversedWord("Hello"))