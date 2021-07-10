#A Genric tree which have more than two children


class Gtree:
    def __init__(self,data):
        self.data=data
        self.children=list()


def insert():
    print("Enter the data")
    node=int(input())
    if node==-1:
        return None
    root=Gtree(node)
    print(f"how many children do you want of {root.data}")
    children=int(input())
    #here if children input would be zero then it will not run the for loop
    for i in range(children):
        child=insert()
        root.children.append(child)
    return root

def printGtree(root):
    #below in line 25 is edge case not a base case
    if root==None:
        return
    print(root.data)
    #if child will be zero then it will not run the loop
    for child in root.children:
        printGtree(child)

    return
def printGtreeD(root):
    if root==None:
        return
    print(f'{root.data}:',end='')
    for child in root.children:
        print(f"{child.data} ",end='')
    print()
    for child in root.children:
        printGtreeD(child)

    return

if __name__=="__main__":
 a=insert()
 printGtreeD(a)
