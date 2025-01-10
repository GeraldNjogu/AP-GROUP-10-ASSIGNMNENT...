class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False
            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char in node.children:
                should_delete_child = _delete(node.children[char], word, depth + 1)
                if should_delete_child:
                    del node.children[char]
                    return not node.is_end_of_word and len(node.children) == 0
            return False
        _delete(self.root, word, 0)
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_words(node, prefix)
    def _collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._collect_words(child_node, prefix + char))
        return words
