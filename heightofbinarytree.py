def findHeight(root):
    if(root==None):
        return 0
    lh=findHeight(root.left)
    rh=findHeight(root.right)
    return 1+max(lh,rh)