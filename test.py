# def deco(func):
#     def wrapper(*args, **kwargs):
#         print('--start--')
#         func(*args, **kwargs)
#         print('---end---')
#     return wrapper

# @deco
# def test():
#     print('Hello, Decorator')

# test()


# def deco2(func):
#     import os

#     def wrapper(*args, **kwargs):
#         res = '--start--' + os.linesep
#         res += func(*args, **kwargs) + '!' + os.linesep
#         res += '---end---'
#         return res
#     return wrapper


# @deco2
# def test2():
#     return('Hello, Decorator')


# print(test2())

# def deco_html(func):
#     def wrapper(*args, **kwargs):
#         res = '<html>'
#         res = res+func(*args, **kwargs)
#         res = res+'</html>'
#         return res
#     return wrapper


# def deco_body(func):
#     def wrapper(*args, **kwargs):
#         res = '<body>' + func(*args, **kwargs) + '</body>'
#         return res
#     return wrapper


# @deco_html
# @deco_body
# def test():
#     return 'Hello, Decorator'


# print(test())


# def deco_p(func):
#     def wrapper(*args, **kwargs):
#         res = '<p>'
#         res = res + func(args[0], **kwargs)
#         res = res + '</p>'
#         return res
#     return wrapper


# @deco_p
# def test(str):
#     return(str)


# print(test('Hello, Decorator'))


# def deco_tag(tag):
#     def _deco_tag(func):
#         def wrapper(*args, **kwargs):
#             res = '<' + tag + '>' + func(*args, **kwargs) + '</' + tag + '>'
#             return res
#         return wrapper
#     return _deco_tag


# @deco_tag('html')
# @deco_tag('body')
# def test():
#     return 'Hello World'


# print(test())


def twice(func):
    def wrapper(*args, **kwargs):
        return(func(*args, *kwargs)) * 2
    return wrapper


@twice
def add(x, y):
    return x + y


print(add(1, 3))
