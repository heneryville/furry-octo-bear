class treeList:
  rootNode=None
  def add(self, data):
    if self.rootNode==None:
      self.rootNode=treeListNode(data, None, None)
    else:
     def addHelper(data, cursor):
        if data<cursor.data:
          if cursor.leftChild==None:
            cursor.leftChild=treeListNode(data, None, None)
          else:
            addHelper(data, cursor.leftChild)
        else:
          if cursor.rightChild==None:
            cursor.rightChild=treeListNode(data, None, None)
          else:
            addHelper(data, cursor.rightChild)
     #invoke AddHelper function    
     addHelper(data, self.rootNode)  
  
  def remove(self, data):
    parentNode=None
    def findNode(cursor, parentNode):
    
      if cursor.data==data:
       return (parentNode, cursor)
      if self.rootNode.data>data:
        cursor=cursor.leftChild
      else cursor=cursor.rightChild
      findNode(data, cursor.leftChild, cursor)
      
      
    
    def getLeftmostNode(data, cursor):
      if cursor.leftChild==None:
        return cursor
      else:
        return: getLeftmostNode(data, cursor.leftChild)
        
        
        
        
  
  
  
  def show(self):
    def printHelper(node, depth):
      if(node == None): return
      printHelper(node.rightChild,depth+1);
      print(('*' * depth) + str(node.data))
      printHelper(node.leftChild,depth+1);
    printHelper(self.rootNode,0)

class treeListNode:
  def __init__(self, data, leftChild, rightChild):
    self.data=data
    self.leftChild=leftChild
    self.rightChild=rightChild

tl=treeList()
tl.add(1)
tl.add(2)
tl.add(3)
tl.add(4)
tl.add(5)
tl.add(6)
tl.add(11)
tl.add(14)

print
tl.removeNode(1)
tl.show();








#  def removeNode(self, data):
#    target==None              
#    def testNode(data, cursor):
#      if cursor.leftChild==None and cursor.rightChild==None:
#        self.rootNode.data=None
#        return
#      if cursor.leftChild==None and cursor.rightChild!=None:
#        
#        if cursor.data<data:
#          testNode(data, cursor.leftChild)
#        else:
#          
#        
#        
#        print "None on left side Only"
#        return
#      if cursor.leftChild!=None and cursor.rightChild==None:
#        print "None on right side Only"
#        return
#      else:
#    testNode(data, self.rootNode)
	
	