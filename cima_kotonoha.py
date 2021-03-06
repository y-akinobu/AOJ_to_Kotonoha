
# "Hello World"を出力する
print("Hello World")
# 入力された文字列の整数値の3乗を出力する
print(int(input())**3)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b = map(int,input().split())
# aにbを掛けた値と2に({{aにbを加えた値}})の組を掛けた値を出力する
print(a*b,2*(a+b))
# 入力された文字列をcとする
c = input()
# cを空白で分割した列を展開し順にaとbとする
a,b = c.split()
# (aの整数値がbの整数値より大きいかどうか)の組のとき、
if (int(a)>int(b)) :
  # 'a > b'を出力する
  print('a > b')
# ('(aの整数値がbの整数値より小さいかどうか)の組の',)
elif (int(a)<int(b)) :
  # 'a < b'を出力する
  print('a < b')
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'a == b'"]]]]]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c = map(int,input().split())
# ('No'と'Yes')からなる列({{{{aがbより小さいかどうか}}がcより小さいかどうか}})を出力する
print(['No','Yes'][a<b<c])
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c = map(int,input().split())
# ('Close'と'Open')からなる列(|(&(a,b),c))を出力する
print(['Close','Open'][a&b|c])
# 入力された文字列の整数値をsとする
s = int(input())
# sを3600で割った商、{{sを60で割った商}}を60で割った余り、sを60で割った余り、((sep, ':'))からなる辞書を出力する
print(s//3600,s//60%60,s%60,sep=':')
# ({{{{入力された文字列を空白で分割した列}}の各要素をiとし、iの整数値の列}})の組を(aとb)の組とする
(a,b)=(int(i) for i in input().split())
# '%s %s %.5f'を({{aをbで割った商}}、{{aをbで割った余り}}、{{aをbで割った値}})の組で割った余りを出力する
print('%s %s %.5f'%(a//b,a%b,a/b))
[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'pi']]]
# 入力された文字列の浮動小数点数値をrとする
r = float(input())
# テンプレート{{{{rにrを掛けた値}}にpiを掛けた値}}を{{{{2にpiを掛けた値}}にrを掛けた値}}でフォーマットした文字列を出力する
print("{} {}".format(r*r*pi,2*pi*r))
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b = map(int,input().split())
# {{aにbを掛けた値}}を3.305785で割った値を出力する
print(a*b/3.305785)
# {{入力された文字列を空白で分割した列}}の各要素をiとし、iの整数値の列をdとする
d = [int(i) for i in input().split()]
# d.sort()
d.sort()
# format(dの最初値,d(1),d(2))を出力する
print("{0} {1} {2}".format(d[0],d[1],d[2]))
# 入力された文字列を空白で分割した列をnumとする
num = input().split()
# numの最初値の整数値をWとする
W = int(num[0])
# num(1)の整数値をHとする
H = int(num[1])
# num(2)の整数値をxとする
x = int(num[2])
# num(3)の整数値をyとする
y = int(num[3])
# num(4)の整数値をrとする
r = int(num[4])
# ({{x-rが0より小さく}}、または{{y-rが0より小さいかどうか}}、または{{{{xにrを加えた値}}がWより大きいかどうか}}、または{{{{yにrを加えた値}}がHより大きいかどうか}})の組のとき、
if (x-r<0 or y-r<0 or x+r>W or y+r>H) :
  # 'No'を出力する
  print('No')
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'Yes'"]]]]]]
# map(整数,{{入力された文字列を空白で分割した列}})をソートした列を展開し順にa、b、c、dとする
a,b,c,d = sorted(map(int,input().split()))
# ('no'と'yes')からなる列({{aがb}}、かつ{{cがdかどうか}})を出力する
print(['no','yes'][a==b and c==d])
# (6、4、3、2)からなる列をpとする
p = [6,4,3,2]
# '0から4未満までの数列の各要素を順に_として、繰り返す
for _  in range(4) :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にtとnとする
  t,n = map(int,input().split())
  # {{p({{tから1を引いた値}})にnを掛けた値}}に1000を掛けた値を出力する
  print(p[t-1]*n*1000)
# 7をnとする
n = 7
# nの間、繰り返す
while n :
  # ([[#Name 'n'], [#Int '1']],)
  [[#Name 'n'], [#Int '1']]
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a,b = map(int,input().split())
  # aからbを引いた値を出力する
  print(a-b)
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#MultiAssignment left: [# [#Name 'a'][#Name 'b'][#Name 'c']]right: [#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # map(整数,(bとc)からなる列)を展開し順にbとcとする
  b,c = map(int,[b,c])
  # a、bにcを加えた値、{{bに200を掛けた値}}に{{cに300を掛けた値}}を加えた値を出力する
  print(a,b+c,b*200+c*300)
# {{{{'0から10未満までの数列}}の各要素を_とし、input()の整数値の列}}の総和を出力する
print(sum([int(input()) for _ in range(10)]))
# 入力された文字列をxとする
x = input()
# 1をiとする
i = 1
# (xが'0'と等しくないかどうか)の組の間、繰り返す
while (x!='0') :
  # テンプレートiをxでフォーマットした文字列を出力する
  print("Case {0}: {1}".format(i,x))
  # ([[#Name 'i'], [#Int '1']],)
  [[#Name 'i'], [#Int '1']]
  # 入力された文字列をxとする
  x = input()
# mathモジュールを用いる
import math
# 100をaとする
a = 100
# '0から入力された文字列の整数値未満までの数列の各要素を順に_として、繰り返す
for _  in range(int(input())) :
  # math.ceil(a*1.05)をaとする
  a = math.ceil(a*1.05)
# aに1000を掛けた値を出力する
print(a*1000)
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c = map(int,input().split())
# 0をdとする
d = 0
# aがbに1を加えた値と等しくない間、繰り返す
while a!=b+1 :
  # cをaで割った余りが0のとき、
  if c%a==0 :
    # ([[#Name 'd'], [#Int '1']],)
    [[#Name 'd'], [#Int '1']]
  # ([[#Name 'a'], [#Int '1']],)
  [[#Name 'a'], [#Int '1']]
# dを出力する
print(d)
# '1から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(1,10) :
  # '1から10未満までの数列の各要素を順にjとして、繰り返す
  for j  in range(1,10) :
    # "%dx%d=%d"を(i、j、{{iにjを掛けた値}})の組で割った余りを出力する
    print("%dx%d=%d"%(i,j,i*j))
[#Document [# '-*- coding: utf-8 -*-']]
# 1の間、繰り返す
while 1 :
  # {{{{入力された文字列を空白で分割した列}}の各要素をiとし、iの整数値の列}}を(HとW)の組とする
  (H,W) = [int(i) for i in input().split()]
  # HがWかどうかが0のとき、
  if H==W==0 :
    # 繰り返すのを中断する
    break
  # '0からH未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(H) :
    # '0からW未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(W) :
      # ({{iにjを加えた値}})の組を2で割った余りが0のとき、
      if (i+j)%2==0 :
        # '#'と((end, ""))からなる辞書を出力する
        print('#',end="")
      # ()
      else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString "'.'"][#Data [#KeyValue name: [#Name 'end']value: [#QString '""']]]]]]]]
    # ''を出力する
    print('')
  # ''を出力する
  print('')
# 1の間、繰り返す
while 1 :
  # 入力された文字列をsとする
  s = input()
  # '?'がsに含まれるとき、
  if '?' in s :
    # 繰り返すのを中断する
    break
  # {{ 文字列sを評価した値}}の整数値を出力する
  print(int(eval(s)))
# 入力された文字列
input()
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# aの最小値、aの最大値、aの総和を出力する
print(min(a),max(a),sum(a))
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが3より小さいとき、
  if n<3 :
    # 繰り返すのを中断する
    break
  # ({{sorted([int(input()) for _ in [0]*n])の位置1から位置-1までの部分}}の総和)の組を({{nから2を引いた値}})の組で割った商を出力する
  print((sum(sorted([int(input()) for _ in [0]*n])[1:-1]))//(n-2))
# 1をbとするをaとする
a = b=1
# '0から入力された文字列の整数値未満までの数列の各要素を順に_として、繰り返す
for _  in range(int(input())) :
  # bとaにbを加えた値をaとbとする
  a,b = b,a+b
# aを出力する
print(a)
# 入力された文字列
input()
# {{入力された文字列を空白で分割した列}}の逆順を文字列' 'で連結した文字列を出力する
print(' '.join(input().split()[::-1]))
# {{range(5)の各要素を_とし、max(40,int(input())) の列}}の総和を5で割った商を出力する
print(sum([max(40,int(input())) for _ in range(5)])//5)
# {{{{int(input()) for _ in range(4)をソートした列}}の先頭を除いた部分}}の総和に{{{{'0から2未満までの数列}}の各要素を_とし、input()の整数値の列}}の最大値を加えた値を出力する
print(sum(sorted(int(input()) for _ in range(4))[1:])+max(int(input()) for _ in range(2)))
# *(({{{{'0から2未満までの数列}}の各要素を_とし、sorted([int(input()) for _ in range(10)])[-3:]の総和の列}})の組)を出力する
print(*(sum(sorted([int(input()) for _ in range(10)])[-3:]) for _ in range(2)))
# queueモジュールを用いる
import queue
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとkとする
  n,k = map(int,input().split())
  # nが0のとき、
  if n==0 :
    # 繰り返すのを中断する
    break
  # queue.deque(int(input()) for _ in range(k))をaとする
  a = queue.deque(int(input()) for _ in range(k))
  # aの総和をbとするをmとする
  m = b=sum(a)
  # '0からnからkを引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(n-k) :
    # a.popleft()をcとする
    c = a.popleft()
    # 入力された文字列の整数値をdとする
    d = int(input())
    # a.append(d)
    a.append(d)
    # ([[#Name 'b'], [#Infix left: [#Name 'd']name: [#Name '-']right: [#Name 'c']]],)
    [[#Name 'b'], [#Infix left: [#Name 'd']name: [#Name '-']right: [#Name 'c']]]
    # bとmの最大値をmとする
    m = max(b,m)        
  # mを出力する
  print(m)
# ({{{{[int(input()) for _ in range(10)]をソートした列}}の位置先頭から-1間隔で位置6までの部分}})の組の各要素をiとし、{{iを出力する}}の列
[print(i) for i in (sorted([int(input()) for _ in range(10)])[:6:-1])]
# 入力された文字列を英大文字に変換した文字列をxとする
x = input().upper()
# xを出力する
print(x)
# 入力された文字列の英大文字を英小文字、英小文字を英大文字に変換した文字列を出力する
print(input().swapcase())
# sysモジュールを用いる
import sys
# sys.stdin.read()を英小文字に変換した文字列をsとする
s = sys.stdin.read().lower()
# '97から123未満までの数列の各要素を順にiとして、繰り返す
for i  in range(97,123) :
  # 文字コードiの文字、':'、s内の文字コードiの文字の出現をカウントした整数を出力する
  print(chr(i),':',s.count(chr(i)))
# 1の間、繰り返す
while 1 :
  # 入力された文字列をnとする
  n = input()
  # nが'0'のとき、
  if n=='0' :
    # 繰り返すのを中断する
    break
  # {{nの各要素をxとし、xの整数値の列}}の総和を出力する
  print(sum(int(x) for x in n))
# 入力された文字列をsとする
s = input()
# {{'KUPC'の各要素をiとし、{{s内のiの出現をカウントした整数}}の列}}の最小値を出力する
print(min(s.count(i) for i in 'KUPC'))
# 入力された文字列を英小文字に変換した文字列をwとする
w = input().lower()
# 空列をcとする
c = []
# 入力された文字列をsとする
s = input()
# (sが'END_OF_TEXT'と等しくないかどうか)の組の間、繰り返す
while (s!='END_OF_TEXT') :
  # ([[#Name 'c'], [#MethodExpr recv: [#MethodExpr recv: [#Name 's']name: [#Name 'lower']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]],)
  [[#Name 'c'], [#MethodExpr recv: [#MethodExpr recv: [#Name 's']name: [#Name 'lower']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]
  # 入力された文字列をsとする
  s = input()
# {{cの各要素をxとし、{{xがwの}}ときのxの列}}の長さを出力する
print(len([x for x in c if x==w]))
# 入力された文字列をIとする
I = input
# I()に2を掛けた値をsとする
s = I()*2
# ('No'と'Yes')からなる列({{I()がsに含まれるかどうか}})を出力する
print(['No','Yes'][I()in s])
# 入力された文字列をtとする
t = input()
# 入力された文字列をpとする
p = input()
# {{'0からtの長さ未満までの数列}}の各要素をiとし、{{{{tの先頭i個を取り除いた部分}}の先頭がpで始まる}}ときの{{iを出力する}}の列
[print(i)for i in range(len(t))if t[i:].startswith(p)]
# 0をtとするをhとする
h = t=0
# '0から入力された文字列の整数値未満までの数列の各要素を順に_として、繰り返す
for _  in range(int(input())) :
  # 入力された文字列を空白で分割した列を展開し順にaとbとする
  a,b = input().split()
  # aがbより大きいとき、
  if a>b :
    # ([[#Name 't'], [#Int '3']],)
    [[#Name 't'], [#Int '3']]
  # ('aがbより小さい',)
  elif a<b :
    # ([[#Name 'h'], [#Int '3']],)
    [[#Name 'h'], [#Int '3']]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 't']name: [# '+=']right: [#Int '1']][#SelfAssignment left: [#Name 'h']name: [# '+=']right: [#Int '1']]]]
# tとhを出力する
print(t,h)
# 1の間、繰り返す
while 1 :
  # 入力された文字列をaとする
  a = input()
  # aが'0'のとき、
  if a=='0' :
    # 繰り返すのを中断する
    break
  # aの先頭を除いた部分内の'A'の出現をカウントした整数とaの先頭を除いた部分内の'B'の出現をカウントした整数をdとeとする
  d,e = a[1:].count('A'),a[1:].count('B')
  # dがeより小さいとき(0と1)の組を(bとc)の組とする、そうでなければ(1と0)の組
  (b,c)=(0,1) if d<e else (1,0)
  # dにbを加えた値とeにcを加えた値を出力する
  print(d+b,e+c)
# map(float,入力された文字列を空白で分割した列)を展開し順にx、y、xx、yyとする
x,y,xx,yy = map(float, input().split())
# '%5f'を({{(x-xx)**2に(y-yy)**2を加えた値}})の組の0.5乗で割った余りを出力する
print('%5f'%((x-xx)**2+(y-yy)**2)**0.5)
[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'sin'][#Name 'cos'][#Name 'radians']]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a,b,c = map(int,input().split())
# radians(c)をcとする
c = radians(c)
# {{aにbを掛けた値}}にsin(c)を掛けた値に0.5を掛けた値をsとする
s = a*b*sin(c)*0.5
# (s、{{aにbを加えた値}}に({{a*a+b*bから2*a*b*cos(c)を引いた値}})の組の0.5乗を加えた値、{{sをaで割った値}}に2を掛けた値)からなる列の各要素を順にiとして、繰り返す
for i  in [s,a+b+(a*a+b*b-2*a*b*cos(c))**0.5,s/a*2] :
  # '%5f'をiで割った余りを出力する
  print('%5f'%i)
# 入力された文字列が'0'と等しくない間、繰り返す
while input()!='0' :
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをnとする
  n = list(map(int,input().split()))
  # nの長さをbとする
  b = len(n)
  # nの総和をbで割った値をaとする
  a = sum(n)/b
  # ({{(x-a)**2 for x in nの総和をbで割った値}})の組の0.5乗を出力する
  print((sum((x-a)**2 for x in n)/b)**0.5)
# itertoolsモジュールを用いる
import itertools
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとsとする
  n,s = map(int, input().split())
  # nが0のとき、
  if n==0 :
    # 繰り返すのを中断する
    break
  # {{itertools.combinations(range(1,n+1), 3) の各要素をcとし、{{sum(c)がsの}}ときの1の列}}の長さを出力する
  print(len([1 for c in itertools.combinations(range(1,n+1), 3) if sum(c)==s]))
# map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
n,m = map(int,input().split())
# {{'0からn未満までの数列}}の各要素を_とし、'map(整数,{{input()を空白で分割した列}})のリストの列をaとする
a = [list(map(int,input().split())) for _ in range(n)]
# {{'0からm未満までの数列}}の各要素を_とし、入力された文字列の整数値の列をbとする
b = [int(input()) for _ in range(m)]
# {{'0からn未満までの数列}}の各要素をiとし、{{j*k for j,k in zip(a[i],b)の総和を出力する}}の列
[print(sum([j*k for j,k in zip(a[i],b)])) for i in range(n)]
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、m、lとする
n,m,l = map(int,input().split())
# {{'0からn未満までの数列}}の各要素を_とし、'map(整数,{{input()を空白で分割した列}})のリストの列をaとする
a = [list(map(int,input().split())) for _ in range(n)]
# {{'0からm未満までの数列}}の各要素を_とし、'map(整数,{{input()を空白で分割した列}})のリストの列をbとする
b = [list(map(int,input().split())) for _ in range(m)]
# {{aの各要素をxとし、sum(j*k for j,k in zip(x,y)) for y in zip(*b)の列}}の各要素をxとし、{{*(x)を出力する}}の列
[print(*x) for x in [[sum(j*k for j,k in zip(x,y)) for y in zip(*b)] for x in a]]
# 入力された文字列をnとする
n = input()
# nに': 'を加えた値と((end, ''))からなる辞書を出力する
print(n+': ',end='')
# nの整数値をnとする
n = int(n)
# 2をdとする
d = 2
# {{nをdで割った余り}}が0、かつnが3より大きい間、繰り返す
while n%d==0 and n>3 :
  # dと((end, ' '))からなる辞書を出力する
  print(d,end=' ')
  # ([[#Name 'n'], [#Name 'd']],)
  [[#Name 'n'], [#Name 'd']]
# ([[#Name 'd'], [#Int '1']],)
[[#Name 'd'], [#Int '1']]
# nをdで割った商をmとする
m = n//d
# mがd以上の間、繰り返す
while m>=d :
  # ({{nをdで割った余り}}が0かどうか)の組のとき、
  if (n%d==0) :
    # dと((end, ' '))からなる辞書を出力する
    print(d,end=' ')
    # mをnとする
    n = m
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'd']name: [# '+=']right: [#Int '2']]]]
  # nをdで割った商をmとする
  m = n//d
# nを出力する
print(n)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b = map(int,input().split())
# aのb乗に対する1000000007の剰余を出力する
print(pow(a,b,1000000007))
Syntax Error ((unknown source):3:18+40)
    while b:(a,b),c=(b,a%b),c+1
                  ^            
# 関数gcdを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def gcd (a,b) :
  # bの間、繰り返す
  while b :
    # bとaをbで割った余りをaとbとする
    a,b = b,a%b
  # aを関数出力とする
  return a
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']]]のパラメータを持つように定義する
def lcm (a,b) :
  # aをgcd(a,b)で割った商にbを掛けた値を関数出力とする
  return a//gcd(a,b)*b
# 入力された文字列
input()
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをaとする
a = list(map(int,input().split()))
# 1をbとする
b = 1
# aの各要素を順にiとして、繰り返す
for i  in a :
  # lcm(b,i)をbとする
  b = lcm(b,i)
# bを出力する
print(b)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a,b = map(int,input().split())
# bの間、繰り返す
while b :
  # bとaをbで割った余りをaとbとする
  a,b = b,a%b
# aを出力する
print(a)
# 32768をNとする
N = 32768
# {{'0からN未満までの数列}}の各要素をiとし、iの列をpとする
p = [i for i in range(N)]
# '2からNの0.5乗の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(2,int(N**0.5)+1) :
  # p(i)のとき、
  if p[i] :
    # 'iにiを掛けた値からN未満までのi間隔の数列の各要素を順にjとして、繰り返す
    for j  in range(i*i,N,i) :
      # 0をp[j]にする
      p[j] = 0
# pの集合をソートした列の先頭2個を取り除いた部分をpとする
p = sorted(set(p))[2:]
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n==0 :
    # 繰り返すのを中断する
    break
  # 0をcとする
  c = 0
  # &(n,1)のとき、
  if n&1 :
    # {{nから2を引いた値}}がpに含まれるかどうかの整数値をcとする
    c = int(n-2 in p)
  # ()
  else :[#Else [#Block [#For each: [# [#Name 'x']]list: [#Name 'p']body: [#Block [#If cond: [#Infix left: [#Name 'x']name: [#Name '>']right: [#Infix left: [#Name 'n']name: [#Name '//']right: [#Int '2']]]then: [#Block [#Break 'break']]][#If cond: [#Infix left: [#Infix left: [#Name 'n']name: [#Name '-']right: [#Name 'x']]name: [#Name 'in']right: [#Name 'p']]then: [#Block [#SelfAssignment left: [#Name 'c']name: [# '+=']right: [#Int '1']]]]]]]]
  # cを出力する
  print(c)
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n==0 :
    # 繰り返すのを中断する
    break
  # 0をcとする
  c = 0
  # nが1と等しくない間、繰り返す
  while n!=1 :
    # nを2で割った余りのとき{{nに3を掛けた値}}に1を加えた値、そうでなければnを2で割った値をnとする
    n = n*3+1 if n%2 else n/2
    # ([[#Name 'c'], [#Int '1']],)
    [[#Name 'c'], [#Int '1']]
  # cを出力する
  print(c)
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'd']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # {{{{'0から600//d未満までの数列}}の各要素をiとし、{{(i*d)**2にdを掛けた値}}の列}}の総和を出力する
  print(sum([(i*d)**2*d for i in range(600//d)]))
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#MultiAssignment left: [# [#Name 'a'][#Name 'b'][#Name 'c'][#Name 'd'][#Name 'e'][#Name 'f']]right: [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # ({{{{cにdを掛けた値}}から{{aにfを掛けた値}}を引いた値}})の組を({{{{bにdを掛けた値}}から{{aにeを掛けた値}}を引いた値}})の組で割った値をxとする
  x = (c*d-a*f)/(b*d-a*e)
  # "%.3f %.3f"を({{(c-b*x)の組をaで割った値}}とx)の組で割った余りを出力する
  print("%.3f %.3f"%((c-b*x)/a,x))
# 1の間、繰り返す
while 1 :
  # 入力された文字列の浮動小数点数値をqとする
  q = float(input())
  # qが0より小さいとき、
  if q<0 :
    # 繰り返すのを中断する
    break
  # qを2で割った値をxとする
  x = q/2
  # {{xの3乗からqを引いた値}}の絶対値がqに10の(-5)の組乗を掛けた値以上の間、繰り返す
  while abs(x**3-q)>=q*10**(-5) :
    # ([[#Name 'x'], [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Name 'x']name: [#Name '**']right: [#Int '3']]name: [#Name '-']right: [#Name 'q']]]name: [#Name '/']right: [#Tuple [#Infix left: [#Infix left: [#Int '3']name: [#Name '*']right: [#Name 'x']]name: [#Name '*']right: [#Name 'x']]]]],)
    [[#Name 'x'], [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Name 'x']name: [#Name '**']right: [#Int '3']]name: [#Name '-']right: [#Name 'q']]]name: [#Name '/']right: [#Tuple [#Infix left: [#Infix left: [#Int '3']name: [#Name '*']right: [#Name 'x']]name: [#Name '*']right: [#Name 'x']]]]]
  # xを出力する
  print(x)
# {{{{input().replace(',','').replace('.','')を空白で分割した列}}の各要素をxとし、{{2<len(x)が7より小さい}}ときのxの列}}を文字列' 'で連結した文字列を出力する
print(' '.join([x for x in input().replace(',','').replace('.','').split() if 2<len(x)<7]))
# 入力された文字列の逆順を出力する
print(input()[::-1])
# 1の間、繰り返す
while 1 :
  # 入力された文字列をnとする
  n = input()
  # nが"END OF INPUT"のとき、
  if n=="END OF INPUT" :
    # 繰り返すのを中断する
    break
  # 0をcとする
  c = 0
  # nの各要素を順にiとして、繰り返す
  for i  in n :
    # iが' 'のとき、
    if i==' ' :
      # cと((end, ""))からなる辞書を出力する
      print(c,end="")
      # 0をcとする
      c = 0
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'c']name: [# '+=']right: [#Int '1']]]]
  # cを出力する
  print(c)
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'a']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # 0をcとするをbとする
  b = c=0
  # '0からaの長さから2を引いた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(len(a)-2) :
    # aの位置iから位置{{iに3を加えた値}}までの部分が'JOI'のとき、
    if a[i:i+3]=='JOI' :
      # ([[#Name 'b'], [#Int '1']],)
      [[#Name 'b'], [#Int '1']]
    # ("aの位置iから位置{{iに3を加えた値}}までの部分が'IOI'の",)
    elif a[i:i+3]=='IOI' :
      # ([[#Name 'c'], [#Int '1']],)
      [[#Name 'c'], [#Int '1']]
  # bを出力する
  print(b)
  # cを出力する
  print(c)
# 0をaとする
a = 0
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # sがsの逆順のとき、
  if s==s[::-1] :
    # ([[#Name 'a'], [#Int '1']],)
    [[#Name 'a'], [#Int '1']]
# aを出力する
print(a)
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'をaとする
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 入力された文字列の各要素を順にxとして、繰り返す
for x  in input() :
  # a({{a.index(x)から3を引いた値}})と((end, ''))からなる辞書を出力する
  print(a[a.index(x)-3],end='')
# 空行を出力する
print()
# 入力された文字列を空白で分割した列をsとする
s = input().split()
# sと((key, sのcount))からなる辞書の最大値とsと((key, len))からなる辞書の最大値を出力する
print(max(s,key=s.count),max(s,key=len))
# {{{{入力された文字列内の'apple'を'#'で置き換えた文字列}}内の'peach'を'apple'で置き換えた文字列}}内の'#'を'peach'で置き換えた文字列を出力する
print(input().replace('apple','#').replace('peach','apple').replace('#','peach'))
# reモジュールを用いる
import re
# 0をpとする
p = 0
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # re.findall('[0-9]+',s)の各要素を順にiとして、繰り返す
  for i  in re.findall('[0-9]+',s) :
    # ([[#Name 'p'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'i']]]],)
    [[#Name 'p'], [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'i']]]]
# pを出力する
print(p)
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 'a']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをbとする
  b = list(map(int, input().split()))
  # 0をhとする
  h = 0
  # aとbの要素をそれぞれ組にした列の各要素を順にiとjとして、繰り返す
  for i,j  in zip(a,b) :
    # ([[#Name 'h'], [#Infix left: [#Name 'i']name: [#Name '==']right: [#Name 'j']]],)
    [[#Name 'h'], [#Infix left: [#Name 'i']name: [#Name '==']right: [#Name 'j']]]
  # hと&(aの集合,bの集合)の長さからhを引いた値を出力する
  print(h,len(set(a)&set(b))-h)
# 関数tを[#FuncParam [#ParamDecl name: [#Name 'a']][#ParamDecl name: [#Name 'b']][#ParamDecl name: [#Name 'x']]]のパラメータを持つように定義する
def t (a,b,x) :
# {{bに({{100にxを加えた値}})の組を掛けた値}}を100で割った商に{{({{aからbを引いた値}})の組に({{100にxを加えた値}})の組を掛けた値}}を100で割った商を加えた値を関数出力とする
return b*(100+x)//100+(a-b)*(100+x)//100
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にx、y、sとする
  x,y,s = map(int,input().split())
  # xが0のとき、
  if x==0 :
    # 繰り返すのを中断する
    break
  # 0をaとする
  a = 0
  # '{{sに100を掛けた値}}を({{100にxを加えた値}})の組で割った商からsに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(s*100//(100+x),s+1) :
    # '1から{{iを2で割った商}}に1を加えた値未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(1,i//2+1) :
      # t(i,j,x)がsと等しくないとき、
      if t(i,j,x)!=s :
        # 何もしない
        pass
      # ()
      else :[#Else [#Block [#VarDecl name: [#Name 'a']expr: [#ApplyExpr name: [#Name 'max']params: [#Arguments [#Name 'a'][#ApplyExpr name: [#Name 't']params: [#Arguments [#Name 'i'][#Name 'j'][#Name 'y']]]]]]]]
  # aを出力する
  print(a)   
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、t、eとする
n,t,e = map(int,input().split())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをxとする
x = list(map(int,input().split()))
# -1をansとする
ans = -1
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # 'x(i)から20000未満までのx(i)間隔の数列の各要素を順にjとして、繰り返す
  for j  in range(x[i],20000,x[i]) :
    # {{tからeを引いた値}}がj以下かどうかがtにeを加えた値以下のとき、
    if t-e<=j<=t+e :
      # iに1を加えた値をansとする
      ans = i+1
      # 繰り返すのを中断する
      break
# ansを出力する
print(ans)
# 1の間、繰り返す
while 1 :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n==0 :
    # 繰り返すのを中断する
    break
  # nの8進文字列の先頭2個を取り除いた部分の文字列をnとする
  n = str(oct(n)[2:])
  # n.translate(str.maketrans('4567','5789'))をnとする
  n = n.translate(str.maketrans('4567','5789'))
  # nを出力する
  print(n)
# 関数fを[#FuncParam [#ParamDecl name: [#Name 'h']][#ParamDecl name: [#Name 'w']]]のパラメータを持つように定義する
def f (h,w) :
  # hにhを掛けた値にwにwを掛けた値を加えた値をsとする
  s = h*h+w*w
  # ([[#Name 'h'], [#Int '1']],)
  [[#Name 'h'], [#Int '1']]
  # 1の間、繰り返す
  while 1 :
    # hにhを掛けた値がsより小さい間、繰り返す
    while h*h<s :
      # hに1を加えた値をwとする
      w = h+1
      # {{hにhを掛けた値}}に{{wにwを掛けた値}}を加えた値がs以下の間、繰り返す
      while h*h+w*w<=s :
        # {{hにhを掛けた値}}に{{wにwを掛けた値}}を加えた値がsのとき、
        if h*h+w*w==s :
          # hとwを出力する
          print(h,w)
          # 関数処理を中断する
          return 
        # ([[#Name 'w'], [#Int '1']],)
        [[#Name 'w'], [#Int '1']]
      # ([[#Name 'h'], [#Int '1']],)
      [[#Name 'h'], [#Int '1']]
    # ([[#Name 's'], [#Int '1']],)
    [[#Name 's'], [#Int '1']]
    # 1をhとする
    h = 1
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にhとwとする
  h,w = map(int,input().split())
  # hが0のとき、
  if h==0 :
    # 繰り返すのを中断する
    break
  # f(h,w)
  f(h,w)
Syntax Error ((unknown source):5:14+67)
    s=re.sub(u'[A-Za-z .]','',s)
              ^                 
# 入力された文字列をsとする
s = input()
# s.isalpha() or s.isdigit() 、またはs.islower() 、または{{sの全てが英大文字かどうか}}、または{{sの長さが6より小さいかどうか}}のとき'INVALID'、そうでなければ'VALID'を出力する
print('INVALID' if s.isalpha() or s.isdigit() or s.islower() or s.isupper() or len(s)<6 else 'VALID')
# (''、'Man'、'Oku'、'Cho'、'Kei'、'Gai'、'Jo'、'Jou'、'Ko'、'Kan'、'Sei'、'Sai'、'Gok'、'Ggs'、'Asg'、'Nyt'、'Fks'、'Mts')からなる列をsとする
s = ['','Man','Oku','Cho','Kei','Gai','Jo','Jou','Ko','Kan','Sei','Sai','Gok','Ggs','Asg','Nyt','Fks','Mts']
# 1の間、繰り返す
while 1 :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
  m,n = map(int,input().split())
  # mが0のとき、
  if m==0 :
    # 繰り返すのを中断する
    break
  # ''をaとする
  a = ''
  # '0からmのn乗の文字列の長さ未満までの4間隔の数列の各要素を順にiとして、繰り返す
  for i  in range(0,len(str(m**n)),4) :
    # mのn乗を(10のi乗)の組で割った商を10000で割った余りをbとする
    b = m**n//(10**i)%10000
    # bのとき、
    if b :
      # bの文字列にs({{iを4で割った商}})を加えた値にaを加えた値をaとする
      a = str(b)+s[i//4]+a
  # aを出力する
  print(a)
Syntax Error ((unknown source):13:23+329)
    print(eval(re.sub(r'(\d+)',r'c(\1)',input()[:-1])))
                       ^                               
# '0から入力された文字列の整数値未満までの数列の各要素を順に_として、繰り返す
for _  in range(int(input())) :
  # 入力された文字列をsとする
  s = input()
  # '1から27未満までの2間隔の数列の各要素を順にiとして、繰り返す
  for i  in range(1,27,2) :
    # '0から27未満までの数列の各要素を順にjとして、繰り返す
    for j  in range(27) :
      # 空列をaとする
      a = []
      # '0からsの長さ未満までの数列の各要素を順にkとして、繰り返す
      for k  in range(len(s)) :
        # s(k)の全てが英小文字のとき、
        if s[k].islower() :
          # ([[#Name 'a'], [#ApplyExpr name: [#Name 'chr']params: [#Arguments [#Infix left: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Tuple [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 's']index: [#Name 'k']]]]name: [#Name '-']right: [#Int '97']]]name: [#Name '*']right: [#Name 'i']]name: [#Name '+']right: [#Name 'j']]]name: [#Name '%']right: [#Int '26']]name: [#Name '+']right: [#Int '97']]]]],)
          [[#Name 'a'], [#ApplyExpr name: [#Name 'chr']params: [#Arguments [#Infix left: [#Infix left: [#Tuple [#Infix left: [#Infix left: [#Tuple [#Infix left: [#ApplyExpr name: [#Name 'ord']params: [#Arguments [#IndexExpr recv: [#Name 's']index: [#Name 'k']]]]name: [#Name '-']right: [#Int '97']]]name: [#Name '*']right: [#Name 'i']]name: [#Name '+']right: [#Name 'j']]]name: [#Name '%']right: [#Int '26']]name: [#Name '+']right: [#Int '97']]]]]
        # ()
        else :[#Else [#Block [#SelfAssignment left: [#Name 'a']name: [# '+=']right: [#IndexExpr recv: [#Name 's']index: [#Name 'k']]]]]
      # aを文字列''で連結した文字列をaとする
      a = ''.join(a)
      # 'this'がaに含まれ、または'that'がaに含まれるとき、
      if 'this' in a or 'that' in a :
        # aを出力する
        print(a)
        # 繰り返すのを中断する
        break
# 1の間、繰り返す
while 1 :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]except: [# [#Except body: [#Block [#Break 'break']]]]]
  # 0、''、1をi、a、nとする
  i,a,n = 0,'',1
  # sの各要素を順にiとして、繰り返す
  for i  in s :
    # nが0のとき、
    if n==0 :
      # iの整数値をnとする
      n = int(i)
    # ("iが'@'の",)
    elif i=='@' :
      # 0をnとする
      n = 0
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'a']name: [# '+=']right: [#Infix left: [#Name 'i']name: [#Name '*']right: [#Name 'n']]][#VarDecl name: [#Name 'n']expr: [#Int '1']]]]
  # aを出力する
  print(a)
# '0から入力された文字列の整数値未満までの数列の各要素を順に_として、繰り返す
for _  in range(int(input())) :
  # 0をcをbとするとするをaとする
  a = b=c=0
  # map(整数,入力された文字列を空白で分割した列)の各要素を順にxとして、繰り返す
  for x  in map(int,input().split()) :
    # xがbより大きいとき、
    if x>b :
      # xをbとする
      b = x
    # ('xがcより大きい',)
    elif x>c :
      # xをcとする
      c = x
    # ()
    else :[#Else [#Block [#VarDecl name: [#Name 'a']expr: [#Int '1']]]]
  # ('YES'と'NO')からなる列(a)を出力する
  print(['YES','NO'][a])
# -1e11と1e11をaとbとする
a,b = -1e11,1e11
# '0から入力された文字列の整数値未満までの数列の各要素を順に_として、繰り返す
for _  in range(int(input())) :
  # 入力された文字列の整数値をcとする
  c = int(input())
  # aとcからbを引いた値の最大値とbとcの最小値をaとbとする
  a,b = max(a,c-b),min(b,c)
# aを出力する
print(a)
# '入力された文字列を空白で分割した列のリストをsとする
s = list(input().split())
# 空列をaとする
a = []
# sの各要素を順にxとして、繰り返す
for x  in s :
  # xが('+'、'-'、'*')からなる列に含まれるとき、
  if x in ['+','-','*'] :
    # a.pop()の文字列とa.pop()の文字列をcとbとする
    c,b = str(a.pop()),str(a.pop())
    # ([[#Name 'b'], [#Infix left: [#Name 'x']name: [#Name '+']right: [#Name 'c']]],)
    [[#Name 'b'], [#Infix left: [#Name 'x']name: [#Name '+']right: [#Name 'c']]]
    # ([[#Name 'a'], [#List [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'eval']params: [#Arguments [#Name 'b']]]]]]],)
    [[#Name 'a'], [#List [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'eval']params: [#Arguments [#Name 'b']]]]]]]
  # ()
  else :[#Else [#Block [#SelfAssignment left: [#Name 'a']name: [# '+=']right: [#List [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'x']]]]]]]
# a.pop()を出力する
print(a.pop())
# 入力された文字列
input()
# 入力された文字列を空白で分割した列をaとする
a = input().split()
# 入力された文字列
input()
# &(aの集合,{{input()を空白で分割した列}}の集合)の長さを出力する
print(len(set(a)&set(input().split())))
# 入力された文字列
input()
# 入力された文字列を空白で分割した列をaとする
a = input().split()
# 入力された文字列
input()
# &(aの集合,{{input()を空白で分割した列}}の集合)の長さを出力する
print(len(set(a)&set(input().split())))
Syntax Error ((unknown source):11:13+225)
print(len(b),*(d))
             ^    