# input exercise
book_title_input = input("what is the book title: ")
page_count_input = int(input("what is the page count: "))


def classify_book(page_count_input):
    if page_count_input > 100:
        return "full-length book"
    else:
        return "short book"
result_page_count = classify_book(page_count_input)

print(f"{book_title_input} is: {result_page_count}")