import networkx as nx

class DeadlockDetector:
    def __init__(self, graph):
        self.graph = graph  # Taking Resource Allocation Graph 

    def detect_deadlock(self): # To check the deadlock detection (circular dependencies in a directed graph)
        try:
            cycle = list(nx.find_cycle(self.graph, orientation="original"))  # Detect cycle
            print("Deadlock Detected! Cycle:", cycle)
            return True, cycle
        except nx.NetworkXNoCycle:
            print("No Deadlock Found.")
            return False, []
# Example
if __name__ == "__main__":
    from module1_graph import ResourceAllocationGraph  # Importing Module 1
    # Step 1- Create Graph
    rag = ResourceAllocationGraph()
    rag.add_process("P1")
    rag.add_process("P2")
    rag.add_resource("R1")
    rag.add_resource("R2")
    # Deadlock Scenario (Circular Dependency)
    rag.request_resource("P1", "R1")  # P1 → R1
    rag.allocate_resource("R1", "P2")  # R1 → P2
    rag.request_resource("P2", "R2")  # P2 → R2
    rag.allocate_resource("R2", "P1")  # R2 → P1 (Deadlock)
    # Step 2- Checking Deadlock
    detector = DeadlockDetector(rag.graph)
    detector.detect_deadlock()
