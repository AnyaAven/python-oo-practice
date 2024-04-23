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

    # NOTE: specifies 'start' type to 'int'. Won't throw error, editor might catch
    def __init__(self, start: int):
        """sets starting number"""
        self.start = start
        self.add = 0

    def __repr__(self):
        return f"SerialGenerator self={self.start} current number={self.start + self.add}"

    @property  # NOTE: makes method behave like property (serial.generate)
    def generate(self):
        """gets next serial number in sequence and returns it"""
        new_num = self.start + self.add
        self.add += 1
        return new_num

    def reset(self):
        """reset add counter to starting value"""
        self.add = 0
