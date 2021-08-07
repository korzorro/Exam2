#Question 1: Dynamic Programming
#PYTHON

class Node:

    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
        self.mvis = None
        self.mvis_set = []


def MVIS(root): # Maximum value of the independent set (MVIS)
    if not root: # Base case: root is None, zero, or empty
        return (0, [])
    
    if not root.children: # Base case: root is a leaf
        return (root.val, [root.val])
    
    child_vals = []
    child_sum = 0
    grandchild_vals = [root.val]
    grandchild_sum = root.val

    # Sum of mvis of all children, and sum of mvis of all grandchildren
    # Also keeps track of the independent set itself at each stage
    for child in root.children:
        if not child.mvis:
            child.mvis, child.mvis_set = MVIS(child) # Memoization
        child_vals += child.mvis_set
        child_sum += child.mvis
        # Grandchildren loop
        for child in child.children:
            if not child.mvis:
                child.mvis, child.mvis_set = MVIS(child) # Memoization
            grandchild_vals += child.mvis_set
            grandchild_sum += child.mvis

    # Always returns the maximum mvis between the root node's children and
    # grandchildren and the set itself
    return max(
        (child_sum, child_vals),
        (grandchild_sum, grandchild_vals),
        key=lambda x: x[0])

# Build the original tree from Q1
root = Node(3, [
    Node(4, [
        Node(1), Node(2)]),
    Node(1, [
        Node(2)]),
    Node(5, [
        Node(1), Node(1)])])

# call function with root node(3)
solution = MVIS(root)

print(solution)
# Output (11, [4, 2, 5])
# I could return the nodes themselves instead of their values, but for this
# exercise, there's only one combination of [4, 2, 5] possible.
