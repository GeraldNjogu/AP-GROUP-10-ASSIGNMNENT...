class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    # Insert a new word into the trie
    ...

  def delete(self, word):
    # Delete a word from the trie
    ...

  def search(self, word):
    # Search for a word in the trie
    ...

  def starts_with(self, prefix):
    # Find all words that start with a given prefix
    ...

  def _collect_words(self, node, prefix):
    # Helper function for starts_with to collect all words under a node
    ...
