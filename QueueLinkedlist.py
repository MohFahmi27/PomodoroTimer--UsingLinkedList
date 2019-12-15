from Node import *

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def en_queue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def de__queue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if (self.front == None):
            self.rear = None
        return str(temp.data)

    def deleteNode(self, key):
        temp = self.front
        if (temp is not None):
            if (temp.data == key):
                self.front = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

    def length(self):
        myfront = self.front
        if self.isEmpty():
            i = 0
            return int(i)
        else :
            i = 0
            while (myfront != None):
                i += 1
                myfront = myfront.next
            return i

    def tampil(self):
        myfront = self.front
        if self.isEmpty():
            print("Kegiatan Kosong")
        else:
            i = 0
            while (myfront != None):
                i += 1
                print(i,". ",myfront.data)
                myfront = myfront.next
            return