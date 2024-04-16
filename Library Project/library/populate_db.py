from books import *

def populate_database():
    # Vytvorenie autorov
    for i in range(1, 11):
        Author.objects.create(first_name=f'Author{i}_first', last_name=f'Author{i}_last')

    # Vytvorenie kategórií
    for i in range(1, 11):
        Category.objects.create(name=f'Category{i}', description=f'Description for Category{i}')

    # Vytvorenie kníh
    authors = Author.objects.all()
    categories = Category.objects.all()
    for i in range(1, 11):
        book = Book.objects.create(
            name=f'Book{i}',
            description=f'Description for Book{i}',
            on_stock=True if i % 2 == 0 else False
        )
        # Priradenie náhodného autora a kategórie k knihe
        book.author.add(authors[i - 1])
        book.category.add(categories[i - 1])

populate_database()