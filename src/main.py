import sys
from search_keyword import KeywordSearcher
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <keyword> <search_path> <output_path>")
        sys.exit(1)
    else:
        print(
        "\n"
        "\n"
        "\n______        _    _                     _____                          _     "
        "\n| ___ \      | |  | |                   /  ___|                        | |    "
        "\n| |_/ /_   _ | |_ | |__    ___   _ __   \ `--.   ___   __ _  _ __  ___ | |__  "
        "\n|  __/| | | || __|| '_ \  / _ \ | '_ \   `--. \ / _ \ / _` || '__|/ __|| '_ \ "
        "\n| |   | |_| || |_ | | | || (_) || | | | /\__/ /|  __/| (_| || |  | (__ | | | |"
        "\n\_|    \__, | \__||_| |_| \___/ |_| |_| \____/  \___| \__,_||_|   \___||_| |_|"
        "\n        __/ |                                                                 "
        "\n       |___/                                                                  "
        "\n"
        "\n"
        )

        keyword = sys.argv[1]
        search_path = sys.argv[2]
        output_path = sys.argv[3]

        searcher = KeywordSearcher(keyword, search_path, output_path)
        searcher.search_keyword()
        logging.info("Search completed!")

        searcher.print_result()
