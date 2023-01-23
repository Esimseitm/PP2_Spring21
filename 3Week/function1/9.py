radius = float(input())

def volume(R):
    volume = (4/3) * 3.14 * R * R * R
    print(f'{volume:.1f}')
volume(radius)
