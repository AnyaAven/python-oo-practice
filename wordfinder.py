from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """ Opens file path and populates word list then closes file.

        Prints confirmation message of the amount of words in file
        """
        self.file_path = file_path

        self.words = self.get_words_from_file()

        self.print_word_count()

    def __repr__(self):
        return f"<WordFinder \nfile_path='{self.file_path}' \nwords={self.words}>"

    def print_word_count(self):
        """Prints out confirmation message

        Returns None
        """
        print(f"{len(self.words)} words read")

    def get_words_from_file(self):
        """ Open file and read each line and add to word list,
        closes files

        Returns list of words
        """
        file = open(self.file_path)

        words = file.read().splitlines()
        file.close()

        return words

    def get_random_word(self) -> str:
        """ Returns a random word from word list

        Returns string
        """
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """Finds a random word from file,
    excluding blank lines and comments (#)
    """

    def get_words_from_file(self):
        """gets random word from words,
        filtering blank lines and lines starting with #

        Returns list of words
        """

        words = super().get_words_from_file()
        filteredWords = [
            word for word in words if not (word == "" or word.startswith('#'))]
        return filteredWords
