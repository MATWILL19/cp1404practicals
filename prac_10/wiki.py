import wikipedia

INPUT_TEXT = "Enter page title: "

def main():
    """Search for and get a wikipedia page title, summary and url."""
    wiki_input = input(INPUT_TEXT)
    while wiki_input != "":
        try:
            wiki_search = wikipedia.page(wiki_input)
            wiki_title = wiki_search.title
            print(wiki_title)
            wiki_summary = wiki_search.summary
            print(wiki_summary)
            wiki_link = wiki_search.url
            print(wiki_link)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search: ")
            print(e.options)
        wiki_input = input(INPUT_TEXT)
    print("Thank you.")

main()