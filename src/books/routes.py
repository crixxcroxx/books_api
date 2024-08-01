from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.books_data import books
from src.books.models import Book


book_router = APIRouter()

@book_router.get('/', response_model=list[Book])
async def get_all_books():
    return books


@book_router.get('/{book_id}')
async def get_book_by_id(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")


@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book: Book) -> dict:
    new_book = book.model_dump()
    books.append(new_book)
    return new_book


# @book_router.patch('/{book_id}')
# async def update_book(book_id: int, update_data: BookUpdate) -> dict:
#     for book in books:
#         if book['id'] == book_id:
#             book['title'] = update_data.title
#             book['author'] = update_data.author
#             book['publisher'] = update_data.publisher
#             book['published_date'] = update_data.published_date
#             book['language'] = update_data.language

#             return book
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")


@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found!")