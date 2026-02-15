"""
DocString
E escrever o que eu
quiser


asdfasdfd
"""

''' Usar para escrever suas notas '''

# Permite escrever um comentário
print(123)  # Na frente
# Abaixo
print(456)


import sys
print(sys.builtin_module_names)

module_names = ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_interpchannels', '_interpqueues', '_interpreters', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha2', '_sha3', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_suggestions', '_symtable', '_sysconfig', '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref', '_winapi', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib')

print()

lista = [modulo.replace('_', '').upper() 
         for modulo in module_names 
         if 'nt' in modulo]
print(lista)
