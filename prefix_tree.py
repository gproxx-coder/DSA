class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.end_of_word

    def starts_with(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


if __name__ == '__main__':
    w = Trie()
    w.insert("Apple")
    print(w.search("Apple"))
    print(w.search("Apply"))
    print(w.search("App"))

    print(w.starts_with("App"))
    print(w.starts_with("Apples"))



