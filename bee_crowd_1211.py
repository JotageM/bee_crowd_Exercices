# class Trienode:
#     def __init__(self):
#         self.children = [None] * 10
#         self.isLeaf = False
# class Trie():
#     def __init__(self) -> None:
#         self.root = Trienode()

#     def insert(self,word: str):
#         current = self.root
#         for number in word:
#             index = ord(number) - ord('0')
#             if not current.children[index]:
#                 current.children[index] = Trienode()
#             current = current.children[index]
#         current.isLeaf = True


#     def count_nodes(self):
#         return self._test_nodes(self.root)

#     def _test_nodes(self, node):
#         if node is None:
#             return 0

#         count = 1
#         for child in node.children:
#             count += self._test_nodes(child)

#         return count

# while True:
#     try:
#         n = int(input())
#         total_digits = 0
#         trie = Trie()
#         for i in range(n):
#             number = input()
#             trie.insert(number)
#             total_digits += len(number)


#         nodes = int(trie.count_nodes()-1)
        
#         print(total_digits - nodes)

#     except EOFError:
#         break


def calculate_savings(numbers):
    if not numbers:
        return 0
    
    saved_chars = 0
    prev_number = numbers[0]

    for i in range(1, len(numbers)):
        current_number = numbers[i]
        common_prefix_len = 0

        # Calcula o comprimento do prefixo comum entre o número atual e o anterior
        for j in range(len(current_number)):
            if current_number[j] == prev_number[j]:
                common_prefix_len += 1
            else:
                break
        
        saved_chars += common_prefix_len
        prev_number = current_number
    
    return saved_chars

while True:
    try:
        n = int(input())
        numbers = [input().strip() for _ in range(n)]
        print(calculate_savings(numbers))

    except EOFError:
        break

