from Assignment2.TreeNode import TreeNode


class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


root = TreeNode(2, TreeNode(1), TreeNode(3))
codec = Codec()
data = codec.serialize(root)
print(data)
ans = codec.deserialize(data)





