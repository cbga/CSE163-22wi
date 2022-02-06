"""
Bingan Chen (AA)
Implements the class Document with functions included for hw4.
"""
import re


class Document:
    """
        This is comments (not finished)
    """
    def __init__(self, doc_path):
        """
        This is comments (not finished)
        """
        self._file_path = doc_path
        self._dic = {}
        self._word_count = 0
        with open(doc_path) as doc:
            for line in doc.readlines():
                for token in line.split():
                    token = token.lower()
                    token = re.sub(r'\W+', '', token)
                    self._word_count += 1
                    if token not in self._dic:
                        self._dic[token] = 0
                    self._dic[token] += 1
        for string in self._dic.keys():
            self._dic[string] /= self._word_count

    def term_frequency(self, term):
        """
        This is comments (not finished)
        """
        term = term.lower()
        term = re.sub(r'\W+', '', term)
        if term not in self._dic:
            return 0
        return self._dic[term]

    def get_path(self):
        """
        This is comments (not finished)
        """
        return self._file_path

    def get_words(self):
        """
        This is comments (not finished)
        """
        return list(self._dic.keys())