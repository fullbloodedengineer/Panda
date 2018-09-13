class Socket:
    def __init__(self,owner,sID='State'):
        self.id = sID
        self.direction = 1 #-1 in, +1 is out
        self.maxConnections = -1 #-1 is infinite
        self.owner = owner
        self.connections = 0
        self.properties = {}
    def isOppositeConnection(self,other):
        return self.direction + other.direction == 0

    def acceptAnotherConnection(self):
        return self.maxConnections > self.connections
    
    def acceptVisitor(self,visitor):
        pass

class Edge:
    def __init__(self,target=None,sorce=None,weight=1):
        self.socket = socket
        self.target = target #socket
        self.source = source #socket
        self.weight = 1

    def setFirstConnection(self,socket):
        if socket.direction > 0:
            self.target = socket
        else:
            self.source = socket
        
    def setSecondConnection(self,socket,validate=True):
        if socket.direction > 0 and :
            self.target = socket
        else:
            self.source = socket

        if validate:
            self.connectEdge()

    def connectEdge(self):
        valid = False
        if self.target.isOppositeConnection(self.source):
            if self.target.acceptAnotherConnection() and self.source.acceptAnotherConnection():
                valid = True
            else:
                raise ValueError, "A chosen socket can't accept more connections"               
        else:
            raise ValueError, "Sockets must be of opposite directions"

        return valid

    def acceptVisitor(self,visitor):
        pass

class Node:
    '''A node is graph item that can have properties and multiple sockets. Every Node has at least one socket (state) used for output''' 
    def __init__(self,id="Node"):
        self.factory = None #Used to create the visual items
        self.sockets = {
                        intput:set([]),
                        ouptut:set(Socket(self))
                        } #Sockets are the connectable properties
        self.properties = {}

    def acceptVisitor(self,visitor):
        #A visitor can change my values and cause a reaction to the event
        pass

class Graph:
    def __init__(self,id="Base"):
        self.id = id
        self.nodes = {}
        self.edges = {} #Target:Source

    def acceptVisitor(self,visitor):
        pass

    def startEdge(self,socket):
        tmpEdge = Edge()
        tmpEdge.setFirstConnection(socket)
        self.currentEdge = tmpEdge

    def doesEdgeExist(self,edge):
        '''Check edges to see if this combination of sockets exists already'''
        pass

    def finishEdge(self,socket):
        if self.currentEdge.setSecondConnection(socket):
            self.edges[self.tmpEdge.id] = tmpEdge
        tmpEdge = None #Clear value for next edge      

    def addEdgeDirect(self,edge):
        self.edge[edge.id] = edge
          
    def createNode(self,nodeID):
        if not self.nodes.has_id(nodeID):
            node = Node(id=nodeID)
            self.nodes[nodeID] = node
            return node
        else:
            raise ValueError, "Node ID %s already exists in the graph" %node.id            
        
    def addNode(self,node):
        if isinstance(node,Node):
            if self.nodes.has_key(node.id):
                raise ValueError, "Node ID %s already exists in the graph" %node.id
            else:
                self.nodes[node.id] = node
        else:
            raise ValueError, "%s is not of type Node" %node