
xa = float(input('podaj x punku A:'))
ya = float(input('podaj x punku B:'))
xb = float(input('podaj x punku B:'))
yb = float(input('podaj x punku B:'))
xc = float(input('podaj x punku C:'))
yc = float(input('podaj x punku C:'))

area = 0.5 * (xb-xa) * (yc-ya) - (yb-ya) * (xc - xa)
print(f'Pole trojkata wynosi {area:.2f}')
