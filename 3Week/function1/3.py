numheads, numlegs = map(int, input().split())
def math(head, leg):
    y = (leg - (head*2))//2
    x = head - y
    print(f'{"rabbits"} - {y}')
    print(f'{"chikens"} - {x}')
math(numheads, numlegs)