import networkx as nx
# To prevent the deadlocks
class DeadlockPrevention:
    def __init__(self, graph):
        self.graph = graph  # RAG
        self.resource_order = {}  # Fixed priority order for Circular Wait Prevention

    def set_resource_order(self, order): # Set fixed order for Circular Wait Prevention
        self.resource_order = order

    def request_resources_safely(self, process, requested_resources):# Hold and Wait prevention - Process requests all required resources at once
        for res in requested_resources:
            if self.graph.has_edge(res, process):  # Already allocated
                print(f"{res} is already allocated! Request denied.")
                return False

        for res in requested_resources:
            self.graph.add_edge(process, res)  # Pi → Ri
            print(f"{process} requested {res} (Hold & Wait Prevention).")
        return True

    def request_resource_ordered(self, process, resource): # Circular - Wait prevention- Processes must request resources in increasing order.
        allocated_resources = [
            res for res in self.graph.predecessors(process)
            if res in self.resource_order
        ]
        if allocated_resources:
            max_allocated = max(allocated_resources, key=lambda r: self.resource_order[r])
            if self.resource_order[resource] < self.resource_order[max_allocated]:
                print(f"{process} cannot request {resource} (Violates Circular Wait Prevention).")
                return False
        self.graph.add_edge(process, resource)
        print(f"{process} requested {resource} (Circular Wait Prevention).")
        return True

#  Example 
if __name__ == "__main__":
    from module1_graph import ResourceAllocationGraph  # Importing a graph module
    rag = ResourceAllocationGraph()
    rag.add_process("P1")
    rag.add_process("P2")
    rag.add_resource("R1")
    rag.add_resource("R2")
    prevention = DeadlockPrevention(rag.graph)
    prevention.set_resource_order({"R1": 1, "R2": 2}) 
    prevention.request_resources_safely("P1", ["R1", "R2"]) # safe request (hold and wait prevention)
    # Circular Wait Prevention Test
    prevention.request_resource_ordered("P2", "R1")
    prevention.request_resource_ordered("P2", "R2")  # Allowed
    prevention.request_resource_ordered("P2", "R1")  # Not Allowed 
