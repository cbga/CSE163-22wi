"""
Bingan Chen (AA)
Implements the class SearchEngine with functions included for hw4.
This file constructs a Search Engine for a specific directory,
and searches for a query of words.
"""
import math
import os
import re
from document import Document


class SearchEngine:
    """
    This class represents a search engine for a directory of files
    and search for a query of words in the files.
    """
    def __init__(self, directory):
        """
        Constructs an inverted index associating each term in the corpus
        to the list of documents that contain the term.
        :param directory: A desired directory for the files.
        """
        self._inverted_index = {}
        self._dir = directory
        self._doc_count = 0
        for filename in os.listdir(self._dir):
            self._doc_count += 1
            doc_path = os.path.join(self._dir, filename)
            doc = Document(doc_path)
            for token in doc.get_words():
                if token not in self._inverted_index:
                    self._inverted_index[token] = []
                self._inverted_index[token].append(doc)

    def _calculate_idf(self, term):
        """
        :param term: A desired term to be calculated in inverse document
                    frequency (IDF).
        :return: The calculated IDF for the term.
        """
        term = term.lower()
        if term not in self._inverted_index:
            return 0
        doc_contain_count = len(self._inverted_index[term])
        return math.log(self._doc_count / doc_contain_count)

    def search(self, query):
        """
        :param query: Contains one or more terms to be searched.
        :return: A list of document paths sorted in descending order
                by tf–idf statistic; If there are no matching documents,
                return an empty list.
        """
        result_dic = {}
        result = []
        for term in query.split():
            term = term.lower()
            term = re.sub(r'\W+', '', term)
            if term in self._inverted_index:
                idf = self._calculate_idf(term)
                for single_doc in self._inverted_index[term]:
                    tf = single_doc.term_frequency(term)
                    tfidf = idf * tf
                    single_path = single_doc.get_path()
                    if single_path not in result_dic:
                        result_dic[single_path] = 0
                    result_dic[single_path] += tfidf
        after_sort = sorted(
            result_dic.items(), key=lambda item: item[1], reverse=True
        )
        for d in after_sort:
            result.append(d[0])
        return result
