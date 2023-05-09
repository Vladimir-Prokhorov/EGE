'''
    heap: текущее состояние кучи
    moves: текущий ход
    to: номер хода игрока, которого мы исследуем (Петя: 1, 3, 5; Ваня: 2, 4, 6)
'''
def game(heap, moves, to):
    if heap >= 106:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    res = [game(heap + 1, moves + 1, to),
           game(heap * 2, moves + 1, to)]
    # any(<массив лог. значений>) - функция, возвращает true,
    # если хотя бы одно значение в массиве истинно
    return any(res)


def game2(heap, moves, to):
    if heap >= 106:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    res = [game2(heap + 1, moves + 1, to),
           game2(heap * 2, moves + 1, to)]
    # all(<массив лог. значений>) - функция, возвращает true, если все значения истинны
    return any(res) if (moves + 1) % 2 == to % 2 else all(res)


print(f'19: {min(s for s in range(1, 106) if game(s, 0, 2) and not game(s, 0, 1))}')
print(f'20: {[s for s in range(1, 106) if not game2(s, 0, 1) and game2(s, 0, 3)]}')
print(f'21: {[s for s in range(1, 106) if not game2(s, 0, 2) and game2(s, 0, 4)]}')
