def load_file_to_list(path):
    fhan=open(path)
    values=[]
    for i in fhan:
        values.append(i.strip())
    return values

def calculate(li):
    vec={"forward":0,"up":0,"down":0}
    for item in li:
        splitted=str(item).split()
        vec[splitted[0]]+=int(splitted[1])
    depth=vec['down']-vec['up']
    x=vec['forward']
    return (x*depth)


if __name__=="__main__":
    li=load_file_to_list('input.txt')
    
    print(calculate(li))