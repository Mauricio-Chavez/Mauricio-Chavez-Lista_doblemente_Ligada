class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def append(self, value):
        if self.head is None:
            self.head=node(value)
            self.tail=self.head
            self.length=1
        else:
            new_nodo=node(value)
            self.tail.next=new_nodo
            new_nodo.prev=self.tail
            self.tail=new_nodo
            self.length +=1
    def print_list(self,s):
        if s==1:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
        else:
            temp = self.tail
            for i in range (1,self.length+1):
                print(temp.value)
                temp=temp.prev
    def pop(self):
        tem=self.tail.prev
        self.tail.prev=None
        tem.next=None
        self.tail=tem
        self.length-=1
    def popfirst(self):
        tem=self.head
        self.head=tem.next
        tem.next=None
        self.head.prev=None
        self.length-=1
    def prepend(self,value):
        new_nodo=node(value)
        self.head.prev=new_nodo
        new_nodo.next=self.head
        self.head=new_nodo
        self.length+=1
    def get(self,value):
        indice = value
        recorrer = self.head
        if indice <= self.length and indice > 0:
            for i in range(1, value):
                recorrer = recorrer.next
            print(recorrer.value)

        else:
            print("El indice indicado no existe")

    def set(self,i,value):
        tem=self.head
        if self.length == 0:
            new_nodo = node(value)
            self.head = new_nodo
            self.tail = new_nodo
            self.head.prev=None
        else:
            if i > 0 and i <= self.length:
                for j in range(1, i):
                    tem = tem.next

                tem.value = value

    def insert(self,i, value):
        tem = self.head
        new_nodo = node(value)
        if i > 0 and i <= (self.length + 1):
            if self.length == 0:
                self.append(value)
            else:
                if i == 1:
                    self.prepend(value)
                    return
                if i == (self.length + 1):
                    self.append(value)
                    return
                if i > 1 and i <= self.length:
                    for j in range(1, i - 1):
                        tem = tem.next

                    new_nodo.next=tem.next
                    new_nodo.prev=tem
                    tem.next=new_nodo
                    tem.next.next.prev=tem.next
                    self.length += 1
                    return
        else:
            print("El indice ingresado no es valido")
            return
    def remove(self,i):
        ant=self.head
        borrar=self.head
        pos=self.head
        if i > 0 and i <= self.length:
            if i==1:
                self.popfirst()
                return
            if i > 1 and i < self.length:
                for l in range(1,i):
                    borrar=borrar.next
                for j in range(1,i-1):
                    ant=ant.next
                for k in range(1,i+1):
                    pos=pos.next

                borrar.next=None
                borrar.prev=None
                ant.next=pos
                pos.prev=ant
                self.length-=1

                return
            if i==self.length:
                self.pop()
                return
        else:
            print("El indice de nodo ingresado no existe")
            return



my_doubly_linked_list=DoublyLinkedList()
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
"""print(f"Head: {my_doubly_linked_list.head.value}")
print(f"Tail: {my_doubly_linked_list.tail.value}")
print(f"Length: {my_doubly_linked_list.length}")"""
my_doubly_linked_list.print_list(1)
print("------------------------------------------")
my_doubly_linked_list.print_list(2)
print("------------------------------------------")
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list(1)
print("------------------------------------------")
my_doubly_linked_list.popfirst()
my_doubly_linked_list.print_list(1)
print("------------------------------------------")
my_doubly_linked_list.prepend(3)
my_doubly_linked_list.print_list(1)
print("------------------------------------------")
my_doubly_linked_list.get(2)
print("------------------------------------------")
my_doubly_linked_list.print_list(1)
print("------------------------------------------")
my_doubly_linked_list.set(1,6)
my_doubly_linked_list.print_list(1)
print("------------------------------------------")
my_doubly_linked_list.insert(2,7)
my_doubly_linked_list.print_list(1)
print("------------------------------------------")
my_doubly_linked_list.remove(3)
my_doubly_linked_list.print_list(1)


