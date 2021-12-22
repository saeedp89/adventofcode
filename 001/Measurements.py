class MeasureTage:
    def __init__(self):
        self.values = []
        file_handle = open("input.txt")
        for item in file_handle:
            self.values.append(int(item.strip()))

    def get_number_of_increases(self):
        counter = 0
        for number in range(1,len(self.values)):
            if self.values[number] > self.values[number - 1]:
                counter += 1
        return counter        
