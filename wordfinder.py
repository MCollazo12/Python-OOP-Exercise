import random

class WordFinder:
    """
    A class that reads words from a passed in dictionary file and provides a random word using the random() method
    
    Args:
        file_path (str): The path to the dictionary file to be used for word retrieval
        
    Attributes:
        data (list): A list of words read from the dictionary file
    """
    
    def __init__(self, file_path):
        """
        Initializes a WordFinder instance by opening and reading the specified
        dictionary file. The number of words read from the file is displayed.
        """
        dict_file = open(file_path)
        self.data = self.read_file(dict_file)
        print(f"{'{:,}'.format(len(self.data))} words read")
        
    def read_file(self, dict_file):
        """ 
        Reads the passed in dict_file and returns a list of words with spaces removed 
        """      
        return [line.strip() for line in dict_file if line.strip() ]
        
    def random(self):
        """
        Returns a random word from the list of words using random.choice()
        """
        return random.choice(self.data)
        
class SpecialWordFinder(WordFinder):
    """
    A specialized WordFinder class that inherits its functionality from WordFinder.
    Will read words from a file and return a list without spaces or # comments
    """
    
    def read_file(self, dict_file):
        """
        Reads words from a given file and returns a list with spaces and # comments removed 
        """
        return [line.strip() for line in dict_file if line.strip() and not line.startswith('#')]
    
        
        

    