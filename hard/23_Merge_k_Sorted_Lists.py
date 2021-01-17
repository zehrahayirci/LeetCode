# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        indexes = [0 for i in range(k)]
        prev = None 
        start = None
        
        tk = k
        
        items = []
        j = 0
        jmap = {}
        for i in range(k):
            if lists[i]!= None:
                jmap[i] = j
                items.append([lists[i].val,i])
                j+=1
            else:
                tk-=1
        
        if tk == 0:
            return None
        
        finished = 0
        while finished < tk:
            a = min(items, key = lambda x: x[0])
            if prev is None:
                start = lists[a[1]]
                prev = lists[a[1]]
                if lists[a[1]].next:
                    lists[a[1]] = lists[a[1]].next
                    items[jmap[a[1]]][0] = lists[a[1]].val
                else:
                    items[jmap[a[1]]][0] = 1e6  
                    finished += 1                
                continue
            else: 
                prev.next = lists[a[1]]
                prev=prev.next
                if lists[a[1]].next:
                    lists[a[1]] = lists[a[1]].next
                    items[jmap[a[1]]][0] = lists[a[1]].val
                else:
                    items[jmap[a[1]]][0] = 1e6  
                    finished += 1
    
        return start
        
        
    '''   
    def mergeKLists(self, lists):   
        k =len(lists)
        #print(k)
        smallest = 100000
        small_index = 0
        
        start=None
        if k == 0 :
            return None
        for i in range(k):
            if not lists[i]:
                return self.mergeKLists(lists[0:i]+lists[i+1:])
            if lists[i].val < smallest:
                smallest=lists[i].val
                small_index = i
        #print(smallest,small_index)
        if smallest < 100000:
            start = lists[small_index]
            lists[small_index] = lists[small_index].next
            start.next=  self.mergeKLists(lists)
        return start
    '''