class Node :
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self) -> None:
        self.head=None

    def append(self,data):
        node=Node(data)

        if self.head is None:
            self.head=node
            return
        else:
            last_node=self.head
            while last_node.next is not None:
                last_node=last_node.next
            last_node.next=node
 
    def print_node(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.next

    def prepend(self,data):
        node=Node(data)
        node.next=self.head
        self.head=node

    def middle(self,pre_node,data):
        
        node=Node(data)
        node.next=pre_node.next
        pre_node.next=node

    def delete_node(self,data):
        cur=self.head
        if cur is not None and cur.data==data:
            self.head=cur.next
            cur=None
            return
        else:
            pre=None
            while cur is not None and cur.data ==data:
                pre=cur
                cur=cur.next

            if cur is None:
                return
            else:
                pre.next=cur.next
                cur=None

    def delete_node_pos(self,pos):
        cur=self.head
        if pos==0:
            self.head=cur.next
            cur=None
            return

        else:
            pre=self.head
            count=1
            while cur is not None and count==pos:
                pre=cur
                cur=cur.next
                count+=1

            if cur is None:
                return
            else:
                pre.next=cur.next
                cur=None



if __name__=='__main__':
    lst=Linked_List()
    lst.append('A')
    lst.append('B')
    lst.append('C')
    lst.append('D')
    lst.append('E')
    lst.print_node()
    '''
    lst.prepend('C')
    lst.middle(lst.head,'D')
    lst.middle(lst.head.next,'F')
    lst.print_node()
    print()

    #lst.delete_node('A')
    #lst.delete_node('C')
    # '''
    lst.delete_node_pos(2)

    #lst.print_node()
