import random


class Page:
    def __init__(self, id):
        self.id = id
        self.referenced = 0
        self.modified = 0

    def __repr__(self):
        return f"Page({self.id}, R={self.referenced}, M={self.modified})"


def nru_replacement(pages):
    classes = {0: [], 1: [], 2: [], 3: []}

    for page in pages:
        category = 2 * page.referenced + page.modified
        classes[category].append(page)

    for i in range(4):
        if classes[i]:
            return random.choice(classes[i])

    return None

def main():
    pages = [Page(i) for i in range(5)]

    pages[0].referenced, pages[0].modified = 1, 0
    pages[1].referenced, pages[1].modified = 1, 1
    pages[2].referenced, pages[2].modified = 0, 0
    pages[3].referenced, pages[3].modified = 0, 1
    pages[4].referenced, pages[4].modified = 1, 0

    print("Páginas antes da substituição:", pages)
    removed_page = nru_replacement(pages)
    print("Página removida:", removed_page)

if __name__ == "__main__":
    main()