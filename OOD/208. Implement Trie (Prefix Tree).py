class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        Note Two Attributes
        children and is_end
        """
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self  # note this expr

        for x in word:
            i = ord(x) - 97
            if node.children[i] is None:
                node.children[i] = Trie()  # generate new node
            node = node.children[i]  # node = node.left
        node.is_end = True  # end mark

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for x in word:
            i = ord(x) - 97
            if node.children[i] is None:
                return False
            node = node.children[i]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for x in prefix:
            i = ord(x) - 97
            if node.children[i] is None:
                return False
            node = node.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")
    trie.search("app")
    trie.startsWith("app")
    trie.insert("app")
    trie.search("app")
