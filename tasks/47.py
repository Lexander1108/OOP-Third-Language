a = int(input('Enter first side: \t'))
b = int(input('Enter second side: \t'))
c = int(input('Enter third side: \t'))
def check (i1, i2, i3):
    if (i1 + i2) > i3 and (i1 + i3) > i2 and (i2 + i3) > i1:
        print('Triangle exist!\n')
        mx = max(i1, i2, i3)
        mn = min(i1, i2, i3)
        md = (i1 + i2 + i3) - (mx + mn)
        if mx**2 < md**2 + mn**2:
            print('Triangle is acute-angled!')
        else:
            print('Triangle isn`t acute-angled!')
    else:
        print('Triangle doesn`t exist!')
check(a, b, c)

