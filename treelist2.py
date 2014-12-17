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
				return
			#invoke addHelper function    
			addHelper(data, self.rootNode)  
  
	def remove(self, data):
		parentNode=self.rootNode
		
		if self.rootNode.data==data:
			if self.rootNode.leftChild==None and self.rootNode.rightChild==None:
				self.rootNode=None
				return
			if self.rootNode.rightChild==None:
				self.rootNode=self.rootNode.leftChild
				return
		
	
		def findNode(data, cursor, parentNode):
			print cursor, parentNode, cursor.data, data
			if cursor.data==data:
				return cursor
			if cursor.data>data:
				parentNode=cursor
				cursor=cursor.leftChild
			else: 
				parentNode=cursor
				cursor=cursor.rightChild
			findNode(data, cursor, parentNode)
	  
	  
		def getClosestReplacementNode(data, cursor, parentNode):
			print cursor
			if cursor.leftChild==None:
				data=cursor.data
				if cursor.rightChild==None:
					parentNode.leftChild=None
					return data
				else:
					parentNode.leftChild=cursor.rightChild
					return data
			else:
				getClosestReplacementNode(data, cursor.leftChild, cursor)
				
				
		nodeBeingRemoved=findNode(data, parentNode, parentNode)
		print nodeBeingRemoved
		nodeBeingRemoved.data=getClosestReplacementNode(0, nodeBeingRemoved, parentNode) 
		
  
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
tl.add(20)
tl.add(30)
tl.add(10)
tl.add(5)
tl.add(14)
tl.add(25)
tl.add(3)
tl.add(6)
tl.add(12)
tl.add(18)
tl.add(21)
tl.add(20)
tl.add(22)
tl.add(24)


tl.remove(21)
tl.show();






	
