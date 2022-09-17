from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse.csgraph import breadth_first_order


def find_minimum_spanning_tree(subtree):
    """
    Returns:
        The N x N compressed-sparse representation of the undirected minimum
        spanning tree over the input
    """
    result = minimum_spanning_tree(subtree)

    return result.toarray().astype(int)


def find_breadth_order(subtree):
    """
    BFS is a traversal approach in which we first walk through all nodes on the same level before moving on to the next level.  
    """
    return breadth_first_order(subtree, i_start=0, directed=False, return_predecessors=False)



if __name__ == "__main__":


    """
    It's used a  graph with four-component.
    Example of a minimum spanning tree after its computatation.
    
         input graph             minimum spanning tree
             (0)                         (0)
            /   \                           \
           8     3                           3
          /       \                           \
        (3)---6---(1)               (3)       (1)
          \       /                   \       /
           1     2                     1     2
            \   /                       \   /  
             (2)                         (2)
    """

    # The N x N matrix representing an undirected graph over N nodes
    subtree = csr_matrix([
                          [0, 3, 0, 8],
                          [0, 0, 2, 6],
                          [0, 0, 0, 1],
                          [0, 0, 0, 0]
                        ])

    # Computation of matrix by finding the min span tree
    min_tree = find_minimum_spanning_tree(subtree) 

    #It's used BFS by finding shortest path from the span tree
    result = find_breadth_order(min_tree)
    print(result)

