from ranking import compute_ranks
from webCrawler import crawl_web


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None


def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if ranks[candidate] > best_page:
            best_page = ranks[candidate]
    return best_page


def search(keyword):
    index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
    ranks = compute_ranks(graph)
    print lucky_search(index, ranks, keyword)


