"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initializes the SerialGenerator with a starting value and a counter"""
        self.start = start
        self.count = 0
        
    def __repr__(self) -> str:
        return f'SerialGenerator start={self.start} next={self.start+1}'
        
    def generate(self):
        """
        Generates the next serial number by adding the current count to the starting value and returning it
        """
        serial_number = self.start + self.count
        self.count += 1
        return serial_number
        
    def reset(self):
        """
        Resets SerialGenerator to its initial starting value by setting the count back to zero. The next call of generate will return the inital starting value
        """
        self.count = 0
        
        
