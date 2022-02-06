from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine


def test_document():
    doc0 = Document('doc_test/doc_test_0.txt')
    assert_equals(0.125, doc0.term_frequency('cities'))

    doc1 = Document('doc_test/doc_test_1.txt')
    assert_equals('doc_test/doc_test_1.txt', doc1.get_path())

    doc2 = Document('doc_test/doc_test_2.txt')
    assert_equals(['i', 'like', 'eating', 'apples'], doc2.get_words())


def test_search_engine():
    engine = SearchEngine('self_some_docs/')
    assert_equals(['self_some_docs/doc1.txt'], engine.search('apples'))
    assert_equals([], engine.search('pineapples'))
    assert_equals(['self_some_docs/doc2.txt', 'self_some_docs/doc1.txt'], engine.search('are fresh'))
    assert_equals([], engine.search(' ! pineapples apples'))

    print(engine.get_map())


def main():
    test_document()
    test_search_engine()


if __name__ == '__main__':
    main()
