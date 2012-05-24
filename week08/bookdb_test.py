import bookdb

def test_list_books():
    books = bookdb.BookDB()
    titles = books.titles()
    assert len(titles) > 1
    print titles
    for title in titles:
        assert 'title' in title
        assert 'id' in title

def test_get_book_info():
    books = bookdb.BookDB()
    titles = books.titles()
    id = titles[0]['id']
    print id
    info = books.title_info(id)
    print info
    assert 'title' in info
    assert info['title'] == titles[0]['title']
    assert 'publisher' in info
    assert 'isbn' in info
    assert 'author' in info

