from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """ Opens file path and populates word list then closes file.

            Prints confirmation message of the amount of words in file
        """
        self.file_path = file_path
        self.words = []
        self.update_words_from_file()

        self.confirmation_msg(amount=len(self.words))

    def confirmation_msg(self, amount):
        """Prints out confirmation message

            Called on __init__
            Returns None
        """
        print(f"{amount} words read")

    def update_words_from_file(self):
        """ Open file and read each line and add to word list,
            closes files
            Called on __init__

            Returns None
        """
        file = open(self.file_path)

        self.words = file.read().splitlines()

        file.close()

    def get_random_word(self) -> str:
        """ Returns a random word from word list
            Called on __init__

            Returns string
        """
        return choice(self.words)




