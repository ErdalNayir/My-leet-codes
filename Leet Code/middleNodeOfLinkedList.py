class ListNode:
    def __init__(self, val="", next=None):
        self.val = val
        self.next = next
        self.count=1


def addNode(head,val):
    newNode=ListNode(val)

    if head.next==None: # if there is only head node

        head.next=newNode
        head.count=head.count+1
        print("Node has been added\n\n")

    else:  # insert new node at the begining of linked list
        newNode.next=head.next
        head.next=newNode
        head.count=head.count+1
        print("Node has been added\n\n")


def traverseList(head):
    temp=head

    while(temp!=None):
        print(temp.val)
        temp=temp.next
    print("\n\n")

def middleListNode(head):
    temp=head # I dont want to make new changes to head so I created temp
    lengthOfLinkedList=0

    while temp!=None: # We find Lenght of linked List
        lengthOfLinkedList+=1
        temp=temp.next

    middleIndex=lengthOfLinkedList//2 #Find middle of LinkedList

    while middleIndex>0:
        head=head.next
        middleIndex-=1
    
    return head


head=ListNode(1) # linked list created


while True:
    print("1. Add node")
    print("2.Traverse Linked List")
    print("3.Print count of linked list")
    print("4.MiddleListNode")
    print("0.Exit\n")

    opt=int(input("Please choose an option: "))

    if opt==1:
        value=int(input("Please enter the value of new node: "))
        addNode(head,value)
    elif opt==2:
        traverseList(head)
    elif opt==3:
        print("Number of node in list: {}\n\n".format(head.count))
    elif opt==4:
        result=middleListNode(head)
    elif opt==0:
        print("Byeeee")
        break
