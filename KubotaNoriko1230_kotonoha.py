
# "Hello World"を出力する
print("Hello World")
# 入力された文字列の整数値をxとする
x = int(input())
# xの3乗を出力する
print(x**3)
# 入力された文字列の整数値をnとする
n = int(input())
# nに32を掛けた値を出力する
print(n * 32)
# 入力された文字列の整数値をxとする
x = int(input())
# {{({{xから30を引いた値}})の組を2で割った値}}の整数値を出力する
print(int((x-30) / 2))
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# {{aにbを加えた値}}にcを加えた値を出力する
print(a+b+c)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aにbを掛けた値と({{aにbを加えた値}})の組に2を掛けた値を出力する
print(a*b, (a+b)*2)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aがbより大きいとき、
if a > b  :
  # "a > b"を出力する
  print("a > b")
# ('aがbより小さい',)
elif a < b  :
  # "a < b"を出力する
  print("a < b")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"a == b"']]]]]]
Syntax Error ((unknown source):7:-1+86)
else :
      
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b = map(int, input().split())
# {{({{aにbを加えた値}})の組を2で割った値}}の整数値を出力する
print(int((a+b)/2))
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b = map(int, input().split())
# bがaより大きいとき、
if b > a  :
  # aとbを入れ替える
  a, b = b, a
# aからbを引いた値を出力する
print(a - b)
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# cが1のとき、
if c == 1  :
  # "Open"を出力する
  print("Open")
# ('aが1、かつbが1の',)
elif a == 1 and b == 1  :
  # "Open"を出力する
  print("Open")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"Close"']]]]]]
# 入力された文字列の整数値をtimeとする
time = int(input())
# timeを3600で割った商をHとする
H = time//3600
# timeを3600で割った余りをMとする
M = time%3600
# Mを60で割った余りをSとする
S = M%60
# Mを60で割った商をMとする
M = M//60
# H、M、S、((sep, ":"))からなる辞書を出力する
print(H, M, S, sep=":")
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# aをbで割った値の整数値をdとする
d = int(a / b)
# aをbで割った余りをeとする
e = a % b
# aをbで割った値をfとする
f = a / b
# format(d,e,f)を出力する
print("{0} {1} {2:.5f}".format(d, e, f))
# 3.141592653589をpiとする
pi = 3.141592653589
# 入力された文字列の浮動小数点数値をrとする
r = float(input())
# rにrを掛けた値にpiを掛けた値をaとする
a = r * r * pi
# rに2を掛けた値にpiを掛けた値をbとする
b = r * 2 * pi
# テンプレートaをbでフォーマットした文字列を出力する
print("{0:.5f} {1:.5f}".format(a, b))
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# {{aにbを掛けた値}}を3.305785で割った値を出力する
print(a * b / 3.305785)
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b,c  = map(int, input().split())
# aがbより大きいとき、
if a > b  :
  # aとbを入れ替える
  a, b = b, a
# bがcより大きいとき、
if b > c  :
  # bとcを入れ替える
  b, c = c, b
# aがbより大きいとき、
if a > b  :
  # aとbを入れ替える
  a, b = b, a
# a、b、cを出力する
print(a, b, c)
Syntax Error ((unknown source):7:-1+124)
else :
      
# map(整数,入力された文字列を空白で分割した列)を展開し順にe1、e2、e3、e4とする
e1, e2, e3, e4  = map(int, input().split())
# {{e1がe2}}、かつ{{e3がe4かどうか}}、または{{e1がe3}}、かつ{{e2がe4かどうか}}、または{{e1がe4}}、かつ{{e2がe3かどうか}}のとき、
if e1 == e2 and e3 == e4 or e1 == e3 and e2 == e4 or e1 == e4 and e2 == e3  :
  # "yes"を出力する
  print("yes")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"no"']]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にN、A、B、C、Dとする
N, A, B, C, D  = map(int, input().split())[#Document [# '# setX']]
# NをAで割った余りが0のとき、
if N % A == 0  :
  # NをAで割った商にBを掛けた値をXとする
  X = N // A * B
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'X']expr: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Name 'N']name: [#Name '//']right: [#Name 'A']]name: [#Name '+']right: [#Int '1']]]name: [#Name '*']right: [#Name 'B']]]]][#Document [# '# setY']]
# NをCで割った余りが0のとき、
if N % C == 0  :
  # NをCで割った商にDを掛けた値をYとする
  Y = N // C * D
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'Y']expr: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Name 'N']name: [#Name '//']right: [#Name 'C']]name: [#Name '+']right: [#Int '1']]]name: [#Name '*']right: [#Name 'D']]]]]
# XとYの最小値を出力する
print(min(X, Y))
# map(整数,入力された文字列を空白で分割した列)を展開し順にA、B、Cとする
A, B, C  = map(int, input().split())
# 0をcoinとする
coin = 0
# 1をdayとする
day = 1
# coinがCより小さい間、繰り返す
while coin < C  :
  # ([[#Name 'coin'], [#Name 'A']],)
  [[#Name 'coin'], [#Name 'A']]
  # dayを7で割った余りが0のとき、
  if day % 7 == 0  :
    # ([[#Name 'coin'], [#Name 'B']],)
    [[#Name 'coin'], [#Name 'B']]
  # ([[#Name 'day'], [#Int '1']],)
  [[#Name 'day'], [#Int '1']]
# dayから1を引いた値を出力する
print(day-1)
# 1000をnとする
n = 1000
# 0をiとする
i = 0
# iがnより小さい間、繰り返す
while i < n  :
  # "Hello World"を出力する
  print("Hello World")
  # iに1を加えた値をiとする
  i = i + 1
# 関数changeを[#FuncParam [#ParamDecl name: [#Name 't']]]のパラメータを持つように定義する
def change (t)  :
  # tが1のとき、
  if t == 1  :
    # 6000を関数出力とする
    return 6000
  # ('tが2の',)
  elif t == 2  :
    # 4000を関数出力とする
    return 4000
  # ('tが3の',)
  elif t == 3  :
    # 3000を関数出力とする
    return 3000
  # ('tが4の',)
  elif t == 4  :
    # 2000を関数出力とする
    return 2000
# map(整数,入力された文字列を空白で分割した列)を展開し順にt1とn1とする
t1, n1  = map(int, input().split())
# map(整数,入力された文字列を空白で分割した列)を展開し順にt2とn2とする
t2, n2  = map(int, input().split())
# map(整数,入力された文字列を空白で分割した列)を展開し順にt3とn3とする
t3, n3  = map(int, input().split())
# map(整数,入力された文字列を空白で分割した列)を展開し順にt4とn4とする
t4, n4  = map(int, input().split())
# change(t1)にn1を掛けた値を出力する
print(change(t1) * n1)
# change(t2)にn2を掛けた値を出力する
print(change(t2) * n2)
# change(t3)にn3を掛けた値を出力する
print(change(t3) * n3)
# change(t4)にn4を掛けた値を出力する
print(change(t4) * n4)
# '0から7未満までの数列の各要素を順にiとして、繰り返す
for i  in range(7)  :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にhiとlowとする
  hi, low  = map(int, input().split())
  # hiからlowを引いた値を出力する
  print(hi - low)
# '0から9未満までの数列の各要素を順にiとして、繰り返す
for i  in range(9)  :
  # 入力された文字列を空白で分割した列を展開し順にname、a、bとする
  name, a, b  = input().split()
  # name、aの整数値にbの整数値を加えた値、{{200にaの整数値を掛けた値}}に{{300にbの整数値を掛けた値}}を加えた値を出力する
  print(name, int(a)+int(b), 200*int(a)+300*int(b))
# 0をsumとする
sum = 0
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
  # ([[#Name 'sum'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]],)
  [[#Name 'sum'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]
# sumを出力する
print(sum)
# 1をiとする
i = 1
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をxとする
  x = int(input())
  # xが0のとき、
  if x == 0  :
    # 繰り返すのを中断する
    break[#Document [# 'print(f"Case {i}: {x}")']]
  # "Case "、i、": "、x、((sep, ""))からなる辞書を出力する
  print("Case ", i, ": ", x, sep="")
  # iに1を加えた値をiとする
  i = i + 1
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a, b  = map(int, input().split())
  # aが0、かつbが0のとき、
  if a == 0 and b == 0  :
    # 繰り返すのを中断する
    break
  # aがbより大きいとき、
  if a > b  :
    # aとbを入れ替える
    a, b = b, a
  # aとbを出力する
  print(a, b)
# 入力された文字列の整数値をNとする
N = int(input())
# '0からN未満までの数列の各要素を順にiとして、繰り返す
for i  in range(N)  :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
  a, b, c  = map(int, input().split())
  # {{aの2乗が{{bの2乗にcの2乗を加えた値}}}}、または{{bの2乗が{{cの2乗にaの2乗を加えた値}}かどうか}}、またはcの2乗が{{aの2乗にbの2乗を加えた値}}のとき、
  if a**2 == b**2 + c**2 or b**2 == c**2 + a**2 or c**2 == a**2 + b**2  :
    # "YES"を出力する
    print("YES")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"NO"']]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 100000をSとする
S = 100000
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # ([[#Name 'S'], [#Double '1.05']],)
  [[#Name 'S'], [#Double '1.05']]
  # Sを1000で割った余りが0と等しくないとき、
  if S % 1000 != 0  :
    # ({{{{Sを1000で割った値}}の整数値に1を加えた値}})の組に1000を掛けた値をSとする
    S = (int(S / 1000) + 1) * 1000
# Sを出力する
print(S)
Syntax Error ((unknown source):9:-1+100)
else :
      
# '1から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1, 10)  :
  # '1から10未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(1, 10)  :
    # i、"x"、j、"="、iにjを掛けた値、((sep, ""))からなる辞書を出力する
    print(i, "x", j, "=", i*j, sep="")
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にHとWとする
  H, W  = map(int, input().split())
  # Hが0、かつWが0のとき、
  if H == 0 and W == 0  :
    # 繰り返すのを中断する
    break
  # '0からH未満までの数列の各要素を順にhとして、繰り返す
  for h  in range(H)  :
    # '0からW未満までの数列の各要素を順にwとして、繰り返す
    for w  in range(W)  :
      # ({{hにwを加えた値}})の組を2で割った余りが0のとき、
      if (h + w) % 2 == 0  :
        # "#"と((end, ""))からなる辞書を出力する
        print("#", end="")
      # ()
      else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"."'][#Data [#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]
    # 空行を出力する
    print()
  # 空行を出力する
  print()
# 真の間、繰り返す
while True :
  # 入力された文字列を空白で分割した列を展開し順にa、op、bとする
  a, op, b  = input().split()
  # aの整数値をaとする
  a = int(a)
  # bの整数値をbとする
  b = int(b)
  # opが"?"のとき、
  if op == "?"  :
    # 繰り返すのを中断する
    break
  # ('opが"+"の',)
  elif op == "+"  :
    # aにbを加えた値を出力する
    print(a + b)
  # ('opが"-"の',)
  elif op == "-"  :
    # aからbを引いた値を出力する
    print(a - b)
  # ('opが"/"の',)
  elif op == "/"  :
    # {{aをbで割った値}}の整数値を出力する
    print(int(a / b))
  # ('opが"*"の',)
  elif op == "*"  :
    # aにbを掛けた値を出力する
    print(a * b)
# 入力された文字列をnとする
n = input()
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlとする
l = list(map(int, input().split()))
# lの最小値、lの最大値、lの総和を出力する
print(min(l), max(l), sum(l))
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をNとする
  N = int(input())
  # Nが0のとき、
  if N == 0  :
    # 繰り返すのを中断する
    break
  # '{{'0からN未満までの数列}}の各要素をiとし、入力された文字列の整数値の列のリストをdataとする
  data = list(int(input()) for i in range(N))
  # data.sort()
  data.sort()
  # dataの最初値を削除する
  del data[0]
  # dataの末尾値を削除する
  del data[-1]
  # dataの総和をdataの長さで割った値をdata_aveとする
  data_ave = sum(data)/len(data)
  # data_aveの整数値を出力する
  print(int(data_ave))
[#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'lru_cache']]]
# 関数Fibを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def Fib (n)  :
  # nが0のとき、
  if n == 0  :
    # 1を関数出力とする
    return 1
  # ('nが1の',)
  elif n == 1  :
    # 1を関数出力とする
    return 1
  # ()
  else :[#Else [#Block [#Return expr: [#Infix left: [#ApplyExpr name: [#Name 'Fib']params: [#Arguments [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]]]name: [#Name '+']right: [#ApplyExpr name: [#Name 'Fib']params: [#Arguments [#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '2']]]]]]]]
# 入力された文字列の整数値をNとする
N = int(input())
# Fib(N)を出力する
print(Fib(N))
# mathモジュールを用いる
import math
# 関数Kochを[#FuncParam [#ParamDecl name: [#Name 'Px']][#ParamDecl name: [#Name 'Py']][#ParamDecl name: [#Name 'Qx']][#ParamDecl name: [#Name 'Qy']][#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def Koch (Px, Py, Qx, Qy, n)  :
  # nが0のとき、
  if n == 0  :
    # 関数処理を中断する
    return 
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'Ax']expr: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'Px']]name: [#Name '+']right: [#Name 'Qx']]]name: [#Name '/']right: [#Int '3']]][#VarDecl name: [#Name 'Ay']expr: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'Py']]name: [#Name '+']right: [#Name 'Qy']]]name: [#Name '/']right: [#Int '3']]][#VarDecl name: [#Name 'Bx']expr: [#Infix left: [#Tuple [#Infix left: [#Name 'Px']name: [#Name '+']right: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'Qx']]]]name: [#Name '/']right: [#Int '3']]][#VarDecl name: [#Name 'By']expr: [#Infix left: [#Tuple [#Infix left: [#Name 'Py']name: [#Name '+']right: [#Infix left: [#Int '2']name: [#Name '*']right: [#Name 'Qy']]]]name: [#Name '/']right: [#Int '3']]][#VarDecl name: [#Name 'Cx']expr: [#Infix left: [#Infix left: [#Name 'Ax']name: [#Name '+']right: [#Infix left: [#Tuple [#Infix left: [#Name 'Bx']name: [#Name '-']right: [#Name 'Ax']]]name: [#Name '*']right: [#MethodExpr recv: [#Name 'math']name: [#Name 'cos']params: [#Arguments [#Infix left: [#GetExpr recv: [#Name 'math']name: [#Name 'pi']]name: [#Name '/']right: [#Int '3']]]]]]name: [#Name '-']right: [#Infix left: [#Tuple [#Infix left: [#Name 'By']name: [#Name '-']right: [#Name 'Ay']]]name: [#Name '*']right: [#MethodExpr recv: [#Name 'math']name: [#Name 'sin']params: [#Arguments [#Infix left: [#GetExpr recv: [#Name 'math']name: [#Name 'pi']]name: [#Name '/']right: [#Int '3']]]]]]][#VarDecl name: [#Name 'Cy']expr: [#Infix left: [#Infix left: [#Name 'Ay']name: [#Name '+']right: [#Infix left: [#Tuple [#Infix left: [#Name 'Bx']name: [#Name '-']right: [#Name 'Ax']]]name: [#Name '*']right: [#MethodExpr recv: [#Name 'math']name: [#Name 'sin']params: [#Arguments [#Infix left: [#GetExpr recv: [#Name 'math']name: [#Name 'pi']]name: [#Name '/']right: [#Int '3']]]]]]name: [#Name '+']right: [#Infix left: [#Tuple [#Infix left: [#Name 'By']name: [#Name '-']right: [#Name 'Ay']]]name: [#Name '*']right: [#MethodExpr recv: [#Name 'math']name: [#Name 'cos']params: [#Arguments [#Infix left: [#GetExpr recv: [#Name 'math']name: [#Name 'pi']]name: [#Name '/']right: [#Int '3']]]]]]][#Expression [#ApplyExpr name: [#Name 'Koch']params: [#Arguments [#Name 'Px'][#Name 'Py'][#Name 'Ax'][#Name 'Ay'][#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'Ax'][#Name 'Ay']]]][#Expression [#ApplyExpr name: [#Name 'Koch']params: [#Arguments [#Name 'Ax'][#Name 'Ay'][#Name 'Cx'][#Name 'Cy'][#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'Cx'][#Name 'Cy']]]][#Expression [#ApplyExpr name: [#Name 'Koch']params: [#Arguments [#Name 'Cx'][#Name 'Cy'][#Name 'Bx'][#Name 'By'][#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'Bx'][#Name 'By']]]][#Expression [#ApplyExpr name: [#Name 'Koch']params: [#Arguments [#Name 'Bx'][#Name 'By'][#Name 'Qx'][#Name 'Qy'][#Infix left: [#Name 'n']name: [#Name '-']right: [#Int '1']]]]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 0と0.00000000を出力する
print(0, 0.00000000)
# Koch(0.00000000,0.00000000,100.00000000,0.00000000,n)
Koch(0.00000000, 0.00000000, 100.00000000, 0.00000000, n)
# 100.00000000と0.00000000を出力する
print(100.00000000, 0.00000000)
Syntax Error ((unknown source):4:8+73)
print(*a, sep=" ")
        ^         
# 0をsumとする
sum = 0
# '0から5未満までの数列の各要素を順にiとして、繰り返す
for i  in range(5)  :
  # 入力された文字列の整数値をscoreとする
  score = int(input())
  # scoreが40より小さいとき、
  if score < 40  :
    # 40をscoreとする
    score = 40
  # ([[#Name 'sum'], [#Name 'score']],)
  [[#Name 'sum'], [#Name 'score']]
# sumを5で割った商を出力する
print(sum//5)
# 空列をlist_aとする
list_a = []
# 空列をlist_bとする
list_b = []
# '0から4未満までの数列の各要素を順にxとして、繰り返す
for x  in range(4)  :
  # list_a.append(int(input()))
  list_a.append(int(input()))
# list_a.sort(reverse = True)
list_a.sort(reverse = True)
# '0から2未満までの数列の各要素を順にxとして、繰り返す
for x  in range(2)  :
  # list_b.append(int(input()))
  list_b.append(int(input()))
# list_b.sort(reverse = True)
list_b.sort(reverse = True)
# {{list_aの位置0から位置3までの部分}}の総和にlist_bの最初値を加えた値を出力する
print(sum(list_a[0:3]) + list_b[0])
# 空列をlist_Wとする
list_W = []
# 空列をlist_Kとする
list_K = []
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
  # list_W.append(int(input()))
  list_W.append(int(input()))
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
  # list_K.append(int(input()))
  list_K.append(int(input()))
# list_W.sort(reverse = True)
list_W.sort(reverse = True)
# list_K.sort(reverse = True)
list_K.sort(reverse = True)
# list_Wの位置0から位置3までの部分の総和をsum_Wとする
sum_W = sum(list_W[0:3])
# list_Kの位置0から位置3までの部分の総和をsum_Kとする
sum_K = sum(list_K[0:3])
# sum_Wとsum_Kを出力する
print(sum_W, sum_K)
# mathモジュールを用いる
import math
# 入力された文字列の整数値をNとする
N = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをAとする
A = list(map(int, input().split()))
# Aの最小値をmとする
m = min(A)
# Aの最大値をMとする
M = max(A)
# math.ceil((m + M) / 2) からmを引いた値を出力する
print(math.ceil((m + M) / 2) - m)
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
  n, m  = map(int, input().split())
  # mが0、かつnが0のとき、
  if m == 0 and n == 0  :
    # 繰り返すのを中断する
    break
  # 空列をListとする
  List = []
  # 0をmax_ansとする
  max_ans = 0
  # 0をsum_ansとする
  sum_ans = 0
  # '0からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n)  :
    # List.append(int(input()))
    List.append(int(input()))
    # iがmより小さいとき、
    if i < m  :
      # ([[#Name 'sum_ans'], [#IndexExpr recv: [#Name 'List']index: [#Name 'i']]],)
      [[#Name 'sum_ans'], [#IndexExpr recv: [#Name 'List']index: [#Name 'i']]]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'sum_ans']name: [# '+=']right: [#Infix left: [#IndexExpr recv: [#Name 'List']index: [#Name 'i']]name: [#Name '-']right: [#IndexExpr recv: [#Name 'List']index: [#Infix left: [#Name 'i']name: [#Name '-']right: [#Name 'm']]]]]]]
    # iが{{mから1を引いた値}}以上、かつmax_ansがsum_ansより小さいとき、
    if i >= m - 1 and max_ans < sum_ans  :
      # sum_ansをmax_ansとする
      max_ans = sum_ans
  # max_ansを出力する
  print(max_ans)
# 空列をLISTとする
LIST = []
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10)  :
  # LIST.append(int(input()))
  LIST.append(int(input()))
# LIST.sort(reverse = True)
LIST.sort(reverse = True)
# LISTの最初値を出力する
print(LIST[0])
# LIST(1)を出力する
print(LIST[1])
# LIST(2)を出力する
print(LIST[2])
# 入力された文字列の文字列をstr_orgとする
str_org = str(input())
# str_orgを英大文字に変換した文字列を出力する
print(str_org.upper())
# 入力された文字列をstrとする
str = input()
# strの英大文字を英小文字、英小文字を英大文字に変換した文字列を出力する
print(str.swapcase())
# '{{'0から26未満までの数列}}の各要素をiとし、0の列のリストをcount_charとする
count_char = list(0 for i in range(26))
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'str_org']expr: [#ApplyExpr name: [#Name 'str']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]][#VarDecl name: [#Name 'str_org']expr: [#MethodExpr recv: [#Name 'str_org']name: [#Name 'lower']params: [#Arguments '']]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'str_org']]]]]body: [#Block [#VarDecl name: [#Name 'num_org']expr: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 'str_org']index: [#Name 'i']]]]][#If cond: [#And left: [#Infix left: [#Name 'num_org']name: [#Name '>']right: [#Int '96']]right: [#Infix left: [#Name 'num_org']name: [#Name '<']right: [#Int '123']]]then: [#Block [#SelfAssignment left: [#IndexExpr recv: [#Name 'count_char']index: [#Infix left: [#Name 'num_org']name: [#Name '-']right: [#Int '97']]]name: [# '+=']right: [#Int '1']]]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
# '97から123未満までの数列の各要素を順にiとして、繰り返す
for i  in range(97, 123)  :
  # 文字コードiの文字、":"、count_char({{iから97を引いた値}})を出力する
  print(chr(i), ":", count_char[i-97])
# 真の間、繰り返す
while True :
  # 入力された文字列をnumとする
  num = input()
  # numが'0'のとき、
  if num == '0'  :
    # 繰り返すのを中断する
    break
  # numの各要素をiとし、iの整数値の列をnum_lstとする
  num_lst = [int(i) for i in num]
  # num_lstの総和を出力する
  print(sum(num_lst))
# '入力された文字列のリストをaとする
a = list(input())
# a内の"K"の出現をカウントした整数をcount_Kとする
count_K = a.count("K")
# a内の"P"の出現をカウントした整数をcount_Pとする
count_P = a.count("P")
# a内の"U"の出現をカウントした整数をcount_Uとする
count_U = a.count("U")
# a内の"C"の出現をカウントした整数をcount_Cとする
count_C = a.count("C")
# count_K、count_P、count_U、count_Cの最小値を出力する
print(min(count_K, count_P, count_U, count_C))
# 入力された文字列をWとする
W = input()
# 0をnとする
n = 0
# 真の間、繰り返す
while True :
  # 入力された文字列をTとする
  T = input()
  # Tが"END_OF_TEXT"のとき、
  if T== "END_OF_TEXT"  :
    # 繰り返すのを中断する
    break
  # 'Tを空白で分割した列のリストをsmall_Tとする
  small_T = list(T.split())
  # '0からsmall_Tの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(small_T))  :
    # strとsmall_T(i)を英小文字に変換した文字列がstrとWを英小文字に変換した文字列のとき、
    if str.lower(small_T[i]) == str.lower(W)  :
      # ([[#Name 'n'], [#Int '1']],)
      [[#Name 'n'], [#Int '1']]
# nを出力する
print(n)
# '入力された文字列のリストをsとする
s = list(input())
# '入力された文字列のリストをpとする
p = list(input())
# '0からpの長さ未満までの数列の各要素を順にxとして、繰り返す
for x  in range(len(p))  :
  # s.append(s[x])
  s.append(s[x])
# 0をiとする
i = 0
# 0をjとする
j = 0
# 真の間、繰り返す
while True :
  # p(j)がs(i)のとき、
  if p[j] == s[i]  :
    # ([[#Name 'j'], [#Int '1']],)
    [[#Name 'j'], [#Int '1']]
    # jがpの長さのとき、
    if j == len(p)  :
      # "Yes"を出力する
      print("Yes")
      # 繰り返すのを中断する
      break
    # ([[#Name 'i'], [#Int '1']],)
    [[#Name 'i'], [#Int '1']]
    # iがsの長さのとき、
    if i == len(s)  :
      # "No"を出力する
      print("No")
      # 繰り返すのを中断する
      break
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'i']name: [# '+=']right: [#Tuple [#Infix left: [#Int '1']name: [#Name '-']right: [#Name 'j']]]][#If cond: [#Infix left: [#Name 'i']name: [#Name '==']right: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 's']]]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"No"']]]][#Break 'break']]][#VarDecl name: [#Name 'j']expr: [#Int '0']]]]
# '入力された文字列のリストをaとする
a = list(input())
# '入力された文字列のリストをbとする
b = list(input())
# '0から{{aの長さに1を加えた値}}からbの長さを引いた値未満までの数列の各要素を順にjとして、繰り返す
for j  in range(len(a)+1-len(b))  :
  # 真をSameとする
  Same = True
  # jをansとする
  ans = j
  # 0をiとする
  i = 0
  # iがbの長さより小さい間、繰り返す
  while i < len(b)  :
    # b(i)がa(j)のとき、
    if b[i] == a[j]  :
      # ([[#Name 'i'], [#Int '1']],)
      [[#Name 'i'], [#Int '1']]
      # ([[#Name 'j'], [#Int '1']],)
      [[#Name 'j'], [#Int '1']]
    # ()
    else :[#Else [#Block [#VarDecl name: [#Name 'Same']expr: [#False 'False']][#Break 'break']]]
  # Sameが真のとき、
  if Same == True  :
    # ansを出力する
    print(ans)
# 入力された文字列の整数値をnとする
n = int(input())
# 0をTaro_tenとする
Taro_ten = 0
# 0をHanako_tenとする
Hanako_ten = 0
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # '入力された文字列を空白で分割した列のリストを展開し順にaとbとする
  a, b  = list(input().split())
  # 'aのリストをTaroとする
  Taro = list(a)
  # 'bのリストをHanakoとする
  Hanako = list(b)
  # Taroの長さとHanakoの長さの最小値をlengthとする
  length = min(len(Taro), len(Hanako))
  # '0からlength未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(length)  :
    # Taro(i)の順序数がHanako(i)の順序数より大きいとき、
    if ord(Taro[i]) > ord(Hanako[i])  :
      # ([[#Name 'Taro_ten'], [#Int '3']],)
      [[#Name 'Taro_ten'], [#Int '3']]
      # 繰り返すのを中断する
      break
    # ('Taro(i)の順序数がHanako(i)の順序数より小さい',)
    elif ord(Taro[i]) < ord(Hanako[i])  :
      # ([[#Name 'Hanako_ten'], [#Int '3']],)
      [[#Name 'Hanako_ten'], [#Int '3']]
      # 繰り返すのを中断する
      break
    # iがlengthから1を引いた値のとき、
    if i == length -1  :
      # Taroの長さがlengthより大きいとき、
      if len(Taro) > length  :
        # ([[#Name 'Taro_ten'], [#Int '3']],)
        [[#Name 'Taro_ten'], [#Int '3']]
      # ('Hanakoの長さがlengthより大きい',)
      elif len(Hanako) > length  :
        # ([[#Name 'Hanako_ten'], [#Int '3']],)
        [[#Name 'Hanako_ten'], [#Int '3']]
      # ()
      else :[#Else [#Block [#SelfAssignment left: [#Name 'Taro_ten']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'Hanako_ten']name: [# '+=']right: [#Int '1']]]]
# Taro_tenとHanako_tenを出力する
print(Taro_ten, Hanako_ten)
# 真の間、繰り返す
while True :
  # 入力された文字列をscoreとする
  score = input()
  # scoreが"0"のとき、
  if score == "0"  :
    # 繰り返すのを中断する
    break
  # score内の"A"の出現をカウントした整数をscore_aとする
  score_a = score.count("A")
  # score内の"B"の出現をカウントした整数をscore_bとする
  score_b = score.count("B")
  # score(0)が"A"のとき、
  if score[0] == "A"  :
    # ([[#Name 'score_a'], [#Int '1']],)
    [[#Name 'score_a'], [#Int '1']]
  # ('score(0)が"B"の',)
  elif score[0] == "B"  :
    # ([[#Name 'score_b'], [#Int '1']],)
    [[#Name 'score_b'], [#Int '1']]
  # score_aがscore_bより大きいとき、
  if score_a > score_b  :
    # ([[#Name 'score_a'], [#Int '1']],)
    [[#Name 'score_a'], [#Int '1']]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'score_b']name: [# '+=']right: [#Int '1']]]]
  # score_aとscore_bを出力する
  print(score_a, score_b)
# mathモジュールを用いる
import math
# map(float,入力された文字列を空白で分割した列)を展開し順にx1、y1、x2、y2とする
x1, y1, x2, y2  = map(float, input().split())
# math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)をdistとする
dist = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
# format(dist)を出力する
print("{:.5f}".format(dist))
# mathモジュールを用いる
import math
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、Cとする
a, b, C  = map(int, input().split())
# {{aにbを掛けた値}}にmath.sin(math.pi * C / 180) を掛けた値を2で割った値をSとする
S = a * b * math.sin(math.pi * C / 180) / 2
# math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.pi * C / 180))をcとする
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.pi * C / 180))
# aにbを加えた値にcを加えた値をLとする
L = a + b + c
# 2にSを掛けた値をaで割った値をhとする
h = 2 * S / a
# format(S)を出力する
print('{:.4f}'.format(S))
# format(L)を出力する
print('{:.4f}'.format(L))
# format(h)を出力する
print('{:.4f}'.format(h))
# mathモジュールを用いる
import math
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをsとする
  s = list(map(int, input().split()))
  # sの総和をsの長さで割った値をmとする
  m = sum(s) / len(s)
  # 0をaとする
  a = 0
  # '0からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n)  :
    # ([[#Name 'a'], [#Infix left: [#Tuple [#Infix left: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name '-']right: [#Name 'm']]]name: [#Name '**']right: [#Int '2']]],)
    [[#Name 'a'], [#Infix left: [#Tuple [#Infix left: [#IndexExpr recv: [#Name 's']index: [#Name 'i']]name: [#Name '-']right: [#Name 'm']]]name: [#Name '**']right: [#Int '2']]]
  # ([[#Name 'a'], [#Name 'n']],)
  [[#Name 'a'], [#Name 'n']]
  # math.sqrt(a)をaとする
  a = math.sqrt(a)
  # aを出力する
  print(a)
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にm、f、rとする
  m, f, r  = map(int, input().split())
  # {{mが-1}}、かつ{{fが-1かどうか}}、かつrが-1のとき、
  if m == -1 and f == -1 and r == -1  :
    # 繰り返すのを中断する
    break
  # mが-1、またはfが-1のとき、
  if m == -1 or f == -1  :
    # "F"を出力する
    print("F")
  # ('({{mにfを加えた値}})の組が80以上の',)
  elif (m + f) >= 80  :
    # "A"を出力する
    print("A")
  # ('({{mにfを加えた値}})の組が65以上の',)
  elif (m + f) >= 65  :
    # "B"を出力する
    print("B")
  # ('({{mにfを加えた値}})の組が50以上の',)
  elif (m + f) >= 50  :
    # "C"を出力する
    print("C")
  # ('({{mにfを加えた値}})の組が30以上、かつrが50以上の',)
  elif (m + f) >= 30 and r >= 50  :
    # "C"を出力する
    print("C")
  # ('({{mにfを加えた値}})の組が30以上の',)
  elif (m + f) >= 30  :
    # "D"を出力する
    print("D")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"F"']]]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
  n, m  = map(int, input().split())
  # nが0、かつmが0のとき、
  if n == 0 and m == 0  :
    # 繰り返すのを中断する
    break
  # 0をcountとする
  count = 0
  # '1からnから1を引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(1, n-1)  :
    # 'iに1を加えた値からn未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(i+1, n)  :
      # 'jに1を加えた値からnに1を加えた値未満までの数列の各要素を順にkとして、繰り返す
      for k  in range(j+1, n+1)  :
        # {{iにjを加えた値}}にkを加えた値がmのとき、
        if i + j + k == m  :
          # ([[#Name 'count'], [#Int '1']],)
          [[#Name 'count'], [#Int '1']]
  # countを出力する
  print(count)
# 入力された文字列の整数値をnとする
n = int(input())
# {{'0から4未満までの数列}}の各要素をjとし、{{{{'0から13未満までの数列}}の各要素をiとし、偽の列}}の列をcardとする
card = [[False for i in range(13)] for j in range(4)]
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # 入力された文字列を空白で分割した列を展開し順にmarkとsuitとする
  mark, suit  = input().split()
  # markが"S"のとき、
  if mark == "S"  :
    # 0をmark_numとする
    mark_num = 0
  # ('markが"H"の',)
  elif mark == "H"  :
    # 1をmark_numとする
    mark_num = 1
  # ('markが"C"の',)
  elif mark == "C"  :
    # 2をmark_numとする
    mark_num = 2
  # ('markが"D"の',)
  elif mark == "D"  :
    # 3をmark_numとする
    mark_num = 3
  # 真をcard[mark_num][int(suit)-1] にする
  card[mark_num][int(suit)-1]  = True
# '0から4未満までの数列の各要素を順にjとして、繰り返す
for j  in range(4)  :
  # '0から13未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(13)  :
    # card(j)(i)が偽のとき、
    if card[j][i] == False  :
      # jが0のとき、
      if j == 0  :
        # "S"とiに1を加えた値を出力する
        print("S", i+1)
      # ('jが1の',)
      elif j == 1  :
        # "H"とiに1を加えた値を出力する
        print("H", i+1)
      # ('jが2の',)
      elif j == 2  :
        # "C"とiに1を加えた値を出力する
        print("C", i+1)
      # ('jが3の',)
      elif j == 3  :
        # "D"とiに1を加えた値を出力する
        print("D", i+1)
# map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
n, m  = map(int, input().split())
# {{'0からn未満までの数列}}の各要素をiとし、'map(整数,{{input()を空白で分割した列}})のリストの列をBとする
B = [list(map(int, input().split())) for i in range(n)]
# {{'0からm未満までの数列}}の各要素をiとし、入力された文字列の整数値の列をAとする
A = [int(input()) for i in range(m)]
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # 0をansとする
  ans = 0
  # '0からm未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(m)  :
    # ([[#Name 'ans'], [#Infix left: [#IndexExpr recv: [#Name 'A']index: [#Name 'j']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'B']index: [#Name 'i']]index: [#Name 'j']]]],)
    [[#Name 'ans'], [#Infix left: [#IndexExpr recv: [#Name 'A']index: [#Name 'j']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'B']index: [#Name 'i']]index: [#Name 'j']]]]
  # ansを出力する
  print(ans)    
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、m、lとする
n, m, l  = map(int, input().split())
# {{'0からn未満までの数列}}の各要素をiとし、'map(整数,{{input()を空白で分割した列}})のリストの列をAとする
A = [list(map(int, input().split())) for i in range(n)]
# {{'0からm未満までの数列}}の各要素をiとし、'map(整数,{{input()を空白で分割した列}})のリストの列をBとする
B = [list(map(int, input().split())) for i in range(m)]
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # '0からl未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(l)  :
    # 0をansとする
    ans = 0
    # '0からm未満までの数列の各要素を順にkとして、繰り返す
    for k  in range(m)  :
      # ([[#Name 'ans'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'i']]index: [#Name 'k']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'B']index: [#Name 'k']]index: [#Name 'j']]]],)
      [[#Name 'ans'], [#Infix left: [#IndexExpr recv: [#IndexExpr recv: [#Name 'A']index: [#Name 'i']]index: [#Name 'k']]name: [#Name '*']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'B']index: [#Name 'k']]index: [#Name 'j']]]]
    # jがlから1を引いた値のとき、
    if j == l-1  :
      # ansを出力する
      print(ans)
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'ans'][#Data [#KeyValue name: [#Name 'end']value: [#QString '" "']]]]]]]]
# 関数factorizationを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def factorization (n) :
  # 空列をLとする
  L = []
  # nをtempとする
  temp = n
  # nと((end, ""))からなる辞書を出力する
  print(n,end="")
  # ":"と((end, ""))からなる辞書を出力する
  print(":",end="")
  # '2から{{nの(1/2)乗を1で割った商}}の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2, int(n**(1/2)//1)+1) :
    # tempをiで割った余りが0のとき、
    if temp%i==0 :
      # 0をcとする
      c = 0
      # tempをiで割った余りが0の間、繰り返す
      while temp%i==0 :
        # ([[#Name 'c'], [#Int '1']],)
        [[#Name 'c'], [#Int '1']]
        # ([[#Name 'temp'], [#Name 'i']],)
        [[#Name 'temp'], [#Name 'i']]
      # L.append([i, c])
      L.append([i, c])
      # '0からc未満までの数列の各要素を順にjとして、繰り返す
      for j  in range(c) :
        # ""、i、((end, ""))からなる辞書を出力する
        print("",i,end="")
  # tempが1と等しくないとき、
  if temp!=1 :
    # ""、temp、((end, ""))からなる辞書を出力する
    print("",temp, end="")
  # 空行を出力する
  print()
# 入力された文字列の整数値をnとする
n = int(input()) 
# factorization(n)
factorization(n)
# 関数Sを[#FuncParam [#ParamDecl name: [#Name 'x']]]のパラメータを持つように定義する
def S (x)  :
  # 1000000007をmodとする
  mod = 1000000007
  # (xをmodで割った余り)の組を関数出力とする
  return (x % mod)
# 関数Aを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']][#ParamDecl name: [#Name 'mod']]]のパラメータを持つように定義する
def A (a, b, mod)  :
  # bが1のとき、
  if b == 1  :
    # aを関数出力とする
    return a
  # ('bを2で割った余りが0の',)
  elif b%2 == 0  :
    # S(aの2乗)をa_2とする
    a_2 = S(a**2)
    # bを2で割った商をb_2とする
    b_2 = b // 2
    # S(A(a_2,b_2,mod))を関数出力とする
    return S(A(a_2, b_2, mod))
  # ()
  else :[#Else [#Block [#VarDecl name: [#Name 'a_2']expr: [#ApplyExpr name: [#Name 'S']params: [#Arguments [#Infix left: [#Name 'a']name: [#Name '**']right: [#Int '2']]]]][#VarDecl name: [#Name 'b_2']expr: [#Infix left: [#Tuple [#Infix left: [#Name 'b']name: [#Name '-']right: [#Int '1']]]name: [#Name '//']right: [#Int '2']]][#Return expr: [#ApplyExpr name: [#Name 'S']params: [#Arguments [#Infix left: [#ApplyExpr name: [#Name 'A']params: [#Arguments [#Name 'a_2'][#Name 'b_2'][#Name 'mod']]]name: [#Name '*']right: [#Name 'a']]]]]]]
# 1000000007をmodとする
mod = 1000000007
# map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
m, n  = map(int, input().split())
# A(m,n,mod)を出力する
print(A(m, n, mod))
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にxとyとする
  x, y  = map(int, input().split())
  # xが0、かつyが0のとき、
  if x == 0 and y == 0  :
    # 繰り返すのを中断する
    break
  # 0をansとする
  ans = 0
  # 真の間、繰り返す
  while True :
    # yが0のとき、
    if y == 0  :
      # 繰り返すのを中断する
      break
    # xがyより小さいとき、
    if x < y  :
      # xとyを入れ替える
      x, y = y, x
    # xをyで割った余りをxとする
    x = x % y
    # xとyを入れ替える
    x, y = y, x
    # ([[#Name 'ans'], [#Int '1']],)
    [[#Name 'ans'], [#Int '1']]
  # xとansを出力する
  print(x, ans)
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a, b)  :
  # 真の間、繰り返す
  while True :
    # aがbより小さいとき、
    if a < b  :
      # aとbを入れ替える
      a, b = b, a
    # aをbで割った余りをamariとする
    amari = a % b
    # amariが0のとき、
    if amari == 0  :
      # 繰り返すのを中断する
      break
    # ()
    else :[#Else [#Block [#MultiAssignment left: [# [#Name 'a'][#Name 'b']]right: [#Tuple [#Name 'b'][#Name 'amari']]]]]
  # (b)の組を関数出力とする
  return (b)
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをcとする
c = list(map(int, input().split()))
# 'nから1を引いた値から0未満までの-1間隔の数列の各要素を順にiとして、繰り返す
for i  in range(n-1, 0, -1)  :
  # {{c(i)にc({{iから1を引いた値}})を掛けた値}}をgcd(c(i),c({{iから1を引いた値}}))で割った値の整数値をc[i-1] にする
  c[i-1]  = int(c[i] * c[i-1] / gcd(c[i], c[i-1]))
# cの最初値を出力する
print(c[0])
# map(整数,入力された文字列を空白で分割した列)を展開し順にNとMとする
N, M  = map(int, input().split())
# 真の間、繰り返す
while True :
  # NがMより小さいとき、
  if N < M  :
    # NとMを入れ替える
    N, M = M, N
  # NをMで割った余りをamariとする
  amari = N % M
  # amariが0のとき、
  if amari == 0  :
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#MultiAssignment left: [# [#Name 'N'][#Name 'M']]right: [#Tuple [#Name 'M'][#Name 'amari']]]]]
# Mを出力する
print(M)
# mathモジュールを用いる
import math
# 関数Sosuを[#FuncParam [#ParamDecl name: [#Name 'N']]]のパラメータを持つように定義する
def Sosu (N)  :
  # '2からmath.sqrt(N)の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2, int(math.sqrt(N))+1)  :
    # Nをiで割った余りが0のとき、
    if N % i == 0  :
      # 'F'を関数出力とする
      return 'F'
  # 'T'を関数出力とする
  return 'T'
# 入力された文字列の整数値をnとする
n = int(input())
# 0をansとする
ans = 0
# '0からn未満までの数列の各要素を順にjとして、繰り返す
for j  in range(n)  :
  # 入力された文字列の整数値をaとする
  a = int(input())
  # Sosu(a)が'T'のとき、
  if Sosu(a) == 'T'  :
    # ([[#Name 'ans'], [#Int '1']],)
    [[#Name 'ans'], [#Int '1']]
# ansを出力する
print(ans)
# mathモジュールを用いる
import math
# 関数sosuを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def sosu (n)  :
  # '3からmath.sqrt(n)の整数値に1を加えた値未満までの2間隔の数列の各要素を順にiとして、繰り返す
  for i  in range(3, int(math.sqrt(n))+1, 2)  :
    # nをiで割った余りが0のとき、
    if n % i == 0  :
      # 偽を関数出力とする
      return False
  # 真を関数出力とする
  return True
# (0、0、1、2、2、3、3、4、4、4、4)からなる列をSとする
S = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4]
# '11から1000000未満までの数列の各要素を順にiとして、繰り返す
for i  in range(11, 1000000)  :
  # iを2で割った余りが0のとき、
  if i % 2 == 0  :
    # S.append(S[i-1])
    S.append(S[i-1])
  # ('sosu(i)の',)
  elif sosu(i)  :
    # S.append(S[i-1]+1)
    S.append(S[i-1]+1)
  # ()
  else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'S']name: [#Name 'append']params: [#Arguments [#IndexExpr recv: [#Name 'S']index: [#Infix left: [#Name 'i']name: [#Name '-']right: [#Int '1']]]]]]]]
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'n']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
  # S(n)を出力する
  print(S[n])
# mathモジュールを用いる
import math
# 関数Sosuを[#FuncParam [#ParamDecl name: [#Name 'N']]]のパラメータを持つように定義する
def Sosu (N)  :
  # '2からmath.sqrt(N)の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2, int(math.sqrt(N))+1)  :
    # Nをiで割った余りが0のとき、
    if N % i == 0  :
      # 偽を関数出力とする
      return False
  # 真を関数出力とする
  return True
# 関数mainを[#FuncParam [#ParamDecl name: [#Name 'a']]]のパラメータを持つように定義する
def main (a)  :
  # 0をcountとする
  count = 0
  # '2からa未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2, a)  :
    # Sosu(i)のとき、
    if Sosu(i)  :
      # aからiを引いた値をotherとする
      other = a - i
      # otherがi以上、かつSosu(other)のとき、
      if other >= i and Sosu(other)  :
        # ([[#Name 'count'], [#Int '1']],)
        [[#Name 'count'], [#Int '1']]
  # countを関数出力とする
  return count
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # main(n)を出力する
  print(main(n))
# 関数Collatzを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def Collatz (n)  :
  # nを2で割った余りが0のとき、
  if n % 2 == 0  :
    # nを2で割った商を関数出力とする
    return n // 2
  # ()
  else :[#Else [#Block [#Return expr: [#Infix left: [#Infix left: [#Name 'n']name: [#Name '*']right: [#Int '3']]name: [#Name '+']right: [#Int '1']]]]]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # 0をcountとする
  count = 0
  # nが1と等しくない間、繰り返す
  while n != 1  :
    # Collatz(n)をnとする
    n = Collatz(n)
    # ([[#Name 'count'], [#Int '1']],)
    [[#Name 'count'], [#Int '1']]
  # countを出力する
  print(count)
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'd']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
  # 0をSとする
  S = 0
  # '0から600をdで割った商未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(600//d)  :
    # ([[#Name 'S'], [#Infix left: [#Infix left: [#Tuple [#Infix left: [#Name 'i']name: [#Name '*']right: [#Name 'd']]]name: [#Name '**']right: [#Int '2']]name: [#Name '*']right: [#Name 'd']]],)
    [[#Name 'S'], [#Infix left: [#Infix left: [#Tuple [#Infix left: [#Name 'i']name: [#Name '*']right: [#Name 'd']]]name: [#Name '**']right: [#Int '2']]name: [#Name '*']right: [#Name 'd']]]
  # Sを出力する
  print(S)
Syntax Error ((unknown source):13:16+428)
      print(f'{X:.3f} {Y:.3f}')
                ^              
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をqとする
  q = int(input())
  # qが-1のとき、
  if q == -1  :
    # 繰り返すのを中断する
    break
  # 1をnとする
  n = 1
  # qを2で割った値をxとする
  x = q / 2
  # 真の間、繰り返す
  while True :
    # {{xの3乗からqを引いた値}}の絶対値が({{0.00001にqを掛けた値}})の組より小さいとき、
    if abs(x**3 - q) < (0.00001 * q)  :
      # 繰り返すのを中断する
      break
    # xから({{xの3乗からqを引いた値}})の組を({{3にxの2乗を掛けた値}})の組で割った値を引いた値をxとする
    x = x - (x**3 - q) / (3 * x**2)
  # format(x)を出力する
  print('{:.6f}'.format(x))
Syntax Error ((unknown source):18:-1+328)
    else:
         
Syntax Error ((unknown source):3:8+38)
print(*s, sep = "")
        ^          
# 真の間、繰り返す
while True :
  # 入力された文字列をaとする
  a = input()
  # aが"END OF INPUT"のとき、
  if a == "END OF INPUT"  :
    # 繰り返すのを中断する
    break
  # 'aのリストをbとする
  b = list(a)
  # 0をcountとする
  count = 0
  # '0からbの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(b))  :
    # b(i)が' 'と等しくないとき、
    if b[i] != ' '  :
      # ([[#Name 'count'], [#Int '1']],)
      [[#Name 'count'], [#Int '1']]
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'count'][#Data [#KeyValue name: [#Name 'end']value: [#QString '""']]]]]][#VarDecl name: [#Name 'count']expr: [#Int '0']]]]
  # countを出力する
  print(count)
Syntax Error ((unknown source):54:10+1135)
    elif x == "U" :
          ^        
# 関数JOIOIを[#FuncParam [#ParamDecl name: [#Name 'l']]]のパラメータを持つように定義する
def JOIOI (l)  :
  # 0をcount_jとする
  count_j = 0
  # 0をcount_iとする
  count_i = 0
  # '0からlの長さから2を引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(l)-2)  :
    # {{l(i)が"J"}}、かつ{{l({{iに1を加えた値}})が"O"かどうか}}、かつl({{iに2を加えた値}})が"I"のとき、
    if l[i] == "J" and l[i+1] == "O" and l[i+2] == "I"  :
      # ([[#Name 'count_j'], [#Int '1']],)
      [[#Name 'count_j'], [#Int '1']]
    # {{l(i)が"I"}}、かつ{{l({{iに1を加えた値}})が"O"かどうか}}、かつl({{iに2を加えた値}})が"I"のとき、
    if l[i] == "I" and l[i+1] == "O" and l[i+2] == "I"  :
      # ([[#Name 'count_i'], [#Int '1']],)
      [[#Name 'count_i'], [#Int '1']]
  # (count_jとcount_i)の組を関数出力とする
  return count_j, count_i
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'l']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
  # JOIOI(l)を展開し順にjとiとする
  j, i  = JOIOI(l)
  # jを出力する
  print(j)
  # iを出力する
  print(i)
# 0をansとする
ans = 0
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
  # "True"をpalとする
  pal = "True"
  # '0からsの長さを2で割った商未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(s)//2)  :
    # s(i)がs({{-iから1を引いた値}})と等しくないとき、
    if s[i] != s[-i-1]  :
      # "False"をpalとする
      pal = "False"
      # 繰り返すのを中断する
      break
  # palが"True"のとき、
  if pal == "True"  :
    # ([[#Name 'ans'], [#Int '1']],)
    [[#Name 'ans'], [#Int '1']]
# ansを出力する
print(ans)
Syntax Error ((unknown source):8:8+171)
print(*n, sep="")    
        ^            
[#FromDecl name: [#ModuleName 'operator']names: [# [#Name 'itemgetter']]]
# '入力された文字列を空白で分割した列のリストをsentenceとする
sentence = list(input().split())
# 0をmax_lengthとする
max_length = 0
# ""をmax_sentenceとする
max_sentence = ""
# 空列をcountとする
count = []
# '0からsentenceの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(sentence))  :
  # max_lengthがsentence(i)の長さより小さいとき、
  if max_length < len(sentence[i])  :
    # sentence(i)の長さをmax_lengthとする
    max_length = len(sentence[i])
    # sentence(i)をmax_sentenceとする
    max_sentence = sentence[i]
  # 偽をnew_wordとする
  new_word = False
  # '0からcountの長さ未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(len(count))  :
    # count(j)(0)がsentence(i)のとき、
    if count[j][0] == sentence[i]  :
      # 真をnew_wordとする
      new_word = True
      # ([[#IndexExpr recv: [#IndexExpr recv: [#Name 'count']index: [#Name 'j']]index: [#Int '1']], [#Int '1']],)
      [[#IndexExpr recv: [#IndexExpr recv: [#Name 'count']index: [#Name 'j']]index: [#Int '1']], [#Int '1']]
      # 繰り返すのを中断する
      break
  # new_wordが偽のとき、
  if new_word == False  :
    # count.append([sentence[i], 1])
    count.append([sentence[i], 1])
# countと((key, itemgetter(1))と(reverse, 真))からなる辞書をソートした列をcountとする
count = sorted(count, key = itemgetter(1), reverse = True)
# countの最初値の最初値とmax_sentenceを出力する
print(count[0][0], max_sentence)
# '入力された文字列を空白で分割した列のリストをAとする
A = list(input().split())
# '0からAの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(A))  :
  # "apple"がA(i)に含まれるとき、
  if "apple" in A[i]  :
    # A(i)内の"apple"を"peach"で置き換えた文字列をA[i] にする
    A[i]  = A[i].replace("apple", "peach")
  # ('"peach"がA(i)に含まれる',)
  elif "peach" in A[i]  :
    # A(i)内の"peach"を"apple"で置き換えた文字列をA[i] にする
    A[i]  = A[i].replace("peach", "apple")
# Aを文字列" "で連結した文字列を出力する
print(" ".join(A))
Syntax Error ((unknown source):10:25+125)
    regex = re.compile('\d+')
                         ^   
# 真の間、繰り返す
while True :[#Try body: [#Block [#MultiAssignment left: [# [#Name 'a1'][#Name 'a2'][#Name 'a3'][#Name 'a4']]right: [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]][#MultiAssignment left: [# [#Name 'b1'][#Name 'b2'][#Name 'b3'][#Name 'b4']]right: [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
  # 0をhitとする
  hit = 0
  # 0をbrowとする
  brow = 0
  # a1がb1のとき、
  if a1 == b1  :
    # ([[#Name 'hit'], [#Int '1']],)
    [[#Name 'hit'], [#Int '1']]
  # a2がb2のとき、
  if a2 == b2  :
    # ([[#Name 'hit'], [#Int '1']],)
    [[#Name 'hit'], [#Int '1']]
  # a3がb3のとき、
  if a3 == b3  :
    # ([[#Name 'hit'], [#Int '1']],)
    [[#Name 'hit'], [#Int '1']]
  # a4がb4のとき、
  if a4 == b4  :
    # ([[#Name 'hit'], [#Int '1']],)
    [[#Name 'hit'], [#Int '1']]
  # {{a1がb2}}、または{{a1がb3かどうか}}、またはa1がb4のとき、
  if a1 == b2 or a1 == b3 or a1 == b4  :
    # ([[#Name 'brow'], [#Int '1']],)
    [[#Name 'brow'], [#Int '1']]
  # {{a2がb1}}、または{{a2がb3かどうか}}、またはa2がb4のとき、
  if a2 == b1 or a2 == b3 or a2 == b4  :
    # ([[#Name 'brow'], [#Int '1']],)
    [[#Name 'brow'], [#Int '1']]
  # {{a3がb1}}、または{{a3がb2かどうか}}、またはa3がb4のとき、
  if a3 == b1 or a3 == b2 or a3 == b4  :
    # ([[#Name 'brow'], [#Int '1']],)
    [[#Name 'brow'], [#Int '1']]
  # {{a4がb1}}、または{{a4がb2かどうか}}、またはa4がb3のとき、
  if a4 == b1 or a4 == b2 or a4 == b3  :
    # ([[#Name 'brow'], [#Int '1']],)
    [[#Name 'brow'], [#Int '1']]
  # hitとbrowを出力する
  print(hit, brow)
Syntax Error ((unknown source):27:10+699)
    elif sum_n <= sum_m :
          ^              
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # 0をcountとする
  count = 0
  # '1からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(1, n)  :
    # 0をsとする
    s = 0
    # 'iからn未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(i, n)  :
      # ([[#Name 's'], [#Name 'j']],)
      [[#Name 's'], [#Name 'j']]
      # sがnのとき、
      if s == n  :
        # ([[#Name 'count'], [#Int '1']],)
        [[#Name 'count'], [#Int '1']]
      # sがnより大きいとき、
      if s > n  :
        # 繰り返すのを中断する
        break
  # countを出力する
  print(count)
# 関数calc_beforeを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 's']]]のパラメータを持つように定義する
def calc_before (x, s)  :
  # 空列をansとする
  ans = []
  # '1からs未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(1, s)  :
    # iに{{{{iにxを掛けた値}}を100で割った値}}を加えた値の整数値をi_taxとする
    i_tax = int(i + i*x/100) 
    # '1からs未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(1, s)  :
      # jに{{{{jにxを掛けた値}}を100で割った値}}を加えた値の整数値をj_taxとする
      j_tax = int(j + j*x/100)
      # i_taxにj_taxを加えた値がsより大きいとき、
      if i_tax + j_tax > s  :
        # 繰り返すのを中断する
        break
      # i_taxにj_taxを加えた値がsのとき、
      if i_tax + j_tax == s  :
        # ans.append([i, j])
        ans.append([i, j])
  # ansを関数出力とする
  return ans
# 関数calc_afterを[#FuncParam [#ParamDecl name: [#Name 'i']][#ParamDecl name: [#Name 'j']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def calc_after (i, j, y)  :
  # {{iに{{{{iにyを掛けた値}}を100で割った値}}を加えた値}}の整数値に{{jに{{{{jにyを掛けた値}}を100で割った値}}を加えた値}}の整数値を加えた値をansとする
  ans = int(i + i*y/100) + int(j + j*y/100)
  # ansを関数出力とする
  return ans
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にx、y、sとする
  x, y, s  = map(int, input().split())
  # xが0、かつyが0のとき、
  if x == 0 and y == 0  :
    # 繰り返すのを中断する
    break
  # calc_before(x,s)をlstとする
  lst = calc_before(x, s)
  # 0をmax_priceとする
  max_price = 0
  # '0からlstの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(lst))  :
    # calc_after(lst(i)の最初値,lst(i)(1),y)をpriceとする
    price = calc_after(lst[i][0], lst[i][1], y)
    # priceとmax_priceの最大値をmax_priceとする
    max_price = max(price, max_price)
  # max_priceを出力する
  print(max_price)
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
  n, m  = map(int, input().split())
  # nが0、かつmが0のとき、
  if n == 0 and m == 0  :
    # 繰り返すのを中断する
    break
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをcatalogとする
  catalog = list(map(int, input().split()))
  # 0をmax_pとする
  max_p = 0
  # '0からnから1を引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n-1)  :
    # '1からn未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(1, n)  :
      # iがjと等しくないとき、
      if i != j  :
        # catalog(i)にcatalog(j)を加えた値をxとする
        x = catalog[i] + catalog[j]
        # xがm以下、かつxがmax_pより大きいとき、
        if x <= m and x > max_p  :
          # xをmax_pとする
          max_p = x
  # max_pが0のとき、
  if max_p == 0  :
    # "NONE"を出力する
    print("NONE")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'max_p']]]]]]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをlstとする
  lst = list(map(int, input().split()))
  # lstの総和をlstの長さで割った値をave_lstとする
  ave_lst = sum(lst) / len(lst)
  # 0をSumとする
  Sum = 0
  # '0からn未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n)  :
    # lst(i)がave_lst以下のとき、
    if lst[i] <= ave_lst  :
      # ([[#Name 'Sum'], [#Int '1']],)
      [[#Name 'Sum'], [#Int '1']]
  # Sumを出力する
  print(Sum)
# mathモジュールを用いる
import math
# 関数Sosuを[#FuncParam [#ParamDecl name: [#Name 'N']]]のパラメータを持つように定義する
def Sosu (N)  :
  # Nが1のとき、
  if N == 1  :
    # 偽を関数出力とする
    return False
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '2'][#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#MethodExpr recv: [#Name 'math']name: [#Name 'sqrt']params: [#Arguments [#Name 'N']]]]]name: [#Name '+']right: [#Int '1']]]]body: [#Block [#If cond: [#Infix left: [#Infix left: [#Name 'N']name: [#Name '%']right: [#Name 'i']]name: [#Name '==']right: [#Int '0']]then: [#Block [#Return expr: [#False 'False']]]]]][#Return expr: [#True 'True']]]]
# 関数amount_sosuを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def amount_sosu (a, b)  :
  # 0をansとする
  ans = 0
  # 'aに1を加えた値からbに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(a+1, b+1)  :
    # Sosu(i)のとき、
    if Sosu(i)  :
      # ([[#Name 'ans'], [#Int '1']],)
      [[#Name 'ans'], [#Int '1']]
  # ansを関数出力とする
  return ans
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0  :
    # 繰り返すのを中断する
    break
  # amount_sosu(n,{{nに2を掛けた値}})を出力する
  print(amount_sosu(n, n*2))
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、t、eとする
n, t, e  = map(int, input().split())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをwatchとする
watch = list(map(int, input().split()))
# 偽をansとする
ans = False
# '0からn未満までの数列の各要素を順にwとして、繰り返す
for w  in range(n)  :
  # '0からeに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(e+1)  :
    # ({{tにiを加えた値}})の組をwatch(w)で割った余りが0のとき、
    if (t+i) % watch[w] == 0  :
      # 真をansとする
      ans = True
      # 繰り返すのを中断する
      break
    # ({{tからiを引いた値}})の組をwatch(w)で割った余りが0のとき、
    if (t-i) % watch[w] == 0  :
      # 真をansとする
      ans = True
      # 繰り返すのを中断する
      break
  # ansが真のとき、
  if ans == True  :
    # 繰り返すのを中断する
    break
# ansが真のとき、
if ans == True  :
  # wに1を加えた値を出力する
  print(w+1)
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Unary name: [#Name '-']expr: [#Int '1']]]]]]]
Syntax Error ((unknown source):40:-1+761)
        elif (carrot[i] - now) < accel_time * speed :
                                                     
# map(整数,入力された文字列を空白で分割した列)を展開し順にdとlとする
d, l  = map(int, input().split())
# {{dをlで割った値}}に{{dをlで割った余り}}を加えた値の整数値をsとする
s = int(d / l + d % l)
# sを出力する
print(s)
# 関数put_Sを[#FuncParam [#ParamDecl name: [#Name 'n']][#ParamDecl name: [#Name 'd']]]のパラメータを持つように定義する
def put_S (n, d)  :[#Global [# [#Name 'square']]]
  # dが0のとき、
  if d == 0  :
    # square(n)(0)から1を引いた値をnew_iとする
    new_i = square[n][0] - 1
    # square(n)(1)をnew_jとする
    new_j = square[n][1]
  # ('dが1の',)
  elif d == 1  :
    # square(n)の最初値をnew_iとする
    new_i = square[n][0]
    # square(n)(1)から1を引いた値をnew_jとする
    new_j = square[n][1] - 1
  # ('dが2の',)
  elif d == 2  :
    # square(n)(0)に1を加えた値をnew_iとする
    new_i = square[n][0] + 1
    # square(n)(1)をnew_jとする
    new_j = square[n][1]
  # ('dが3の',)
  elif d == 3  :
    # square(n)の最初値をnew_iとする
    new_i = square[n][0]
    # square(n)(1)に1を加えた値をnew_jとする
    new_j = square[n][1] + 1
  # square.append([new_i, new_j])
  square.append([new_i, new_j])
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をNとする
  N = int(input())
  # Nが0のとき、
  if N == 0  :
    # 繰り返すのを中断する
    break
  # ((0と0)からなる列)からなる列をsquareとする
  square = [[0, 0]]
  # '0からNから1を引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(N-1)  :
    # map(整数,入力された文字列を空白で分割した列)を展開し順にnとdとする
    n, d  = map(int, input().split())
    # put_S(n,d)
    put_S(n, d) 
  # squareをソートした列をsort_x_squareとする
  sort_x_square = sorted(square)
  # squareと((key, [#FuncExpr params: [#Param [#Name 'x']]body: [#IndexExpr recv: [#Name 'x']index: [#Int '1']]]))からなる辞書をソートした列をsort_y_squareとする
  sort_y_square = sorted(square, key=lambda x:x[1])
  # {{sort_x_squareの末尾値(0)からsort_x_squareの最初値の最初値を引いた値}}に1を加えた値と{{sort_y_squareの末尾値(1)からsort_y_squareの最初値(1)を引いた値}}に1を加えた値を出力する
  print(sort_x_square[-1][0] - sort_x_square[0][0]+1, sort_y_square[-1][1] - sort_y_square[0][1]+1)
# 関数renameを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def rename (a, b)  :
  # 空列をnewとする
  new = []
  # ''aを反転した列のリストをre_aとする
  re_a = list(reversed(a))
  # ''bを反転した列のリストをre_bとする
  re_b = list(reversed(b))
  # new.append(''.join(a + b))
  new.append(''.join(a + b))
  # new.append(''.join(re_a + b))
  new.append(''.join(re_a + b))
  # new.append(''.join(a + re_b))
  new.append(''.join(a + re_b))
  # new.append(''.join(re_a + re_b))
  new.append(''.join(re_a + re_b))
  # new.append(''.join(b + a))
  new.append(''.join(b + a))
  # new.append(''.join(re_b + a))
  new.append(''.join(re_b + a))
  # new.append(''.join(b + re_a))
  new.append(''.join(b + re_a))
  # new.append(''.join(re_b + re_a))
  new.append(''.join(re_b + re_a))
  # 'newの集合のリストを関数出力とする
  return list(set(new))
# 入力された文字列の整数値をmとする
m = int(input())
# '0からm未満までの数列の各要素を順にiとして、繰り返す
for i  in range(m)  :
  # '入力された文字列のリストをtrainとする
  train = list(input())
  # 空列をnew_trainとする
  new_train = []
  # '1からtrainの長さ未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(1, len(train))  :
    # trainの位置先頭から位置jまでの部分をpre_trainとする
    pre_train = train[:j]
    # trainの先頭j個を取り除いた部分をbk_trainとする
    bk_train = train[j:]
    # new_trainにrename(pre_train,bk_train)を加えた値をnew_trainとする
    new_train = new_train + rename(pre_train, bk_train)
  # 'new_trainの集合のリストの長さを出力する
  print(len(list(set(new_train))))
# 真の間、繰り返す
while True :
  # 入力された文字列をsとする
  s = input()
  # 空列をtmpとする
  tmp = []
  # sが'.'のとき、
  if s == '.'  :
    # 繰り返すのを中断する
    break
  # 真をansとする
  ans = True
  # '0からsの長さ未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(s))  :
    # s(i)が'('のとき、
    if s[i] == '('  :
      # tmp.append(s[i])
      tmp.append(s[i])
    # ("s(i)が'['の",)
    elif s[i] == '['  :
      # tmp.append(s[i])
      tmp.append(s[i])
    # ("s(i)が')'の",)
    elif s[i] == ')'  :
      # not in('(',tmp)のとき、
      if '(' not in tmp  :
        # 偽をansとする
        ans = False
        # 繰り返すのを中断する
        break
      # ("tmp(-1)が'('の",)
      elif tmp[-1] == '('  :
        # tmp.pop(-1)
        tmp.pop(-1)
      # ()
      else :[#Else [#Block [#VarDecl name: [#Name 'ans']expr: [#False 'False']][#Break 'break']]]
    # ("s(i)が']'の",)
    elif s[i] == ']'  :
      # not in('[',tmp)のとき、
      if '[' not in tmp  :
        # 偽をansとする
        ans = False
        # 繰り返すのを中断する
        break
      # ("tmp(-1)が'['の",)
      elif tmp[-1] == '['  :
        # tmp.pop(-1)
        tmp.pop(-1)
      # ()
      else :[#Else [#Block [#VarDecl name: [#Name 'ans']expr: [#False 'False']][#Break 'break']]]
  # tmpの長さが0と等しくなく、またはansが偽のとき、
  if len(tmp) != 0 or ans == False  :
    # 'no'を出力する
    print('no')
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'yes'"]]]]]]
# 入力された文字列をpasとする
pas = input()
# pasの長さが6より小さいとき、
if len(pas) < 6  :
  # "INVALID"を出力する
  print("INVALID")
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'num']expr: [#Int '0']][#VarDecl name: [#Name 'Lstr']expr: [#Int '0']][#VarDecl name: [#Name 'Sstr']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'pas']]]]]body: [#Block [#If cond: [#And left: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 'pas']index: [#Name 'i']]]]name: [#Name '>=']right: [#Int '48']]right: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 'pas']index: [#Name 'i']]]]name: [#Name '<=']right: [#Int '57']]]then: [#Block [#SelfAssignment left: [#Name 'num']name: [# '+=']right: [#Int '1']]]][#If cond: [#And left: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 'pas']index: [#Name 'i']]]]name: [#Name '>=']right: [#Int '97']]right: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 'pas']index: [#Name 'i']]]]name: [#Name '<=']right: [#Int '122']]]then: [#Block [#SelfAssignment left: [#Name 'Lstr']name: [# '+=']right: [#Int '1']]]][#If cond: [#And left: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 'pas']index: [#Name 'i']]]]name: [#Name '>=']right: [#Int '65']]right: [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 'pas']index: [#Name 'i']]]]name: [#Name '<=']right: [#Int '90']]]then: [#Block [#SelfAssignment left: [#Name 'Sstr']name: [# '+=']right: [#Int '1']]]]]][#If cond: [#Or left: [#Or left: [#Infix left: [#Name 'num']name: [#Name '==']right: [#Int '0']]right: [#Infix left: [#Name 'Lstr']name: [#Name '==']right: [#Int '0']]]right: [#Infix left: [#Name 'Sstr']name: [#Name '==']right: [#Int '0']]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"INVALID"']]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"VALID"']]]]]]]]]
# 関数CheckDisitを[#FuncParam [#ParamDecl name: [#Name 'a']]]のパラメータを持つように定義する
def CheckDisit (a)  :
  # 0をtmpとする
  tmp = 0
  # '0から11未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(11)  :
    # iが4以下のとき、
    if i <= 4  :
      # ([[#Name 'tmp'], [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]]]name: [#Name '*']right: [#Tuple [#Infix left: [#Int '6']name: [#Name '-']right: [#Name 'i']]]]],)
      [[#Name 'tmp'], [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]]]name: [#Name '*']right: [#Tuple [#Infix left: [#Int '6']name: [#Name '-']right: [#Name 'i']]]]]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'tmp']name: [# '+=']right: [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'a']index: [#Name 'i']]]]name: [#Name '*']right: [#Tuple [#Infix left: [#Int '12']name: [#Name '-']right: [#Name 'i']]]]]]]
  # tmpを11で割った余りをtmpとする
  tmp = tmp % 11
  # tmpが1以下のとき、
  if tmp <= 1  :
    # 0を関数出力とする
    return 0
  # ()
  else :[#Else [#Block [#Return expr: [#Tuple [#Infix left: [#Int '11']name: [#Name '-']right: [#Name 'tmp']]]]]]
# '入力された文字列のリストをmとする
m = list(input())
# m(11)が'?'のとき、
if m[11] == '?'  :
  # CheckDisit(m)を出力する
  print(CheckDisit(m))
# ()
else :[#Else [#Block [#VarDecl name: [#Name 'ans']expr: [#List '[]']][#VarDecl name: [#Name 'x']expr: [#MethodExpr recv: [#Name 'm']name: [#Name 'index']params: [#Arguments [#QString "'?'"]]]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#Assignment left: [#IndexExpr recv: [#Name 'm']index: [#Name 'x']]right: [#ApplyExpr name: [#Name 'str']params: [#Arguments [#Name 'i']]]][#If cond: [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'm']index: [#Int '11']]]]name: [#Name '==']right: [#ApplyExpr name: [#Name 'CheckDisit']params: [#Arguments [#Name 'm']]]]then: [#Block [#Expression [#MethodExpr recv: [#Name 'ans']name: [#Name 'append']params: [#Arguments [#Name 'i']]]]]]]][#If cond: [#Infix left: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'ans']]]name: [#Name '==']right: [#Int '1']]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'ans']index: [#Int '0']]]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"MULTIPLE"']]]]]]]]]
# mathモジュールを用いる
import math
# 真の間、繰り返す
while True :
  # ((0、0、0)からなる列、(0、0、255)からなる列、(0、255、0)からなる列、(0、255、255)からなる列、(255、0、0)からなる列、(255、0、255)からなる列、(255、255、0)からなる列、(255、255、255)からなる列)からなる列をcolorとする
  color = [[0, 0, 0], [0, 0, 255], [0, 255, 0], [0, 255, 255], 
    [255, 0, 0], [255, 0, 255], [255, 255, 0], [255, 255, 255]]
  # 入力された文字列をcolor_16とする
  color_16 = input()
  # color_16が"0"のとき、
  if color_16 == "0"  :
    # 繰り返すのを中断する
    break
  # 16進数文字列color_16(1)にcolor_16(2)を加えた値の整数値をcolor_Rとする
  color_R = int(color_16[1] + color_16[2], 16)
  # 16進数文字列color_16(3)にcolor_16(4)を加えた値の整数値をcolor_Gとする
  color_G = int(color_16[3] + color_16[4], 16)
  # 16進数文字列color_16(5)にcolor_16(6)を加えた値の整数値をcolor_Bとする
  color_B = int(color_16[5] + color_16[6], 16)
  # 500をmin_dとする
  min_d = 500
  # '0から8未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(8)  :
    # color(i)の最初値をRとする
    R = color[i][0]
    # color(i)(1)をGとする
    G = color[i][1]
    # color(i)(2)をBとする
    B = color[i][2]
    # math.sqrt((R - color_R)**2 + (G - color_G)**2 + (B - color_B)**2)をdとする
    d = math.sqrt((R - color_R)**2 + (G - color_G)**2 + (B - color_B)**2)
    # min_dがdより大きいとき、
    if min_d > d  :
      # dをmin_dとする
      min_d = d
      # iをcolor_numとする
      color_num = i
  # color_numが0のとき、
  if color_num == 0  :
    # "black"を出力する
    print("black")
  # ('color_numが1の',)
  elif color_num == 1  :
    # "blue"を出力する
    print("blue") 
  # ('color_numが2の',)
  elif color_num == 2  :
    # "lime"を出力する
    print("lime")
  # ('color_numが3の',)
  elif color_num == 3  :
    # "aqua"を出力する
    print("aqua")
  # ('color_numが4の',)
  elif color_num == 4  :
    # "red"を出力する
    print("red")
  # ('color_numが5の',)
  elif color_num == 5  :
    # "fuchsia"を出力する
    print("fuchsia")
  # ('color_numが6の',)
  elif color_num == 6  :
    # "yellow"を出力する
    print("yellow")
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"white"']]]]]]
# ('Man'、'Oku'、'Cho'、'Kei'、'Gai'、'Jo'、'Jou'、'Ko'、'Kan'、'Sei'、'Sai'、'Gok'、'Ggs'、'Asg'、'Nyt'、'Fks'、'Mts'、'end')からなる列をtanniとする
tanni = ['Man', 'Oku', 'Cho', 'Kei', 'Gai', 'Jo', 'Jou', 'Ko', 'Kan', 'Sei', 
        'Sai', 'Gok', 'Ggs', 'Asg', 'Nyt', 'Fks', 'Mts' , 'end']
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
  m, n  = map(int, input().split())
  # mが0、かつnが0のとき、
  if m == 0 and n == 0  :
    # 繰り返すのを中断する
    break
  # mのn乗をsとする
  s = m**n[#Document [# 'print(s)']]
  # 空列をansとする
  ans = []
  # 0をiとする
  i = 0
  # 真の間、繰り返す
  while True :
    # ans.append(s % 10**4)
    ans.append(s % 10**4)
    # sを10の4乗で割った商をsとする
    s = s // 10**4
    # sが0のとき、
    if s == 0  :
      # 繰り返すのを中断する
      break
    # ()
    else :[#Else [#Block [#If cond: [#Infix left: [#IndexExpr recv: [#Name 'tanni']index: [#Name 'i']]name: [#Name '!=']right: [#QString "'end'"]]then: [#Block [#Expression [#MethodExpr recv: [#Name 'ans']name: [#Name 'append']params: [#Arguments [#IndexExpr recv: [#Name 'tanni']index: [#Name 'i']]]]]]]]]
    # tanni(i)が'end'と等しくないとき、
    if tanni[i] != 'end'  :
      # ([[#Name 'i'], [#Int '1']],)
      [[#Name 'i'], [#Int '1']]
  # ans.reverse()
  ans.reverse()
  # 偽をswitchとする
  switch = False
  # '0からansの長さ未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(len(ans))  :
    # ans(j)が0のとき、
    if ans[j] == 0  :
      # 真をswitchとする
      switch = True
    # ('switchが偽の',)
    elif switch == False  :
      # switchが真のとき、
      if switch == True  :
        # 偽をswitchとする
        switch = False
      # ()
      else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 'ans']index: [#Name 'j']][#Data [#KeyValue name: [#Name 'end']value: [#QString "''"]]]]]]]]
  # 空行を出力する
  print()
# mathモジュールを用いる
import math
# 関数calc_zyouzyoを[#FuncParam [#ParamDecl name: [#Name 'siki']]]のパラメータを持つように定義する
def calc_zyouzyo (siki)  :
  # 0をjとする
  j = 0
  # 真の間、繰り返す
  while True :
    # not in('*',siki)、かつnot in('/',siki)のとき、
    if '*' not in siki and '/' not in siki :
      # 繰り返すのを中断する
      break
    # siki(j)が'*'のとき、
    if siki[j] == '*'  :
      # siki({{jから1を引いた値}})の整数値にsiki({{jに1を加えた値}})の整数値を掛けた値の文字列をsiki[j-1] にする
      siki[j-1]  = str(int(siki[j-1]) * int(siki[j+1]))
      # sikiの位置jから位置jに2を加えた値までの部分を削除する
      del siki[j:j+2]
    # ("siki(j)が'/'の",)
    elif siki[j] == '/'  :
      # ({{siki[j-1]の整数値が0より小さく}}、かつ{{siki[j+1]の整数値が0より小さいかどうか}})の組、または({{siki[j-1]の整数値が0以上}}、かつ{{siki[j+1]の整数値が0以上かどうか}})の組のとき、
      if (int(siki[j-1]) < 0 and int(siki[j+1]) < 0) or (int(siki[j-1]) >= 0 and int(siki[j+1]) >= 0)  :
        # siki({{jから1を引いた値}})の整数値をsiki({{jに1を加えた値}})の整数値で割った商の文字列をsiki[j-1] にする
        siki[j-1]  = str(int(siki[j-1]) // int(siki[j+1]))
      # ()
      else :[#Else [#Block [#If cond: [#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '-']right: [#Int '1']]]]]name: [#Name '%']right: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '+']right: [#Int '1']]]]]]name: [#Name '==']right: [#Int '0']]then: [#Block [#Assignment left: [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '-']right: [#Int '1']]]right: [#ApplyExpr name: [#Name 'str']params: [#Arguments [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '-']right: [#Int '1']]]]]name: [#Name '//']right: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '+']right: [#Int '1']]]]]]]]]]else: [#Else [#Block [#Assignment left: [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '-']right: [#Int '1']]]right: [#ApplyExpr name: [#Name 'str']params: [#Arguments [#Infix left: [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '-']right: [#Int '1']]]]]name: [#Name '//']right: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'siki']index: [#Infix left: [#Name 'j']name: [#Name '+']right: [#Int '1']]]]]]name: [#Name '+']right: [#Int '1']]]]]]]]]]
      # sikiの位置jから位置jに2を加えた値までの部分を削除する
      del siki[j:j+2]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'j']name: [# '+=']right: [#Int '1']]]]
  # sikiの長さが1のとき、
  if len(siki) == 1  :
    # (sikiの最初値)の組を関数出力とする
    return (siki[0])
  # ()
  else :[#Else [#Block [#Return expr: [#Tuple [#Name 'siki']]]]]
# 関数calc_kagenを[#FuncParam [#ParamDecl name: [#Name 'siki']]]のパラメータを持つように定義する
def calc_kagen (siki)  :
  # 0をjとする
  j = 0
  # 真の間、繰り返す
  while True :
    # not in('+',siki)、かつnot in('-',siki)のとき、
    if '+' not in siki and '-' not in siki :
      # 繰り返すのを中断する
      break
    # siki(j)が'+'のとき、
    if siki[j] == '+'  :
      # siki({{jから1を引いた値}})の整数値にsiki({{jに1を加えた値}})の整数値を加えた値の文字列をsiki[j-1] にする
      siki[j-1]  = str(int(siki[j-1]) + int(siki[j+1]))
      # sikiの位置jから位置jに2を加えた値までの部分を削除する
      del siki[j:j+2]
    # ("siki(j)が'-'の",)
    elif siki[j] == '-'  :
      # siki({{jから1を引いた値}})の整数値からsiki({{jに1を加えた値}})の整数値を引いた値の文字列をsiki[j-1] にする
      siki[j-1]  = str(int(siki[j-1]) - int(siki[j+1]))
      # sikiの位置jから位置jに2を加えた値までの部分を削除する
      del siki[j:j+2]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'j']name: [# '+=']right: [#Int '1']]]]
  # sikiの長さが1のとき、
  if len(siki) == 1  :
    # (sikiの最初値)の組を関数出力とする
    return (siki[0])
  # ()
  else :[#Else [#Block [#Return expr: [#Tuple [#Name 'siki']]]]]
# 関数calcを[#FuncParam [#ParamDecl name: [#Name 'siki']]]のパラメータを持つように定義する
def calc (siki)  :
  # calc_zyouzyo(siki)をsikiとする
  siki = calc_zyouzyo(siki)
  # calc_kagen(siki)をsikiとする
  siki = calc_kagen(siki)
  # (siki)の組を関数出力とする
  return (siki)
# 入力された文字列の整数値をnとする
n = int(input())
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # '入力された文字列のリストをtmpとする
  tmp = list(input())
  # 空列をsikiとする
  siki = []
  # ''をnumとする
  num = ''
  # '0からtmpの長さ未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(len(tmp))  :
    # tmp(j)が('*'、'/'、'+'、'-'、'('、')'、'=')からなる列に含まれるとき、
    if tmp[j] in ['*', '/', '+', '-', '(', ')', '=']  :
      # numが''と等しくないとき、
      if num != ''  :
        # siki.append(num)
        siki.append(num)
      # siki.append(tmp[j])
      siki.append(tmp[j])
      # ''をnumとする
      num = ''
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'num']name: [# '+=']right: [#IndexExpr recv: [#Name 'tmp']index: [#Name 'j']]]]]
  # sikiから'='を取り除いた集まり
  siki.remove('=')
  # 0をjとする
  j = 0
  # 真の間、繰り返す
  while True :
    # jがsikiの長さ、またはnot in(')',siki)のとき、
    if j == len(siki) or ')' not in siki :
      # 繰り返すのを中断する
      break
    # 空列をstackとする
    stack = []
    # siki(j)が')'のとき、
    if siki[j] == ')'  :
      # 'jから1を引いた値から-1未満までの-1間隔の数列の各要素を順にkとして、繰り返す
      for k  in range(j-1,-1, -1)  :
        # siki(k)が'('のとき、
        if siki[k] == '('  :
          # 繰り返すのを中断する
          break
        # ()
        else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'stack']name: [#Name 'append']params: [#Arguments [#IndexExpr recv: [#Name 'siki']index: [#Name 'k']]]]]]]
      # stack.reverse()
      stack.reverse()
      # calc(stack)をsiki[k] にする
      siki[k]  = calc(stack)
      # sikiの位置kに1を加えた値から位置jに1を加えた値までの部分を削除する
      del siki[k+1 : j+1]
      # kに1を加えた値をjとする
      j = k+1
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'j']name: [# '+=']right: [#Int '1']]]]
  # calc(siki)をsikiとする
  siki = calc(siki)
  # sikiを出力する
  print(siki)
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
  # 0をiとする
  i = 0
  # iがsの長さより小さい間、繰り返す
  while i < len(s)  :
    # s(i)が"@"のとき、
    if s[i] == "@"  :
      # '0からs({{iに1を加えた値}})の整数値未満までの数列の各要素を順にjとして、繰り返す
      for j  in range(int(s[i+1]))  :
        # s({{iに2を加えた値}})と((end, ""))からなる辞書を出力する
        print(s[i+2], end="")
      # ([[#Name 'i'], [#Int '3']],)
      [[#Name 'i'], [#Int '3']]
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#Name 's']index: [#Name 'i']][#Data [#KeyValue name: [#Name 'end']value: [#QString '""']]]]]][#SelfAssignment left: [#Name 'i']name: [# '+=']right: [#Int '1']]]]
  # 空行を出力する
  print()
# map(整数,入力された文字列を空白で分割した列)を展開し順にH、A、Bとする
H, A, B  = map(int, input().split())
# 0をansとする
ans = 0
# 'AからBに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(A, B+1)  :
  # Hをiで割った余りが0のとき、
  if H % i == 0  :
    # ([[#Name 'ans'], [#Int '1']],)
    [[#Name 'ans'], [#Int '1']]
# ansを出力する
print(ans)
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'n']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
  # 0をcntとする
  cnt = 0
  # '0から10未満までの数列の各要素を順にaとして、繰り返す
  for a  in range(10)  :
    # '0から10未満までの数列の各要素を順にbとして、繰り返す
    for b  in range(10)  :
      # '0から10未満までの数列の各要素を順にcとして、繰り返す
      for c  in range(10)  :
        # '0から10未満までの数列の各要素を順にdとして、繰り返す
        for d  in range(10)  :
          # {{{{aにbを加えた値}}にcを加えた値}}にdを加えた値がnのとき、
          if a + b + c + d == n  :
            # ([[#Name 'cnt'], [#Int '1']],)
            [[#Name 'cnt'], [#Int '1']]
  # cntを出力する
  print(cnt)
# 入力された文字列の整数値をnとする
n = int(input())
# 入力された文字列の整数値をvとする
v = int(input())
# vをmaxvとする
maxv = v
# vをminvとする
minv = v
# -(10の9乗)の組をriekiとする
rieki = -(10**9)
# '0からnから1を引いた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n-1)  :
  # 入力された文字列の整数値をvとする
  v = int(input())
  # riekiがvからminvを引いた値より小さいとき、
  if rieki < v - minv  :
    # vからminvを引いた値をriekiとする
    rieki = v - minv
  # minvがvより大きいとき、
  if minv > v  :
    # vをminvとする
    minv = v
# riekiを出力する
print(rieki)
# 空列をstackとする
stack = []
# 入力された文字列を空白で分割した列をlstとする
lst = input().split()
# '0からlstの長さ未満までの数列の各要素を順にiとして、繰り返す
for i  in range(len(lst))  :
  # lst(i)が('+'、'-'、'*'、'/')からなる列に含まれるとき、
  if lst[i] in ['+', '-', '*', '/']  :
    # stack.pop(-1)をbとする
    b = stack.pop(-1)
    # stack.pop(-1)をaとする
    a = stack.pop(-1)
    # lst(i)が'+'のとき、
    if lst[i] == '+'  :
      # stack.append(a + b)
      stack.append(a + b)
    # ("lst(i)が'-'の",)
    elif lst[i] == '-'  :
      # stack.append(a - b)
      stack.append(a - b)
    # ("lst(i)が'*'の",)
    elif lst[i] == '*'  :
      # stack.append(a * b)
      stack.append(a * b)
    # ()
    else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'stack']name: [#Name 'append']params: [#Arguments [#Infix left: [#Name 'a']name: [#Name '//']right: [#Name 'b']]]]]]]
  # ()
  else :[#Else [#Block [#Expression [#MethodExpr recv: [#Name 'stack']name: [#Name 'append']params: [#Arguments [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'lst']index: [#Name 'i']]]]]]]]]
# stackの最初値を出力する
print(stack[0])
# map(整数,入力された文字列を空白で分割した列)を展開し順にnとqとする
n, q  = map(int, input().split())
# 空列をprocessとする
process = []
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n)  :
  # 入力された文字列を空白で分割した列を展開し順にnameとtimeとする
  name, time  = input().split()
  # process.append([name, int(time)])
  process.append([name, int(time)])
# 0をtimeとする
time = 0
# 真の間、繰り返す
while True :
  # processの長さが0のとき、
  if len(process) == 0  :
    # 繰り返すのを中断する
    break
  # processの最初値(1)がqより大きいとき、
  if process[0][1] > q  :
    # ([[#IndexExpr recv: [#IndexExpr recv: [#Name 'process']index: [#Int '0']]index: [#Int '1']], [#Name 'q']],)
    [[#IndexExpr recv: [#IndexExpr recv: [#Name 'process']index: [#Int '0']]index: [#Int '1']], [#Name 'q']]
    # ([[#Name 'time'], [#Name 'q']],)
    [[#Name 'time'], [#Name 'q']]
    # process.append(process[0])
    process.append(process[0])
    # process.pop(0)
    process.pop(0)
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'time']name: [# '+=']right: [#IndexExpr recv: [#IndexExpr recv: [#Name 'process']index: [#Int '0']]index: [#Int '1']]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#IndexExpr recv: [#IndexExpr recv: [#Name 'process']index: [#Int '0']]index: [#Int '0']][#Name 'time']]]][#Delete expr: [#IndexExpr recv: [#Name 'process']index: [#Int '0']]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをSとする
S = list(map(int, input().split()))
# 入力された文字列の整数値をqとする
q = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをTとする
T = list(map(int, input().split()))
# 0をcntとする
cnt = 0
# '0からq未満までの数列の各要素を順にiとして、繰り返す
for i  in range(q)  :
  # T(i)がSに含まれるとき、
  if T[i] in S  :
    # ([[#Name 'cnt'], [#Int '1']],)
    [[#Name 'cnt'], [#Int '1']]
# cntを出力する
print(cnt)
# 関数Checkを[#FuncParam [#ParamDecl name: [#Name 'A']][#ParamDecl name: [#Name 'i']][#ParamDecl name: [#Name 'j']][#ParamDecl name: [#Name 'W']][#ParamDecl name: [#Name 'H']]]のパラメータを持つように定義する
def Check (A, i, j, W, H)  :
  # jから1を引いた値が0以上のとき、
  if j-1 >= 0  :
    # A(i)({{jから1を引いた値}})が"."のとき、
    if A[i][j-1] == "."  :
      # "+"をA[i][j-1] にする
      A[i][j-1]  = "+"
      # Check(A,i,jから1を引いた値,W,H)
      Check(A, i, j-1, W, H)
  # iに1を加えた値がHより小さいとき、
  if i+1 < H  :
    # A({{iに1を加えた値}})(j)が"."のとき、
    if A[i+1][j] == "."  :
      # "+"をA[i+1][j]にする
      A[i+1][j] = "+"
      # Check(A,iに1を加えた値,j,W,H)
      Check(A, i+1, j, W, H)
  # jに1を加えた値がWより小さいとき、
  if j+1 < W  :
    # A(i)({{jに1を加えた値}})が"."のとき、
    if A[i][j+1] == "."  :
      # "+"をA[i][j+1] にする
      A[i][j+1]  = "+"
      # Check(A,i,jに1を加えた値,W,H)
      Check(A, i, j+1, W, H)
  # iから1を引いた値が0以上のとき、
  if i-1 >= 0  :
    # A({{iから1を引いた値}})(j)が"."のとき、
    if A[i-1][j] == "."  :
      # "+"をA[i-1][j] にする
      A[i-1][j]  = "+"
      # Check(A,iから1を引いた値,j,W,H)
      Check(A, i-1, j, W, H)
  # (A)の組を関数出力とする
  return (A)
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にWとHとする
  W, H  = map(int, input().split())
  # Wが0、かつHが0のとき、
  if W == 0 and H == 0  :
    # 繰り返すのを中断する
    break
  # {{'0からH未満までの数列}}の各要素をiとし、'入力された文字列のリストの列をTileとする
  Tile = [list(input()) for i in range(H)]
  # '0からH未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(H)  :
    # '0からW未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(W)  :
      # Tile(i)(j)が"@"のとき、
      if Tile[i][j] == "@"  :
        # iをmy_iとする
        my_i = i
        # jをmy_jとする
        my_j = j
  # "+"をTile[my_i][my_j] にする
  Tile[my_i][my_j]  = "+"
  # Check(Tile,my_i,my_j,W,H)をTile_newとする
  Tile_new = Check(Tile, my_i, my_j, W, H)
  # 0をcountとする
  count = 0
  # '0からH未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(H)  :
    # '0からW未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(W)  :
      # Tile_new(i)(j)が"+"のとき、
      if Tile_new[i][j] == "+"  :
        # ([[#Name 'count'], [#Int '1']],)
        [[#Name 'count'], [#Int '1']]
  # countを出力する
  print(count)