import time

def counter():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 2
    yield 2

gen = counter()
print('До вибуху залишилось', next(gen), 'секунд...')
time.sleep(1)
print(next(gen), 'секунди...')
time.sleep(1)
print(next(gen), 'секунди...')
time.sleep(1)
print(next(gen), 'з половиною секунди...')
time.sleep(1)
print(next(gen), 'з четвертиною секунди...')
time.sleep(1)
print(next(gen), 'з волосиною...')
time.sleep(1)

print("""
██████╗░░█████╗░░█████╗░███╗░░░███╗██╗
██╔══██╗██╔══██╗██╔══██╗████╗░████║██║
██████╦╝██║░░██║██║░░██║██╔████╔██║██║
██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║╚═╝
██████╦╝╚█████╔╝╚█████╔╝██║░╚═╝░██║██╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
""")
