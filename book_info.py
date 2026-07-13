# book_title = "Trustee and Executor Administration Logbook"
# price = 18.99
# page_count = 50
# is_published = True
# author_name = "oussama"

# print(book_title)
# print(price)
# print(page_count)
# print(is_published)
# print(author_name)

# print(f"Book: {book_title}")
# print(f"Price: {price}")
# print(f"This book has {page_count} pages.")
# print(f"Published status: {is_published}")
# print(f"Author: {author_name}")

# print(f"{book_title} has {page_count} pages and cost ${price}.")

# mystery_value = "18.99"
# print(type(mystery_value))
# print(type(price))

# if page_count > 100
#     print(f"{book_title} is a full-length book.")
# else:
#     print(f"{book_title} is a short book.")


# print(int(10.5))


# book_titles = ["Trustee and Executor Administration Logbook","Conservatorship and Adult Guardianship Reporting Logbook","Family Heirloom and Personal Property Distribution Ledger"]

# for title in book_titles: 
#     print(f"Processing: {title}")
#     print(f"{title} is ready to publish.")

# page_counts = [50, 120, 90]

# for pages in page_counts:
#     if pages > 100:
#         print(f"{pages} pages: full-length book")
#     else:
#         print(f"{pages} pages: short book " )

# book = {
#     "title": "Trustee and Executor Administration Logbook",
#     "price": 18.99,
#     "page_count": 120,
#     "author": "oussama"
# }

# print(f"{book['title']} has {book['page_count']} pages.")

# books = [
#     {"title": "Trustee and Executor Administration Logbook", "price": 12.99, "page_count": 80},
#     {"title": "Conservatorship and Adult Guardianship Reporting Logbook", "price": 18.99, "page_count": 120},
#     {"title": "Family Heirloom and Personal Property Distribution Ledger", "price": 9.99, "page_count": 50}
# ]

# for book in books:
#     print(f"{book['title']} - ${book['price']} - {book['page_count']} pages.")

# books = [
#     {"title": "Trustee and Executor Administration Logbook", "price": 12.99, "page_count": 80},
#     {"title": "Conservatorship and Adult Guardianship Reporting Logbook", "price": 18.99, "page_count": 120},
#     {"title": "Family Heirloom and Personal Property Distribution Ledger", "price": 9.99, "page_count": 50}
# ]

# for book in books:
#     if book['page_count'] > 100:
#         print(f"{book['title']} is full lengheth.")
#     else:
#         print(f"{book['title']} is short.")

# Version A: prints inside
# def classify_print(pages):
#     if pages > 100:
#         print("full-length book")
#     else:
#         print("short book")

# # Version B: returns a value
# def classify_return(pages):
#     if pages > 100:
#         return "full-length book"
#     else: 
#         return "short book"
    

# result_a = classify_print(120)
# print(f"A gave me: {result_a}")

# result_b = classify_return(120)
# print(f"B gave me: {result_b}")


def classify_book(page_count):
    # your if/else here, using return
    if page_count > 100:
        return "full-length book"
    else:
        return "short book"

books = [
    {"title": "Trustee and Executor Administration Logbook", "price": 12.99, "page_count": 80},
    {"title": "Conservatorship and Adult Guardianship Reporting Logbook", "price": 18.99, "page_count": 120},
    {"title": "Family Heirloom and Personal Property Distribution Ledger", "price": 9.99, "page_count": 50}
]

for book in books:
    result = classify_book(book['page_count'])
    print(f"{book['title']}: {result}")