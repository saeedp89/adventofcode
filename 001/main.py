
def load_file_to_list(path):
    fhan=open(path)
    values=[]
    for i in fhan:
        values.append(int(i.strip()))
    return values

def get_ascending_counter(li):
    counter=0
    for number in range(1,len(li)):
        if li[number] > li[number-1]:
            counter+=1
    return counter

def split_to_three_subsets(li):
    #values=[199,200,208,210,200,207,240,269,260,263]
    number_of_subsets=len(li)-2
    subsets=[]
    for i in range(number_of_subsets):
        subsets.append(li[i]+li[i+1]+li[i+2])

    return subsets

if __name__=="__main__":
    li=load_file_to_list('input.txt')
    li_subset=split_to_three_subsets(li)
    print(get_ascending_counter(li_subset))

