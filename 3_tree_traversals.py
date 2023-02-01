def preorder (tree, index):
    if (index <= len (tree) and tree[index - 1] != None):
        print (tree[index - 1], end=" ")
        preorder (tree, 2 * index)
        preorder (tree, 2 * index + 1)

def inorder (tree, index):
    if (index <= len (tree) and tree[index - 1] != None):
        inorder (tree, 2 * index)
        print (tree[index - 1], end=" ")
        inorder (tree, 2 * index + 1)

def postorder (tree, index):
    if (index <= len (tree) and tree[index - 1] != None):
        postorder (tree, 2 * index)
        postorder (tree, 2 * index + 1)
        print (tree[index - 1], end=" ")

tree = [1, 2, 3, 4, 5, None, 7, 8, None, None, None, None, None, 14]

preorder (tree, 1)