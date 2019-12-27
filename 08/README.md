# Задание 8: БПФ

Требуется написать программу, которая по вектору коэффициентов многочлена a_0 + a_1 x + … + a_{n-1} x^{n-1}a 
0
​	
 +a 
1
​	
 x+…+a 
n−1
​	
 x 
n−1
  вычисляет вектор значений этого многочлена в точках \omega_0,…,\omega_{n-1}ω 
0
​	
 ,…,ω 
n−1
​	
  — комплексных корнях степени nn из единицы. Корень \omega_kω 
k
​	
  равен \cos(2\pi k/n) + i \sin(2\pi k/n)cos(2πk/n)+isin(2πk/n). Гарантируется, что nn — степень двойки. Программа должна работать за время O(n \log n)O(nlogn). Входные данные: через пробел перечислены коэффициенты многочлена (действительные числа). Программа должна выдавать значения многочлена, разделяя их пробелами и выдавая через запятую действительную и мнимую часть числа. Ниже приведён алгоритм (Python 3.6), решающий поставленную задачу за время O(n^2)O(n 
2
 ):
<pre><code>
from math import pi, sin, cos


def polynomial(coeffs, x):
    return sum(a * x ** k for k, a in enumerate(coeffs))


coeffs = list(map(float, input().strip().split()))

n = len(coeffs)

result = [
    polynomial(coeffs, cos(2 * pi * k / n) + 1j * sin(2 * pi * k / n))
    for k in range(n)
]

print(' '.join(f'{x.real},{x.imag}' for x in result))
</code></pre>