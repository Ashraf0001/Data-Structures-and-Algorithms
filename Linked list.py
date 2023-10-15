class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insertatbegining(self, data):
        node = Node(data, self.head)
        self.head = node

    def printLinkedlist(self):

        if self.head is None:
            print("This is an empty linkedlist ")

        itr = self.head

        llstr = " "

        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr)


    def insertatend(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next is not None:
            itr = itr.next

        itr.next = Node(data, None)

    def insertvalues(self, data_list):
        self.head = None

        for data in data_list:
            self.insertatend(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    def removeatgivenindex(self, index):

        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr is not None:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1



if __name__=='__main__':

    ll= Linkedlist()
    ll.insertvalues([1, 2, 3])
    ll.printLinkedlist()
    print("Lenght of the linked list:", ll.get_length())
    ll.removeatgivenindex(2)
    ll.insertatend(5)

    ll.printLinkedlist()



    #adding new comment 

    #creating new branch

    #adding new comment in new branch

    #write a function for fibonnacchi series 
    def fibonnacchi(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return fibonnacchi(n-1)+fibonnacchi(n-2)
        
        #write another function for factorial number 

    def factorial(n):
        if n==0:
            return 1
        else:
            return n*factorial(n-1)
        
        #write a function for power of a number
    def power(n,p):
        if p==0:
            return 1
        else:
            return n*power(n,p-1)
        
        #write a function for sum of digits of a number
    def sumofdigits(n):
        if n==0:
            return 0
        else:
            return n%10+sumofdigits(n//10)
        
        #write a function for reverse of a number
        


    





