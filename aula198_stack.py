# # Para Type annotation
# from typing import List

# # Pilha de livros com type annotation
# stack_of_books: List[str] = []  # {1}

# # Adicionando livros no topo da pilha
# stack_of_books.append('Livro 1')  # {2}
# stack_of_books.append('Livro 2')  # {2}
# stack_of_books.append('Livro 3')  # {2}

# try:
#     # Obtendo o elemento mais novo
#     book_1 = stack_of_books.pop()  # Livro 3 {3}
#     print(book_1)  # Livro 3

#     book_2 = stack_of_books.pop()  # Livro 2 {3}
#     print(book_2)  # Livro 2

#     book_3 = stack_of_books.pop()  # Livro 1 {3}
#     print(book_3)  # Livro 1

#     # IndexError: pop from empty list
#     book = stack_of_books.pop()  # Não há mais livros {4}
#     print(book)  # Seu código não chegará aqui
# except IndexError:
#     print('Trate o erro como preferir aqui.')
    
# # Para Type annotation
# from typing import List

# # Pilha de livros com type annotation
# stack_of_books: List[str] = []  # {1}

# # Adicionando livros no topo da pilha
# stack_of_books.append('Livro 1')  # {2}
# stack_of_books.append('Livro 2')  # {2}
# stack_of_books.append('Livro 3')  # {2}

# # Laço for
# for book in stack_of_books[::-1]:
#     # Faça o que preferir com o Livro
#     print(book)

# """
# Saída:
# Livro 3
# Livro 2
# Livro 1
# """

# # Para Type annotation
# from typing import List

# # Pilha de livros com type annotation
# stack_of_books: List[str] = []  # {1}

# # Adicionando livros no topo da pilha
# stack_of_books.append('Livro 1')  # {2}
# stack_of_books.append('Livro 2')  # {2}
# stack_of_books.append('Livro 3')  # {2}

# # Laço while
# while stack_of_books:
#     book = stack_of_books.pop()
#     print(book)

# """
# Saída:
# Livro 3
# Livro 2
# Livro 1
# """

# # Para Type annotation
# from typing import List

# # Pilha de livros com type annotation
# stack_of_books: List[str] = []  # {1}

# # Adicionando livros no topo da pilha
# stack_of_books.append('Livro 1')  # {2}
# stack_of_books.append('Livro 2')  # {2}
# stack_of_books.append('Livro 3')  # {2}

# # A cópia (shallow copy)
# stack_of_books_copy = stack_of_books.copy()

# # Agora não estou mais alterando os dados
# # da pilha original.
# while stack_of_books_copy:
#     print(stack_of_books_copy.pop())

# # A original continua intacta
# print(stack_of_books)  # ['Livro 1', 'Livro 2', 'Livro 3']

# # Para Type annotation
# from typing import List
# from copy import deepcopy

# # Pilha de listas
# stack_of_lists: List[List[str]] = []

# # Adicionando elementos
# stack_of_lists.append(['A', 'B'])
# stack_of_lists.append(['C', 'D'])
# stack_of_lists.append(['E', 'F'])

# # Shallow copy
# stack_of_lists_clone = deepcopy(stack_of_lists)

# # Obtendo o elemento do topo da pilha
# # Isso não altera a lista original
# item = stack_of_lists_clone.pop()

# # Mas isso sim
# item[0] = 'ALTERANDO O DADO'

# # Veja o resultado na lista original
# print(stack_of_lists)

# """
# Saída:
# [['A', 'B'], ['C', 'D'], ['ALTERANDO O DADO', 'F']]
# """

from typing import List, Any
from copy import deepcopy

from aula207_ola_django.blog import data


class Stack:
    """Uma classe representando uma pilha"""

    def __init__(self) -> None:
        # Essa stack é genérica, por isso
        # a lista poderá receber qualquer
        # tipo de dados
        self.__data: List[Any] = []

        # Representa o índice para iterações
        # com for

    def append(self, item: Any) -> None:
        """Representa o append da lista"""
        self.__data.append(item)

    def pop(self) -> Any:
        """Representa o pop da lista sem parâmetros"""
        if not self.__data:
            return

        return self.__data.pop()

    def peek(self) -> Any:
        """Mostra o último elemento adicionado à pilha"""
        if not self.__data:
            return

        return self.__data[-1]

    def __repr__(self) -> str:
        """Representação dos dados"""
        return f'{self.__class__.__name__}({self.__data})'

    def __iter__(self):
        self.__index = 0
        return self
    def __next__(self):
            #1                    #3
        if self.__index+1 >= len(self.__data):
            raise Exception('erro')
        
        item = self.__data[self.__index]
        self.__index += 1
        return item

    def __bool__(self):
        """Para iteração com while"""
        return bool(self.__data)


if __name__ == "__main__":
    stack = Stack()

    stack.append('A')
    stack.append('B')
    stack.append('C')
    
    print(stack)

    print('FOR:')
    for item in stack:
        print(item)

    # print('POP:')
    # last_item = stack.pop()
    # print(stack, last_item)
    # print()

    # print('WHILE:')
    # stack_copy = deepcopy(stack)
    # while stack_copy:
    #     print(stack_copy.pop())
    # print()

    # print('ORIGINAL STACK:')
    # print(stack)