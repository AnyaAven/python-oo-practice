from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """ Opens file path and populates word list then closes file.

        Prints confirmation message of the amount of words in file
        """
        self.file_path = file_path  # NOTE: do we need to store this?

        self.words = self.get_words_from_file()

        self.print_word_count()

    def __repr__(self):
        return f"<WordFinder \nfile_path='{self.file_path}' \nwords={self.words}>"

    def print_word_count(self):
        """Prints out confirmation message

        Called on __init__
        Returns None
        """
        print(f"{len(self.words)} words read")

    def get_words_from_file(self):
        """ Open file and read each line and add to word list,
        closes files
        Called on __init__

        Returns None
        """
        file = open(self.file_path)

        words = file.read().splitlines()
        file.close()

        return words

    def get_random_word(self) -> str:
        """ Returns a random word from word list
        Called on __init__

        Returns string
        """
        return choice(self.words)


# FIXME: change update_words_from_file instead of get_random
class SpecialWordFinder(WordFinder):
    """Finds a random word from file, 
    excluding blank lines and comments (#)
    """

    def get_words_from_file(self):
        words = super().get_words_from_file()
        filteredWords = [
            word for word in words if not (word == "" or word.startswith('#'))]
        return filteredWords

    # def get_random_word_exclusive(self):
    #     """gets random word from words,
    #     filtering blank lines and lines starting with #
    #     """
    #     getRand = choice(self.words)
    #     while (getRand == "" or getRand.startswith('#')):
    #         getRand = choice(self.words)

    #     return getRand
