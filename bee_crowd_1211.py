class Trienode:
    def __init__(self):
        self.children = [None] * 10
        self.isLeaf = False
class Trie():
    def __init__(self) -> None:
        self.root = Trienode()

    def insert(self,word: str):
        current = self.root
        for number in word:
            index = ord(number) - ord('0')
            if not current.children[index]:
                current.children[index] = Trienode()
            current = current.children[index]
        current.isLeaf = True


    def count_nodes(self):
        return self._test_nodes(self.root)

    def _test_nodes(self, node):
        if node is None:
            return 0

        count = 1
        for child in node.children:
            count += self._test_nodes(child)

        return count

while True:
    try:
        n = int(input())
        total_digits = 0
        trie = Trie()
        for i in range(n):
            number = input()
            trie.insert(number)
            total_digits += len(number)


        nodes = int(trie.count_nodes()-1)
        
        print(total_digits - nodes)

    except EOFError:
        break



