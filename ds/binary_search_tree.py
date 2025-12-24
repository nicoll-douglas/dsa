from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")

class BinarySearchTree(Generic[T]):
    """A class that implements a binary search tree.

    Let h be the height of the tree throughout. The approximate value of h thus depends of if the tree is balanced or not. If the tree is balanced, left and right subtrees for any node have roughly the same amount of nodes. Thus, level 0 (root) would have 1 node, level 1 would have about 2, level 2 about 4 and so on until we reach level h giving us about 2^h nodes. If n is the number of nodes then n ~= 2^0 + 2^1 + 2^2 + ... + 2^h = 2^(h+1) - 1. Performing some rough algebra, this would give us h ~= log(n) in the case that it is balanced. If the tree is unbalanced then let us assume the worst case where the tree looks like a linked list of nodes. This would mean that h = n.
    """

    class BinarySearchTreeViolationError(ValueError):
        """Custom error class for a binary search tree violation (duplicate element)."""

        def __init__(self):
            super.__init__("Binary search tree violation, attempted insert of duplicate element")
        # fed
    # ssalc

    class _Node:
        """Class that implements a node in the binary search tree."""

        value: T # The value of the node
        left: _Node | None # The node left of the current in the tree
        right: _Node | None # The node right of the current in the tree

        def __init__(self, value: T):
            """Initialise the node with the given value and null leaf nodes."""
            self.value = value
            self.left = None
            self.right = None
        # fed
    # ssalc

    _root: BinarySearchTree._Node | None # The root node of the binary search tree

    def __init__(self):
        """Initialise an empty binary search tree."""
        self._root = None
    # fed

    def _insert_rec(self, node: _Node | None, value: T) -> _Node:
        """Recursively traverse a node's subtree to insert a node at the correct position.

        In the base case, the given node will be an empty leaf node so the algorithm will have found the correct position to insert a node and return a new node. In the recursive case, we either traverse into the left subtree or right subtree by comparing the given value to insert with the value of the node. We return the given node in order to update it with any modifications from recursion in the previous method call.

        Arguments
        ---------
        node
            A node in the binary search tree or None representing an empty leaf node.

        value
            The value to give to a new node being inserted into the tree.

        Raises
        ------
        BinarySearchTree.BinarySearchTreeViolationError
            If a value trying to be inserted into the tree is already present.

        Returns
        -------
        The given node or a new node.
        """
        if node is None:
            # base recursion case - null leaf node found so return a new node to insert in the previous method call
            return self._Node(value)
        # fi

        if value < node.value:
            # recursive case - if smaller, recurse into left subtree and update node.left (it will then point to newly inserted node or updated subtree)
            node.left = self._insert_rec(node.left, value)
        elif value > node.value:
            # recusrive case - if bigger, recursive into right subtree and update node.right (it will then point to newly inserted node or updated subtree)
            node.right = self._insert_rec(node.right, value)
        else:
            # else values are the same but no duplicates are allowed
            raise self.BinarySearchTreeViolationError
        # fi

        # return given node so its subtree can be re-registered with any modifications in the previous method call
        return node
    # fed

    def insert(self, value: T) -> None:
        """Insert a value into the binary search tree or raise a BinarySearchTreeViolationError if the value is already present.

        Time complexity is O(h) since we are relying on recursively iterating down the levels of the tree to find the correct position to insert the new value. Space complexity is also O(h) since each recusrive call adds an extra frame onto the call stack.
        """
        self._root = self._insert_rec(self._root, value)
    # fed

    def _find_min(self, node: _Node) -> T:
        """Find the node with the smallest value in the subtree of the given node and return it."""
        while node.left is not None:
            node = node.left
        # elihw

        return node
    # fed

    def _delete_rec(self, node: _Node | None, value: T) -> _Node | None:
        """Recursively traverse a node's subtree to find and delete the given value if it exists.
        
        In the first base case, the given node will be an empty leaf node meaning that the algorithm won't have found the value so we return the same value for the node to preserve it. In the second case, the value/node is found and it has no children so we return None to remove the node. In the third base case the found node only has one child so we return that child to substitute the given node with it. In the first recursive case, the value is smaller than the given node's value so we recurse into the left subtree of the node to try and find the value there. The second recursive case mirros the first, so the value would be bigger and we would recurse into the right subtree of the give node to try and find the value there.

        Arguments
        ---------
        node
            A node in the binary search tree or None representing an empty leaf node.

        value
            The value to delete from the binary search tree.

        Returns
        -------
        A node containing modifications.
        """
        if node is None:
            # base recursion case 1 - we have a reached a null leaf node without finding the given value so return None to preserve the node
            return None
        # fi

        if value < node.value:
            # recursive case 1 - if smaller, recurse into left subtree and update node.left (it will then point to an updated subtree with the value deleted)
            node.left = self._delete_rec(node.left, value)
        elif value > node.value:
            # recursive case 2 - if bigger, recurse into right subtree and update node.right (it will then point to an updated subtree with the value deleted)
            node.right = self._delete_rec(node.right, value)
        else:
            # base recursion case 2 - current node has no children, return None to delete the node by substituting it with an empty leaf node
            if node.left is None and node.right is None:
                return None
            # fi

            # base recursion case 3.1 - current node only has a right child so return the right child to delete the node by substituting it with the right child
            if node.left is None:
                return node.right
            # fi

            # base recursion case 3.2 - current node only has a left child so return the left child to delete the node by substituting it with the left child
            if node.right is None:
                return node.left
            # fi
            
            # recursive case 3 - current node has 2 children so find the in-order successor of the node (next smallest value) and replace the node's value with it then deleting the successor node
            successor: _Node = self._find_min(node.right) # find successor
            node.value = successor.value # replace current node value with successor value
            node.right = self._delete_rec(node.right, successor.value) # delete the successor
        # fi

        # return given node so its subtree can be re-registered with any modifications in the previous method call
        return node
    # fed

    def delete(self, value: T) -> None:
        """Delete a value from the binary search tree.

        Time complexity is O(h) since we are relying on recursively iterating down the levels of the tree to find the correct position of the value to delete. Space complexity is also O(h) since each recursive call adds an extra frame onto the call stack.
        """
        self._root = self._delete_rec(self._root, value)
    # fed 

    def _search_rec(self, node: _Node | None, value: T) -> bool:
        """Recursively traverse a node's subtree to search for a given value within it.
        
        In the first base case we reach a null leaf node so the target value won't have been found so we return False. In the second base case the target value equals the value of the current node so we return True. In the first recursive case the target value is less than the value of the given node so we recurse into its left subtree. The second recursive mirrors the first, so the target value would be greater than the value of the given node making us recurse into its right subtree.
        """
        if node is None:
            # base recursion case 1 - we have reached a null leaf node so the value can't possible exist in the node's subtree; return False
            return False
        # fi

        if value < node.value:
            # recursive case 1 - the target value is less than the given node's so recurse into the node's left subtree; return the result of subsequent recursion
            return self._search_rec(node.left, value)
        # fi

        if value > node.value:
            # recursive case 2 - the target value is greater than the given node's so recurse into the node's right subtree; return the result of subsequent recursion
            return self._search_rec(node.right, value)
        # fi

        # base recursion case 2 - the target value equals the value of the given node so it has been found; return True
        return True
    # fed

    def search(self, value: T) -> bool:
        """Search for a value in the binary tree and return a flag indicating whether it is present.
        
        Time complexity is O(h) since we are relying on recursively iterating down the levels of the tree to find the target value. Space complexity is also O(h) since each recursive call adds an extra frame onto the call stack.
        """
        return self._search_rec(self._root, value)
    # fed
# ssalc
