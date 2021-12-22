fhan = open("input.txt")

def load_file_to_list():
    values=[]
    for i in fhan:
        values.append(int(i.strip()))
    return values
def get_ascending_counter():
    counter=0
    values=load_file_to_list()
    for number in range(1,len(values)):
        if values[number] > values[number-1]:
            counter+=1
    return counter

class MeasureTage:
    def __init__(self):
        self.values=[]
        file_handle=open("input.txt")
        for item in file_handle:
            self.values.append(int(item.strip()))

    def get_number_of_increases(self):
        counter=0
        values=load_file_to_list()
        for number in range(1,len(values)):
            if values[number] > values[number-1]:
                counter+=1
        return counter        

