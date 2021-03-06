# Задание 2: Универсальный многополюсник

Схема — это ациклический орграф, в котором каждая вершина является либо входом, либо функциональным элементом; некоторые вершины также могут дополнительно быть помечены как выходные. Схему нужно вывести в стандартный поток вывода в виде последовательности строк, каждая из которых имеет либо вид

GATE <номер вершины> <AND|OR|NOT> <номера вершин, выходы которых поданы на элемент>
или

OUTPUT <порядковый номер выхода> <номера вершины граф схемы, с которой снимается выходное значение>
Вершины нумеруются, начиная с нулевой. Если схема реализует функцию (или набор функций) от nn переменных, то вершины с наименьшими nn номерами (которым не должны быть приписаны функциональные элементы) считаются входами. Номера вершин схемы должны образовывать непрерывный интервал натуральных чисел. Выходы схемы имеют порядковые номера, начинающиеся с нулевого и также образующие непрерывный интервал натуральных чисел.

Пример описания схемы, имеющей два входа и один выход, в котором реализуется операция XOR от двух переменных (функция XOR реализована в вершине с номером 5):

GATE 2 AND 0 1\
GATE 3 OR 0 1\
GATE 4 NOT 2\
GATE 5 AND 3 4\
OUTPUT 0 5

# Описание задания
На лекции для построения схемы логарифмической глубины для умножения чисел в двоичной записи мы использовали «3-2-трюк»: быстрое построение по тройке чисел пары чисел, такой, что сумма пары равняется сумме тройки. Вам предлагается реализовать схему, которая осуществляет указанное преобразование. На входе схемы 3n3n битовых значений (в схеме они имеют номера соответственно от 00 до 3n-13n−1), в таком порядке: a_0,\,\dots,\,a_{n-1}a 
0
​	
 ,…,a 
n−1
​	
 , b_0,\,\dots,\,b_{n-1}b 
0
​	
 ,…,b 
n−1
​	
 , c_0,\,\dots,\,c_{n-1}c 
0
​	
 ,…,c 
n−1
​	
 . Эти значения кодируют соответственно числа A,\,B,\,CA,B,C; при этом a_0,\,b_0,\,c_0a 
0
​	
 ,b 
0
​	
 ,c 
0
​	
  — это самые младшие разряды двоичных записей, а a_{n-1},\,b_{n-1},\,c_{n-1}a 
n−1
​	
 ,b 
n−1
​	
 ,c 
n−1
​	
  — самые старшие. В схеме ровно 2\cdot(n+1)2⋅(n+1) вершин должны быть помечены как выходные и соответствовать битовым записям x_0,\,\dots,\,x_nx 
0
​	
 ,…,x 
n
​	
  и y_0,\,\dots,\,y_ny 
0
​	
 ,…,y 
n
​	
  (именно в таком порядке, т.е., например, выходу схемы с порядковым номером n+2n+2 соответствует бит y_1y 
1
​	
 ) чисел XX и YY, таких, что X+Y=A+B+CX+Y=A+B+C. В качестве функциональных элементов допускается использовать: отрицание (NOT), двухвходовую конъюнкцию (AND), двухвходовую дизъюнкцию (OR).

# Ограничения на размер и глубину
Размер схемы (общее число невходных вершин) должен быть не больше 20\cdot (n+1)20⋅(n+1), а глубина (максимум количества функциональных элементов на пути от входной до выходной вершины) не больше 1010. (ВНИМАНИЕ! Загляните также на следующий шаг, там задание отличается только ограничениями на размер/глубину схемы. Если сразу представляете, как делать, сдавайте одну и ту же программу на следующем и на текущем шаге.)

Формат выходных данных такой же, как и в примере для XOR. Входные данные — единственное число n,\,1\le n\le 1000n,1≤n≤1000.