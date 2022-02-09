"""
Bingan Chen (AA)
Implements the class SeachEngine with functions included for hw4.
"""
import math
import os
import re
from document import Document


class SearchEngine:
    def __init__(self, directory):
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
        term = term.lower()
        if term not in self._inverted_index:
            return 0
        doc_contain_count = len(self._inverted_index[term])
        return math.log(self._doc_count / doc_contain_count)

    def search(self, query):
        """
        This is comments (not finished)
        """
        result_dic = {}
        result = []
        for term in query.split():
            term = term.lower()
            term = re.sub(r'\W+', '', term)
            if term not in self._inverted_index:
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
