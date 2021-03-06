# Задание 3: алгоритм Штрассена + быстрое возведение в степень
Требуется написать программу, возводящую матрицу размера A\in\mathbb{Z}_9^{n\times n}A∈Z 
9
n×n
​	
  в степень nn. Число nn может не быть степенью двойки. Для умножения матриц нужно использовать алгоритм Штрассена со сложностью O(n^{\log_27})O(n 
log 
2
​	
 7
 ), а для возведения в степень — алгоритм, требующий O(\log n)O(logn) матричных умножений. Вся арифметика производится над \mathbb{Z}_9Z 
9
​	
 , то есть, например 5+6=25+6=2, 3\cdot 7=33⋅7=3, 4-8=54−8=5 и т.п.. Ответом должна быть матрица, все элементы которой находятся в диапазоне \{0,\,1,\,\dots,\,8\}{0,1,…,8}. На вход (из стандартного потока ввода) подаётся квадратная матрица AA, строка матрицы соответствует строке входа, элементы внутри строки разделяются пробелами. Пример входа:

2 0 1\
4 2 7\
3 5 5

В стандартный поток вывода программа должна выводить в таком же формате матрицу A^nA 
n
### Пример вывода:

1 0 5\
2 1 8\
6 7 7
### Sample Input 1:

2 0 1\
4 2 7\
3 5 5
### Sample Output 1:

1 0 5\
2 1 8\
6 7 7