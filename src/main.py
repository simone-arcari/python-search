import sys
from search_keyword import KeywordSearcher

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <keyword> <search_path> <output_path>")
        sys.exit(1)

    keyword = sys.argv[1]
    search_path = sys.argv[2]
    output_path = sys.argv[3]

    searcher = KeywordSearcher(keyword, search_path, output_path)
    searcher.search_keyword()
    print("Search completed!")

    searcher.print_result()
