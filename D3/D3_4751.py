
T = int(input())

for test_case in range(T):
    inp = str(input())

    print('..#.' * len(inp),end='')
    print('.')
    print('.#.#' * len(inp),end='')
    print('.')
    for i in range(len(inp)):
        print('#.{}.'.format(inp[i]),end='')
    print('#',end='')
    print()
    print('.#.#' * len(inp), end='')
    print('.')
    print('..#.' * len(inp), end= '')
    print('.')