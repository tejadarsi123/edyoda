class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.top = None
        self.end = None

    def add(self, node):
        node = Node(node)
        if self.top == None:
            self.top = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def reversebygroup(self, group):
        self.top = self.reverse(group, self.top)
        return self.display()

    def reverse(self, k, head):
        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        while (current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse(k, next)

        return prev

    def display(self):
        if (self.top == None):
            print('List is empty')
            return
        temp_variable = self.top
        print(temp_variable.data, end='->')
        while temp_variable.next != None:
            temp_variable = temp_variable.next
            print(temp_variable.data, end='->')
        print()

    def mergealternatively(self, linkedlist):
        self.merge(self.top, linkedlist)
        return self.display()

        if self.top == None or linkedlist.top == None:
            self.top = linkedlist.top
            return

        temp_variable = self.top
        temp2 = linkedlist.top
        while temp_variable != None:
            mainnext = temp_variable.next
            temp_variable.next = temp2
            linkedlist.next = mainnext
            temp_variable = linkedlist.next

    def merge(self, list1, list2):
        list1_current = list1
        list2_current = list2.top

        while list1_current != None and list2_current != None:
            p_next = list1_current.next
            q_next = list2_current.next
            list2_current.next = p_next
            list1_current.next = list2_current
            list1_current = p_next
            list2_current = q_next
            list2.head = list2_current

    def removesumzero(self):
        if self.top == None:
            return "stack is empty"
        else:
            prev = self.top
            current = self.top
            while current != None:
                sum = current.data
                next = current.next
                while next != None:
                    sum += next.data
                    next = next.next
                    if sum == 0:
                        if current == self.top:
                            self.top = next
                        else:
                            prev.next = next
                prev = current
                current = current.next

        return self.display()


# 1. Delete the elements in an linked list whose sum is equal to zero

linkedlist = LinkedList()
linkedlist.add(5)
linkedlist.add(-2)
linkedlist.add(3)
linkedlist.add(-2)
linkedlist.add(-1)
linkedlist.add(6)
linkedlist.removesumzero()

# 2. Reverse a linked list in groups of given size
linkedlist = LinkedList()
linkedlist.add(7)
linkedlist.add(8)
linkedlist.add(2)
linkedlist.add(1)
linkedlist.add(5)
linkedlist.add(6)
linkedlist.reversebygroup(3)

# 3. Merge a linked list into another linked list at alternate positions.
linkedlist = LinkedList()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
linkedlist2 = LinkedList()
linkedlist2.add(4)
linkedlist2.add(5)
linkedlist2.add(6)
linkedlist.mergealternatively(linkedlist2)

# 4. In an array, Count Pairs with given sum
data = input('comma seperated datas').split(',')
list_data = list(map(int, data))
sum = int(input('sum data'))

for i in range(len(list_data)):
    for j in range(i, len(list_data)):
        if list_data[i] + list_data[j] == sum:
            print('({0},{1})'.format(list_data[i], list_data[j]))

# 5. Find duplicates in an array
from collections import Counter

data = input('comma seperated datas').split(',')
list_data = list(map(int, data))
dic = Counter(list_data)
for k in dic:
    if dic[k] > 1:
        print('duplicate datas found', k, dic[k], 'times')

# 6. Find the Kth largest and Kth smallest number in an array

data = input('comma seperated datas').split(',')
list_data = list(map(int, data))
k = int(input('kth data'))
list_data.sort()
print('kth largest data is', list_data[len(list_data) - k])
print('kth smallest data is', list_data[k - 1])

# 7. Move all the negative elements to one side of the array
data = input('enter comma seperated datas').split(',')
list_data = list(map(int, data))
j = 0
for i in range(0, len(list_data)):
    if (list_data[i] < 0):
        temp_variable = list_data[i]
        list_data[i] = list_data[j]
        list_data[j] = temp_variable
        j = j + 1
print(list_data)


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, val):
        self.stack.append(val)

    def stringreverse(self):
        revstring = ''
        while self.stack != []:
            revstring += self.pop()
        return revstring

    def pushstring(self, string):
        for i in string:
            self.push(i)

    def evalPostfixExp(self, string):
        self.stack = []
        for i in string:
            if i.isdigit():
                self.push(int(i))

            else:
                v1 = self.pop()
                v2 = self.pop()
                if i == '+':
                    self.push(v1 + v2)
                if i == '-':
                    self.push(v2 - v1)
                if i == '*':
                    self.push(v1 * v2)
                if i == '/':
                    self.push(v2 / v1)

        result = self.pop()
        return result

    def dequeue(self):
        if self.stack == []:
            return 'empty stack'
        temp_variable = []
        data = None
        while self.stack != []:
            temp_variable.append(self.pop())
        data = temp_variable.pop()
        self.stack = temp_variable[::-1]

        return data


# 8. Reverse a string using a stack
stack = Stack()
stack.pushstring('checking string')
print(stack.stringreverse())

# 9. Evaluate a postfix expression using stack

result = stack.evalPostfixExp('4572+-*')
print(result)

# 10. Implement a queue using the stack structure
stack.push(11)
stack.push(22)
stack.push(33)
stack.push(14)
stack.push(16)

stack.dequeue()
stack.dequeue()
stack.dequeue()