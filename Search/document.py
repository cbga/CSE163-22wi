"""
Bingan Chen (AA)
Implements the class Document with functions included for hw4.
This file constructs a class representing a single file, get the term
frequency of a term, get the path of this file, the unique words in
the doc.
"""
import re


class Document:
    """
    This class represents the data in a single web page and includes
    methods to compute term frequency.
    """
    def __init__(self, doc_path):
        """
        Initialize a document's data by taking a path of the document.
        :param doc_path: the path of a specific document.
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
        :param term: A given term to be computed for TF.
        :return: The term frequency of the specified term; If term does
        not appear in the document, returns 0.
        """
        term = term.lower()
        term = re.sub(r'\W+', '', term)
        if term not in self._dic:
            return 0
        return self._dic[term]

    def get_path(self):
        """
        :return: The path of this document.
        """
        return self._file_path

    def get_words(self):
        """
        :return: A list of unique normalized words in this doc.
        """
        return list(self._dic.keys())
