class Trie:

    class _Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = [None] * 26

    def __init__(self):
        self._root = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, word):
        cur = self._root
        for c in word:
            index = ord(c.lower()) - ord("a")
            if not cur.next[index]:
                cur.next[index] = self._Node()

            cur = cur.next[index]

        if not cur.is_word:
            cur.is_word = True
            self._size += 1

    def contains(self, word):
        cur = self._root
        for c in word:
            index = ord(c.lower()) - ord("a")
            if not cur.next[index]:
                return False

            cur = cur.next[index]

        return cur.is_word

    def is_prefix(self, prefix):
        cur = self._root
        for c in prefix:
            index = ord(c.lower()) - ord("a")
            if not cur.next[index]:
                return False

            cur = cur.next[index]

        return True


if __name__ == '__main__':
    trie = Trie()
    words = ['panda', 'pandas', 'apple', 'app', 'banana', 'papa']
    for word in words:
        trie.add(word)

    print('panda', trie.contains('panda'))
    print('pan', trie.contains('pan'))
    print('pana', trie.is_prefix('pa'))
    print('zzz', trie.contains('zzz'))
