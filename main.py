# Функція
def f(x, y):
    return 4*(x - y) - x**2 - y**2

# Градієнт
def grad_f(x, y):
    dfdx = 4 - 2*x
    dfdy = -4 - 2*y
    return dfdx, dfdy

# Початкові дані
alpha = 0.5
x, y = 3.0, 3.0
eps = 0.01
max_iter = 100

print("k\t x\t\t y\t\t f(x,y)")
print("-"*50)

for k in range(max_iter):
    value = f(x, y)
    print(f"{k}\t {x:.4f}\t {y:.4f}\t {value:.4f}")
    
    # критерій зупинки
    if abs(x - 2) < eps and abs(y + 2) < eps:
        break
    
    # градієнт
    gx, gy = grad_f(x, y)
    
    # крок градієнтного підйому
    x = x + alpha * gx
    y = y + alpha * gy

print("\nЗбіжність досягнута на ітерації:", k)
print(f"Точка максимуму: x = {x:.4f}, y = {y:.4f}")
print(f"Максимальне значення функції: f = {f(x,y):.4f}")
