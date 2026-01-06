from ds import BinarySearchTree, Queue, Array
from typing import TypeVar

T = TypeVar("T")

def breadth_first_search(bst: BinarySearchTree[T], value: T) -> bool:
    """Perform a breadth first search on a binary search tree to see if the given target is within the tree.
    
    Time complexity in the best case occurs when the target value is the first node in the tree which leads to O(1). In the worst case, time complexity is O(n) given that it made be the bottom right node, leading us to have to traverse n nodes. In the average case, we have traverse n / 2 nodes to leading to O(n), Space complexity is O(1) in the best case and O(n) in the average and worst cases given that we have to store a fraction of the tree's nodes in a queue, at worst being n / 2.
    """
    if bst.root is None:
        return False
    # fi
    
    queue: Queue[BinarySearchTree.Node] = Queue(Array(bst.root))

    while queue.length() != 0:
        node = queue.dequeue()

        if node.value == value:
            return True

        if node.left is not None:
            queue.enqueue(node.left)
        # fi

        if node.right is not None:
            queue.enqueue(node.right)
        # fi
    # elihw

    return False
# fed
        
        
    
