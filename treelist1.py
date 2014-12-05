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
	 

class treeListNode:
  def __init__(self, data, leftChild, rightChild):
		self.data=data
		self.leftChild=leftChild
		self.rightChild=rightChild

tl=treeList()
tl.add(10)
tl.add(5)
tl.add(15)

print tl.rootNode.data
print tl.rootNode.leftChild.data
print tl.rootNode.rightChild.data


	
	