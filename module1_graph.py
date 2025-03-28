import networkx as nx

class ResourceAllocationGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Directed Graph (Process → Resource, Resource → Process)

    def add_process(self, process): # The processes are added here
        if process not in self.graph: # Process nodes are added (like P1,P2..etc)
            self.graph.add_node(process, type="process")
            print(f"Process {process} added.")
        else:
            print(f"Process {process} already exists!") # If process is already present then the message will pop

    def add_resource(self, resource):
        if resource not in self.graph:    # Resources nodes are added (like R1,R2..etc)
            self.graph.add_node(resource, type="resource")
            print(f"Resource {resource} added.")
        else:
            print(f"Resource {resource} already exists!") # If Resources is already present then the message will pop

    def request_resource(self, process, resource): # Process can request a resource
        if process in self.graph and resource in self.graph:
            self.graph.add_edge(process, resource)  # P1 → R1
            print(f" {process} requested {resource}.")
        else:
            print("Invalid process/resource!")

    def allocate_resource(self, resource, process): # Resources can be allocated to the processes
        if resource in self.graph and process in self.graph:
            self.graph.add_edge(resource, process)  # R1 → P2
            print(f" {resource} allocated to {process}.")
        else:
            print("Invalid process/resource!")

    def remove_edge(self, node1, node2): # Remove  edge between process/resource
        if self.graph.has_edge(node1, node2):
            self.graph.remove_edge(node1, node2)
            print(f"Edge removed: {node1} → {node2}")
        else:
            print("No such edge exists!")

    def show_graph(self): # It will display the graph structure
        print("Resource Allocation Graph:")
        for edge in self.graph.edges:
            print(f"{edge[0]} → {edge[1]}")

# Example
rag = ResourceAllocationGraph()
rag.add_process("P1")
rag.add_process("P2")
rag.add_resource("R1")
rag.add_resource("R2")

rag.request_resource("P1", "R1")  # P1 → R1
rag.allocate_resource("R1", "P2")  # R1 → P2

rag.show_graph()
