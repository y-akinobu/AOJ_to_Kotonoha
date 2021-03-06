
# 入力された文字列の整数値に32を掛けた値を出力する
print(int(input()) * 32)
# ({{input()の整数値から30を引いた値}})の組を2で割った商を出力する
print((int(input())-30)//2)
# map(整数,{{入力された文字列を空白で分割した列}})の総和を出力する
print(sum(map(int, input().split())))
# map(整数,{{input()を空白で分割した列}})の総和を2で割った商を出力する
print(sum(map(int,input().split()))//2)
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# {{aからbを引いた値}}の絶対値を出力する
print(abs(a - b))
# (("1 0 0", "Close")、("0 1 0", "Close")、("1 1 0", "Open")、("0 0 1", "Open")、("0 0 0", "Close"))からなる辞書をdicとする
dic = {"1 0 0":"Close", "0 1 0":"Close", "1 1 0":"Open",
       "0 0 1":"Open", "0 0 0":"Close"}
# dic(入力された文字列)を出力する
print(dic[input()])
# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a, b  = map(int, input().split())
# {{aにbを掛けた値}}を3.305785で割った値を出力する
print(a * b / 3.305785)
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをソートした列をlstとする
lst = sorted(list(map(int, input().split())))
# lst(0)がlst(1)、かつlst(2)がlst(3)のとき、
if lst[0] == lst[1] and lst[2] == lst[3] :
  # "yes"を出力する
  print("yes")
# ()
else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"no"']]]]]]
[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'ceil']]]
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、a、b、c、dとする
n, a, b, c, d  = map(int, input().split())
# {{ceil({{nをaで割った値}})にbを掛けた値}}と{{ceil({{nをcで割った値}})にdを掛けた値}}の最小値を出力する
print(min(ceil(n / a) * b, ceil(n / c) * d))
# map(整数,入力された文字列を空白で分割した列)を展開し順にa、b、cとする
a, b, c  = map(int, input().split())
# 0をansとする
ans = 0
# ([[#Name 'ans'], [#Infix left: [#Infix left: [#Name 'c']name: [#Name '//']right: [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]]name: [#Name '*']right: [#Int '7']]],)
[[#Name 'ans'], [#Infix left: [#Infix left: [#Name 'c']name: [#Name '//']right: [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]]name: [#Name '*']right: [#Int '7']]]
# ([[#Name 'c'], [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]],)
[[#Name 'c'], [#Tuple [#Infix left: [#Infix left: [#Name 'a']name: [#Name '*']right: [#Int '7']]name: [#Name '+']right: [#Name 'b']]]]
# ([[#Name 'ans'], [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Int '7'][#Infix left: [#Name 'c']name: [#Name '//']right: [#Name 'a']]]]],)
[[#Name 'ans'], [#ApplyExpr name: [#Name 'min']params: [#Arguments [#Int '7'][#Infix left: [#Name 'c']name: [#Name '//']right: [#Name 'a']]]]]
# cをaで割った余り、かつ{{cをaで割った商}}が7より小さいとき、
if c % a and c // a < 7 :
  # ([[#Name 'ans'], [#Int '1']],)
  [[#Name 'ans'], [#Int '1']]
# ansを出力する
print(ans)
# ((1, 6000)、(2, 4000)、(3, 3000)、(4, 2000))からなる辞書をdicとする
dic = {1:6000, 2:4000, 3:3000, 4:2000}
# '0から4未満までの数列の各要素を順に_として、繰り返す
for _  in range(4) :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にtとnとする
  t, n  = map(int, input().split())
  # dic(t)にnを掛けた値を出力する
  print(dic[t] * n)
# 関数put_difを[#FuncParam '()']のパラメータを持つように定義する
def put_dif () :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a, b  = map(int, input().split())
  # aからbを引いた値を出力する
  print(a - b)
# '0から7未満までの数列の各要素を順に_として、繰り返す
for _  in range(7) :
  # put_dif()
  put_dif()
# '0から9未満までの数列の各要素を順に_として、繰り返す
for _  in range(9) :
  # 入力された文字列を空白で分割した列を展開し順にname、v1、v2とする
  name, v1, v2  = input().split()
  # name、v1の整数値にv2の整数値を加えた値、{{v1の整数値に200を掛けた値}}に{{v2の整数値に300を掛けた値}}を加えた値を出力する
  print(name, int(v1) + int(v2), int(v1) * 200 + int(v2) * 300)
# {{{{'0から10未満までの数列}}の各要素を_とし、input()の整数値の列}}の総和を出力する
print(sum([int(input()) for _ in range(10)]))
# 入力された文字列
input()
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'lst']expr: [#ApplyExpr name: [#Name 'list']params: [#Arguments [#ApplyExpr name: [#Name 'map']params: [#Arguments [#Name 'int'][#MethodExpr recv: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]name: [#Name 'split']params: [#Arguments '']]]]]]][#Expression [#MethodExpr recv: [#Name 'lst']name: [#Name 'sort']params: [#Arguments '']]][#If cond: [#Infix left: [#Infix left: [#IndexExpr recv: [#Name 'lst']index: [#Int '2']]name: [#Name '**']right: [#Int '2']]name: [#Name '==']right: [#Infix left: [#Infix left: [#IndexExpr recv: [#Name 'lst']index: [#Int '1']]name: [#Name '**']right: [#Int '2']]name: [#Name '+']right: [#Infix left: [#IndexExpr recv: [#Name 'lst']index: [#Int '0']]name: [#Name '**']right: [#Int '2']]]]then: [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"YES"']]]]]else: [#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"NO"']]]]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
# 入力された文字列の整数値をnとする
n = int(input())
# 100000をaとする
a = 100000
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # aに1.05を掛けた値をaとする
  a = a * 1.05
  # 0をbとする
  b = 0
  # aを1000で割った余りのとき、
  if a % 1000 :
    # 1000をbとする
    b = 1000
  # {{{{aを1000で割った商}}に1000を掛けた値}}にbを加えた値の整数値をaとする
  a = int(a // 1000 * 1000 + b)
# aを出力する
print(a)
# {{{{'1から10未満までの数列}}の各要素をjとし、{{'1から10未満までの数列}}の列}}の各要素をiとし、{{{{str(i)+"x"+str(j)に"="を加えた値}}にi*jの文字列を加えた値}}を出力するの列
[print(str(i)+"x"+str(j)+"="+str(i*j))for i in range(1,10)for j in range(1,10)]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # {{{{[int(input()) for _ in range(n)]をソートした列}}の位置1から位置-1までの部分}}の総和を({{nから2を引いた値}})の組で割った商を出力する
  print(sum(sorted([int(input()) for _ in range(n)])[1:-1]) // (n - 2))
# {{range(5)の各要素を_とし、max(int(input()),40) の列}}の総和を5で割った商を出力する
print(sum([max(int(input()),40) for _ in range(5)]) // 5)
# {{{{[int(input()) for _ in range(4)]をソートした列}}の先頭を除いた部分}}の総和に入力された文字列の整数値と入力された文字列の整数値の最大値を加えた値を出力する
print(sum(sorted([int(input()) for _ in range(4)])[1:]) + max(int(input()), int(input())))
# 関数funcを[#FuncParam '()']のパラメータを持つように定義する
def func () :
  # 空列をlstとする
  lst = []
  # '0から10未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(10) :
    # lst.append(int(input()))
    lst.append(int(input()))
  # lst.sort()
  lst.sort()
  # lstの先頭-3個を取り除いた部分の総和を関数出力とする
  return sum(lst[-3:])
# func()とfunc()を出力する
print(func(),func())
# {{'0から30未満までの数列}}の各要素をiとし、{{iに1を加えた値}}の列をlstとする
lst = [i + 1 for i in range(30)]
# '0から28未満までの数列の各要素を順に_として、繰り返す
for _  in range(28) :
  # 0をlst[int(input()) - 1] にする
  lst[int(input()) - 1]  = 0
# lstの各要素を順にiとして、繰り返す
for i  in lst :
  # iのとき、
  if i :
    # iを出力する
    print(i)
# 関数mainを[#FuncParam '()']のパラメータを持つように定義する
def main () :
  # 真の間、繰り返す
  while True :
    # map(整数,入力された文字列を空白で分割した列)を展開し順にnとkとする
    n,k  = map(int,input().split())
    # nが0、かつkが0のとき、
    if n == 0 and k == 0 :
      # 繰り返すのを中断する
      break
    # 空列をlstとする
    lst = []
    # '0からn未満までの数列の各要素を順にiとして、繰り返す
    for i  in range(n) :
      # lst.append(int(input()))
      lst.append(int(input()))
    # 0をcountとする
    count = 0
    # '0からk未満までの数列の各要素を順にiとして、繰り返す
    for i  in range(k) :
      # ([[#Name 'count'], [#IndexExpr recv: [#Name 'lst']index: [#Name 'i']]],)
      [[#Name 'count'], [#IndexExpr recv: [#Name 'lst']index: [#Name 'i']]]
    # countをansとする
    ans = count
    # 'kからn未満までの数列の各要素を順にiとして、繰り返す
    for i  in range(k, n) :
      # ([[#Name 'count'], [#IndexExpr recv: [#Name 'lst']index: [#Name 'i']]],)
      [[#Name 'count'], [#IndexExpr recv: [#Name 'lst']index: [#Name 'i']]]
      # ([[#Name 'count'], [#IndexExpr recv: [#Name 'lst']index: [#Infix left: [#Name 'i']name: [#Name '-']right: [#Name 'k']]]],)
      [[#Name 'count'], [#IndexExpr recv: [#Name 'lst']index: [#Infix left: [#Name 'i']name: [#Name '-']right: [#Name 'k']]]]
      # ansとcountの最大値をansとする
      ans = max(ans,count)
    # ansを出力する
    print(ans)
# 識別子が'__main__'のとき、
if __name__ == '__main__' :
  # main()
  main()  
# {{'0から10未満までの数列}}の各要素を_とし、入力された文字列の整数値の列をmountainsとする
mountains = [int(input()) for _ in range(10)]
# mountains.sort(reverse=True)
mountains.sort(reverse=True)
# '0から3未満までの数列の各要素を順にiとして、繰り返す
for i  in range(3) :
  # mountains(i)を出力する
  print(mountains[i])
Syntax Error ((unknown source):9:10+107)
  except EOFError:
          ^       
[#FromDecl name: [#ModuleName 'collections']names: [# [#Name 'defaultdict']]]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # defaultdict(整数)をdicとする
  dic = defaultdict(int)
  # '0からn未満までの数列の各要素を順に_として、繰り返す
  for _  in range(n) :
    # ([[#IndexExpr recv: [#Name 'dic']index: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]], [#Int '1']],)
    [[#IndexExpr recv: [#Name 'dic']index: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]], [#Int '1']]
  # '0から10未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(10) :
    # dic(i)が0と等しくないとき、
    if dic[i] != 0 :
      # dic(i)に"*"を掛けた値を出力する
      print(dic[i] * "*")
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"-"']]]]]]
# 入力された文字列を英大文字に変換した文字列を出力する
print(input().upper())
[#FromDecl name: [#ModuleName 'collections']names: [# [#Name 'Counter']]]
# Counter('{{"KUPC"に入力された文字列を加えた値}}のリスト)をdとする
d = Counter(list("KUPC" + input()))
# d("K")、d("U")、d("P")、d("C")の最小値から1を引いた値を出力する
print(min(d["K"], d["U"], d["P"], d["C"]) - 1)
# 関数judgeを[#FuncParam [#ParamDecl name: [#Name 'r']]]のパラメータを持つように定義する
def judge (r) :
  # 0をpbとするをpaとする
  pa = pb = 0
  # rの先頭を除いた部分の各要素を順にcとして、繰り返す
  for c  in r[1:] :
    # cが"A"のとき、
    if c == "A" :
      # ([[#Name 'pa'], [#Int '1']],)
      [[#Name 'pa'], [#Int '1']]
    # ()
    else :[#Else [#Block [#SelfAssignment left: [#Name 'pb']name: [# '+=']right: [#Int '1']]]]
  # paがpbより小さいとき、
  if pa < pb :
    # paとpbに1を加えた値を出力する
    print(pa, pb + 1)
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Name 'pa']name: [#Name '+']right: [#Int '1']][#Name 'pb']]]]]]
# 真の間、繰り返す
while True :
  # 入力された文字列をr1とする
  r1 = input()
  # r1が"0"のとき、
  if r1 == "0" :
    # 繰り返すのを中断する
    break
  # judge(r1)
  judge(r1)
  # judge(入力された文字列)
  judge(input())
  # judge(入力された文字列)
  judge(input())
# 関数soinnsuubunnkaiを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def soinnsuubunnkai (n) :
  # 空列をretとする
  ret = []
  # '2からnの(1 / 2)の組乗の整数値に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(2, int(n ** (1 / 2)) + 1) :
    # iがnより大きいとき、
    if i > n :
      # 繰り返すのを中断する
      break
    # nをiで割った余りが0の間、繰り返す
    while n % i == 0 :
      # ([[#Name 'n'], [#Name 'i']],)
      [[#Name 'n'], [#Name 'i']]
      # ret.append(i)
      ret.append(i)
  # nが1と等しくないとき、
  if n != 1 :
    # ret.append(n)
    ret.append(n)
  # retを関数出力とする
  return ret
# 入力された文字列の整数値をnとする
n = int(input())
# nの文字列に": "を加えた値と((end, ""))からなる辞書を出力する
print(str(n)+": ",end="")
# *(soinnsuubunnkai(n))を出力する
print(*soinnsuubunnkai(n))
# 1000000007をMODとする
MOD = 1000000007
# map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
m, n  = map(int, input().split())
# mのn乗に対するMODの剰余を出力する
print(pow(m, n, MOD))
# 関数euclid_gcdを[#FuncParam [#ParamDecl name: [#Name 'v1']][#ParamDecl name: [#Name 'v2']][#ParamDecl name: [#Name 'counter']]]のパラメータを持つように定義する
def euclid_gcd (v1, v2, counter) :
  # v2が0のとき、
  if v2 == 0 :
    # (v1とcounter)の組を関数出力とする
    return (v1, counter)
  # ()
  else :[#Else [#Block [#Return expr: [#ApplyExpr name: [#Name 'euclid_gcd']params: [#Arguments [#Name 'v2'][#Infix left: [#Name 'v1']name: [#Name '%']right: [#Name 'v2']][#Infix left: [#Name 'counter']name: [#Name '+']right: [#Int '1']]]]]]]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
  a, b  = map(int, input().split())
  # aが0のとき、
  if a == 0 :
    # 繰り返すのを中断する
    break
  # aとbの最大値とaとbの最小値をaとbとする
  a, b  = max(a, b), min(a, b)
  # *(euclid_gcd(a,b,0))を出力する
  print(*euclid_gcd(a, b, 0))
[#FromDecl name: [#ModuleName 'math']names: [# [#Name 'gcd']]][#FromDecl name: [#ModuleName 'functools']names: [# [#Name 'reduce']]]
# 関数lcmを[#FuncParam [#ParamDecl name: [#Name 'x']][#ParamDecl name: [#Name 'y']]]のパラメータを持つように定義する
def lcm (x, y) :
  # xにyを掛けた値をgcd(x,y)で割った商を関数出力とする
  return x * y // gcd(x, y)
# 入力された文字列の整数値をnとする
n = int(input())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをalstとする
alst = list(map(int, input().split()))
# reduce(lcm,alst)を出力する
print(reduce(lcm, alst))
# 関数collを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def coll (n) :
  # 0をcntとする
  cnt = 0
  # nが1より大きい間、繰り返す
  while n > 1 :
    # nを2で割った余りのとき、
    if n % 2 :
      # nに3を掛けた値に1を加えた値をnとする
      n = n * 3 + 1
      # ([[#Name 'cnt'], [#Int '1']],)
      [[#Name 'cnt'], [#Int '1']]
    # nを2で割った余りが0の間、繰り返す
    while n % 2 == 0 :
      # nを2で割った商をnとする
      n = n // 2
      # ([[#Name 'cnt'], [#Int '1']],)
      [[#Name 'cnt'], [#Int '1']]
  # cntを関数出力とする
  return cnt
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # coll(n)を出力する
  print(coll(n))
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'd']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]][#VarDecl name: [#Name 's']expr: [#Int '0']][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Name 'd'][#Int '600'][#Name 'd']]]body: [#Block [#SelfAssignment left: [#Name 's']name: [# '+=']right: [#Infix left: [#Infix left: [#Name 'd']name: [#Name '*']right: [#Name 'i']]name: [#Name '*']right: [#Name 'i']]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 's']]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をqとする
  q = int(input())
  # qが-1のとき、
  if q == -1 :
    # 繰り返すのを中断する
    break
  # qを2で割った値をxとする
  x = q / 2
  # qに10の-5乗を掛けた値をendとする
  end = q * 10 ** -5
  # {{xの3乗からqを引いた値}}の絶対値がend以上の間、繰り返す
  while abs(x ** 3 - q) >= end :
    # ({{{{2にxの3乗を掛けた値}}にqを加えた値}})の組を({{3にxの2乗を掛けた値}})の組で割った値をxとする
    x = (2 * x ** 3 + q) / (3 * x ** 2)
  # xを出力する
  print(x)
# 入力された文字列をssとする
ss = input()
# ss内の","を" "で置き換えた文字列をssとする
ss = ss.replace(",", " ")
# ss内の"."を" "で置き換えた文字列をssとする
ss = ss.replace(".", " ")
# *({{{{ssを空白で分割した列}}の各要素をsとし、{{3 <= len(s) が6以下の}}ときのsの列}})を出力する
print(*[s for s in ss.split() if 3 <= len(s) <= 6])
# 入力された文字列の逆順を出力する
print(input()[::-1])
Syntax Error ((unknown source):16:12+251)
  print(*lst,sep="")
            ^       
Syntax Error ((unknown source):19:43+360)
    print(*[name.title() for name in names], sep="")
                                           ^        
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'ss']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]][#VarDecl name: [#Name 'ans1']expr: [#Infix left: [#Name 'ans2']name: [#Name '=']right: [#Int '0']]][#For each: [# [#Name 'i']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Infix left: [#ApplyExpr name: [#Name 'len']params: [#Arguments [#Name 'ss']]]name: [#Name '-']right: [#Int '2']]]]body: [#Block [#If cond: [#And left: [#And left: [#Infix left: [#IndexExpr recv: [#Name 'ss']index: [#Name 'i']]name: [#Name '==']right: [#QString "'J'"]]right: [#Infix left: [#IndexExpr recv: [#Name 'ss']index: [#Infix left: [#Name 'i']name: [#Name '+']right: [#Int '1']]]name: [#Name '==']right: [#QString "'O'"]]]right: [#Infix left: [#IndexExpr recv: [#Name 'ss']index: [#Infix left: [#Name 'i']name: [#Name '+']right: [#Int '2']]]name: [#Name '==']right: [#QString '"I"']]]then: [#Block [#SelfAssignment left: [#Name 'ans1']name: [# '+=']right: [#Int '1']]]elif: [# [#Elif cond: [#And left: [#And left: [#Infix left: [#IndexExpr recv: [#Name 'ss']index: [#Name 'i']]name: [#Name '==']right: [#QString "'I'"]]right: [#Infix left: [#IndexExpr recv: [#Name 'ss']index: [#Infix left: [#Name 'i']name: [#Name '+']right: [#Int '1']]]name: [#Name '==']right: [#QString "'O'"]]]right: [#Infix left: [#IndexExpr recv: [#Name 'ss']index: [#Infix left: [#Name 'i']name: [#Name '+']right: [#Int '2']]]name: [#Name '==']right: [#QString '"I"']]]then: [#Block [#SelfAssignment left: [#Name 'ans2']name: [# '+=']right: [#Int '1']]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'ans1']]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'ans2']]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
Syntax Error ((unknown source):8:10+90)
  except EOFError:
          ^       
# "A"の順序数をbaseとする
base = ord("A")
# 入力された文字列をsとする
s = input()
# ""をansとする
ans = ""
# sの各要素を順にiとして、繰り返す
for i  in s :
  # ansに文字コード{{{{(ord(i) - base - 3)の組を26で割った余り}}にbaseを加えた値}}の文字を加えた値をansとする
  ans = ans + chr((ord(i) - base - 3) % 26 + base)
# ansを出力する
print(ans)
[#FromDecl name: [#ModuleName 'collections']names: [# [#Name 'Counter']]]
# 入力された文字列を空白で分割した列をlstとする
lst = input().split()
# Counter(lst)をdicとする
dic = Counter(lst)
# dic.most_common(1)の最初値の最初値をmost_commonとする
most_common = dic.most_common(1)[0][0]
# {{lstの各要素をsとし、sの長さの列}}の最大値をlengthとする
length = max([len(s) for s in lst])
# lstの各要素を順にsとして、繰り返す
for s  in lst :
  # sの長さがlengthのとき、
  if len(s) == length :
    # sをlongestとする
    longest = s
# most_commonとlongestを出力する
print(most_common, longest)
# 入力された文字列をsとする
s = input()
# s内の"apple"を"X"で置き換えた文字列をsとする
s = s.replace("apple", "X")
# s内の"peach"を"apple"で置き換えた文字列をsとする
s = s.replace("peach", "apple")
# s内の"X"を"peach"で置き換えた文字列をsとする
s = s.replace("X", "peach")
# sを出力する
print(s)
# 0をansとする
ans = 0
# {{'0から10未満までの数列}}の各要素をiとし、iの文字列の列をnumsとする
nums = [str(i) for i in range(10)]
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 's']expr: [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]][#VarDecl name: [#Name 'acc']expr: [#Int '0']][#VarDecl name: [#Name 'last_ind']expr: [#Unary name: [#Name '-']expr: [#Int '1']]][#For each: [# [#Name 'i'][#Name 'c']]list: [#ApplyExpr name: [#Name 'enumerate']params: [#Arguments [#Name 's']]]body: [#Block [#If cond: [#Infix left: [#Name 'c']name: [#Name 'in']right: [#Name 'nums']]then: [#Block [#If cond: [#Infix left: [#Name 'last_ind']name: [#Name '==']right: [#Infix left: [#Name 'i']name: [#Name '-']right: [#Int '1']]]then: [#Block [#SelfAssignment left: [#Name 'acc']name: [# '*=']right: [#Int '10']][#SelfAssignment left: [#Name 'acc']name: [# '+=']right: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'c']]]]]else: [#Else [#Block [#VarDecl name: [#Name 'acc']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#Name 'c']]]]]]][#VarDecl name: [#Name 'last_ind']expr: [#Name 'i']]]else: [#Else [#Block [#SelfAssignment left: [#Name 'ans']name: [# '+=']right: [#Name 'acc']][#VarDecl name: [#Name 'acc']expr: [#Int '0']]]]]]else: [#Else [#Block [#SelfAssignment left: [#Name 'ans']name: [# '+=']right: [#Name 'acc']]]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
# ansを出力する
print(ans)
Syntax Error ((unknown source):18:10+286)
  except EOFError:
          ^       
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
  n, m  = map(int, input().split())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # {{'0からn未満までの数列}}の各要素を_とし、入力された文字列の整数値の列をalstとする
  alst = [int(input()) for _ in range(n)]
  # {{'0からm未満までの数列}}の各要素を_とし、入力された文字列の整数値の列をblstとする
  blst = [int(input()) for _ in range(m)]
  # alst.sort()
  alst.sort()
  # blst.sort()
  blst.sort()
  # alstの総和をsumaとする
  suma = sum(alst)
  # blstの総和をsumbとする
  sumb = sum(blst)
  # 関数searchを[#FuncParam '()']のパラメータを持つように定義する
  def search () :
    # alstの各要素を順にaとして、繰り返す
    for a  in alst :
      # blstの各要素を順にbとして、繰り返す
      for b  in blst :
        # ({{aからbを引いた値}})の組に2を掛けた値がsumaからsumbを引いた値のとき、
        if (a - b) * 2 == suma - sumb :
          # aとbを出力する
          print(a, b)
          # 関数処理を中断する
          return 
    # -1を出力する
    print(-1)
  # search()
  search()
# 関数mainを[#FuncParam '()']のパラメータを持つように定義する
def main () :
  # 真の間、繰り返す
  while True :
    # map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
    n, m  = map(int, input().split())
    # nが0のとき、
    if n == 0 :
      # 繰り返すのを中断する
      break
    # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをソートした列をitemsとする
    items = sorted(list(map(int, input().split())))
    # 0をansとする
    ans = 0
    # '0からnから1を引いた値未満までの数列の各要素を順にiとして、繰り返す
    for i  in range(n - 1) :
      # items(i)をp1とする
      p1 = items[i]
      # 'iに1を加えた値からn未満までの数列の各要素を順にjとして、繰り返す
      for j  in range(i + 1, n) :
        # p1にitems(j)を加えた値をp2とする
        p2 = p1 + items[j]
        # p2がmより大きいとき、
        if p2 > m :
          # 繰り返すのを中断する
          break
        # ansがp2より小さいとき、
        if ans < p2 :
          # p2をansとする
          ans = p2
    # ansが0と等しくないとき、
    if ans != 0 :
      # ansを出力する
      print(ans)
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#QString '"NONE"']]]]]]
# main()
main()
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをalstとする
  alst = list(map(int, input().split()))
  # alstの総和をnで割った値をaveとする
  ave = sum(alst) / n
  # {{alstの各要素をaとし、{{aがave以下かどうか}}の列}}の総和を出力する
  print(sum(a <= ave for a in alst))
# map(整数,入力された文字列を空白で分割した列)を展開し順にn、t、eとする
n, t, e  = map(int, input().split())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをxlstとする
xlst = list(map(int, input().split()))
#  xlstに番号を付けた列の各要素を順にiとxとして、繰り返す
for i, x  in enumerate(xlst) :
  # ({{{{tからeを引いた値}}から1を引いた値}})の組をxで割った商をaとする
  a = (t - e - 1) // x
  # ({{aに1を加えた値}})の組にxを掛けた値がtにeを加えた値以下のとき、
  if (a + 1) * x <= t + e :
    # iに1を加えた値を出力する
    print(i + 1)
    # 繰り返すのを中断する
    break
  # ()
  else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Unary name: [#Name '-']expr: [#Int '1']]]]]]]
# (("0", "0")、("1", "1")、("2", "2")、("3", "3")、("4", "5")、("5", "7")、("6", "8")、("7", "9"))からなる辞書をdicとする
dic = {"0":"0", "1":"1", "2":"2", "3":"3",
       "4":"5", "5":"7", "6":"8", "7":"9"}
# 関数transを[#FuncParam [#ParamDecl name: [#Name 'n']]]のパラメータを持つように定義する
def trans (n) :
  # nが0のとき、
  if n == 0 :
    # "0"を関数出力とする
    return "0"
  # ""をaccとする
  acc = ""
  # nの間、繰り返す
  while n :
    # ([[#Name 'acc'], [#IndexExpr recv: [#Name 'dic']index: [#ApplyExpr name: [#Name 'str']params: [#Arguments [#Infix left: [#Name 'n']name: [#Name '%']right: [#Int '8']]]]]],)
    [[#Name 'acc'], [#IndexExpr recv: [#Name 'dic']index: [#ApplyExpr name: [#Name 'str']params: [#Arguments [#Infix left: [#Name 'n']name: [#Name '%']right: [#Int '8']]]]]]
    # ([[#Name 'n'], [#Int '8']],)
    [[#Name 'n'], [#Int '8']]
  # accの逆順を関数出力とする
  return acc[::-1]
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をnとする
  n = int(input())
  # nが0のとき、
  if n == 0 :
    # 繰り返すのを中断する
    break
  # trans(n)を出力する
  print(trans(n))
# map(整数,入力された文字列を空白で分割した列)を展開し順にdとlとする
d, l  = map(int, input().split())
# {{dをlで割った商}}に{{dをlで割った余り}}を加えた値を出力する
print(d // l + d % l)
# 空列をlstとする
lst = []
# '1から151未満までの数列の各要素を順にhとして、繰り返す
for h  in range(1, 151) :
  # 'hに1を加えた値から151未満までの数列の各要素を順にwとして、繰り返す
  for w  in range(h + 1, 151) :
    # lst.append((h ** 2 + w ** 2, h, w))
    lst.append((h ** 2 + w ** 2, h, w))
# lst.sort()
lst.sort()
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にhとwとする
  h, w  = map(int, input().split())
  # hが0のとき、
  if h == 0 :
    # 繰り返すのを中断する
    break
  # lst.index((h ** 2 + w ** 2, h, w))をindとする
  ind = lst.index((h ** 2 + w ** 2, h, w))
  # *({{lst({{indに1を加えた値}})の先頭を除いた部分}})を出力する
  print(*lst[ind + 1][1:])
# 入力された文字列の整数値をmとする
m = int(input())
# '0からm未満までの数列の各要素を順に_として、繰り返す
for _  in range(m) :
  # 集合をssとする
  ss = set()
  # 入力された文字列をsとする
  s = input()
  # sの長さをlengthとする
  length = len(s)
  # '1からlength未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(1, length) :
    # sの位置先頭から位置iまでの部分をleftとする
    left = s[:i]
    # sの先頭i個を取り除いた部分をrightとする
    right = s[i:]
    # ([[#Name 'ss'], [#Set [#Infix left: [#Name 'left']name: [#Name '+']right: [#Name 'right']][#Infix left: [#Name 'left']name: [#Name '+']right: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]][#Infix left: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#Name 'right']][#Infix left: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]][#Infix left: [#Name 'right']name: [#Name '+']right: [#Name 'left']][#Infix left: [#Name 'right']name: [#Name '+']right: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]][#Infix left: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#Name 'left']][#Infix left: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]]]],)
    [[#Name 'ss'], [#Set [#Infix left: [#Name 'left']name: [#Name '+']right: [#Name 'right']][#Infix left: [#Name 'left']name: [#Name '+']right: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]][#Infix left: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#Name 'right']][#Infix left: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]][#Infix left: [#Name 'right']name: [#Name '+']right: [#Name 'left']][#Infix left: [#Name 'right']name: [#Name '+']right: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]][#Infix left: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#Name 'left']][#Infix left: [#SliceExpr recv: [#Name 'right']step: [#Unary name: [#Name '-']expr: [#Int '1']]]name: [#Name '+']right: [#SliceExpr recv: [#Name 'left']step: [#Unary name: [#Name '-']expr: [#Int '1']]]]]]
  # ssの長さを出力する
  print(len(ss))
Syntax Error ((unknown source):45:22+1408)
        print(*self.mp, sep="\n")
                      ^          
Syntax Error ((unknown source):27:-1+496)
  else:
       
Syntax Error ((unknown source):2:18+30)
if len(s) >= 6 and\
                  ^
# 関数is_collectを[#FuncParam [#ParamDecl name: [#Name 'fixed_number']]]のパラメータを持つように定義する
def is_collect (fixed_number) :
  # 0をscoreとする
  score = 0
  # '1から7未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(1, 7) :
    # ([[#Name 'score'], [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'fixed_number']index: [#Name 'i']]]]name: [#Name '*']right: [#Tuple [#Infix left: [#Name 'i']name: [#Name '+']right: [#Int '1']]]]],)
    [[#Name 'score'], [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'fixed_number']index: [#Name 'i']]]]name: [#Name '*']right: [#Tuple [#Infix left: [#Name 'i']name: [#Name '+']right: [#Int '1']]]]]
  # '7から12未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(7, 12) :
    # ([[#Name 'score'], [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'fixed_number']index: [#Name 'i']]]]name: [#Name '*']right: [#Tuple [#Infix left: [#Name 'i']name: [#Name '-']right: [#Int '5']]]]],)
    [[#Name 'score'], [#Infix left: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#IndexExpr recv: [#Name 'fixed_number']index: [#Name 'i']]]]name: [#Name '*']right: [#Tuple [#Infix left: [#Name 'i']name: [#Name '-']right: [#Int '5']]]]]
  # 11からscoreを11で割った余りを引いた値をlastとする
  last = 11 - score % 11
  # lastの文字列がfixed_number(0)、または({{lastが10以上}}、かつ{{fixed_number(0)が"0"かどうか}})の組のとき、
  if str(last) == fixed_number[0] or (last >= 10 and fixed_number[0] == "0") :
    # 真を関数出力とする
    return True
  # ()
  else :[#Else [#Block [#Return expr: [#False 'False']]]]
# 関数checkを[#FuncParam [#ParamDecl name: [#Name 's']]]のパラメータを持つように定義する
def check (s) :
  # s.index("?")をindexとする
  index = s.index("?")
  # 0をcntとする
  cnt = 0
  # '0から10未満までの数列の各要素を順にiとして、繰り返す
  for i  in range(10) :
    # iの文字列をcとする
    c = str(i)
    # {{sの位置先頭から位置indexまでの部分}}にcを加えた値にsの先頭{{indexに1を加えた値}}個を取り除いた部分を加えた値をfixed_numberとする
    fixed_number = s[:index] + c + s[index + 1:]
    # is_collect(fixed_number)のとき、
    if is_collect(fixed_number) :
      # ([[#Name 'cnt'], [#Int '1']],)
      [[#Name 'cnt'], [#Int '1']]
      # iをretとする
      ret = i
  # cntが1のとき、
  if cnt == 1 :
    # retを関数出力とする
    return ret
  # ()
  else :[#Else [#Block [#Return expr: [#Null 'None']]]]
# check(入力された文字列の逆順)をansとする
ans = check(input()[::-1])
# {{ansが未定値と等しくない}}ときans、そうでなければ"MULTIPLE"を出力する
print(ans if ans != None else "MULTIPLE")
# 10の10乗をINFとする
INF = 10 ** 10
# 空辞書をdicとする
dic = {}
# '0から10未満までの数列の各要素を順にiとして、繰り返す
for i  in range(10) :
  # iをdic[str(i)] にする
  dic[str(i)]  = i
# '"a"の順序数から"f"の順序数に1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(ord("a"), ord("f") + 1) :
  # iから"a"の順序数を引いた値に10を加えた値をdic[chr(i)] にする
  dic[chr(i)]  = i - ord("a") + 10
# 関数hex_to_decを[#FuncParam [#ParamDecl name: [#Name 's']]]のパラメータを持つように定義する
def hex_to_dec (s) :
  # dic(sの最初値)に16を掛けた値にdic(s(1))を加えた値を関数出力とする
  return dic[s[0]] * 16 + dic[s[1]]
# (("black"と'map(hex_to_dec,("00"、"00"、"00")からなる列)のリスト)の組、("blue"と'map(hex_to_dec,("00"、"00"、"ff")からなる列)のリスト)の組、("lime"と'map(hex_to_dec,("00"、"ff"、"00")からなる列)のリスト)の組、("aqua"と'map(hex_to_dec,("00"、"ff"、"ff")からなる列)のリスト)の組、("red"と'map(hex_to_dec,("ff"、"00"、"00")からなる列)のリスト)の組、("fuchsia"と'map(hex_to_dec,("ff"、"00"、"ff")からなる列)のリスト)の組、("yellow"と'map(hex_to_dec,("ff"、"ff"、"00")からなる列)のリスト)の組、("white"と'map(hex_to_dec,("ff"、"ff"、"ff")からなる列)のリスト)の組)からなる列をcolorsとする
colors = [("black",   list(map(hex_to_dec, ["00", "00", "00"]))),
          ("blue",    list(map(hex_to_dec, ["00", "00", "ff"]))),
          ("lime",    list(map(hex_to_dec, ["00", "ff", "00"]))),
          ("aqua",    list(map(hex_to_dec, ["00", "ff", "ff"]))),
          ("red",     list(map(hex_to_dec, ["ff", "00", "00"]))),
          ("fuchsia", list(map(hex_to_dec, ["ff", "00", "ff"]))),
          ("yellow",  list(map(hex_to_dec, ["ff", "ff", "00"]))),
          ("white",   list(map(hex_to_dec, ["ff", "ff", "ff"])))]
# 真の間、繰り返す
while True :
  # 入力された文字列をsとする
  s = input()
  # sが"0"のとき、
  if s == "0" :
    # 繰り返すのを中断する
    break
  # map(hex_to_dec,({{sの位置1から位置3までの部分}}、{{sの位置3から位置5までの部分}}、{{sの位置5から位置7までの部分}})からなる列)を展開し順にr、g、bとする
  r, g, b  = map(hex_to_dec, [s[1:3], s[3:5], s[5:7]])
  # "KUWA"をlowest_nameとする
  lowest_name = "KUWA"
  # INFをlowest_scoreとする
  lowest_score = INF
  # colorsの各要素を順にnameとrgbとして、繰り返す
  for name, rgb  in colors :
    # rgbを展開し順にrc、gc、bcとする
    rc, gc, bc  = rgb
    # ({{rからrcを引いた値}})の組の2乗に({{gからgcを引いた値}})の組の2乗を加えた値に({{bからbcを引いた値}})の組の2乗を加えた値をscoreとする
    score = (r - rc) ** 2 + (g - gc) ** 2 + (b - bc) ** 2
    # scoreがlowest_scoreより小さいとき、
    if score < lowest_score :
      # nameとscoreをlowest_nameとlowest_scoreとする
      lowest_name, lowest_score  = name, score
  # lowest_nameを出力する
  print(lowest_name)
# (""、"Man"、"Oku"、"Cho"、"Kei"、"Gai"、"Jo"、"Jou"、"Ko"、"Kan"、"Sei"、"Sai"、"Gok"、"Ggs"、"Asg"、"Nyt"、"Fks"、"Mts")からなる列をdicとする
dic = ["", "Man", "Oku", "Cho", "Kei", "Gai", "Jo", "Jou", "Ko", "Kan",
       "Sei", "Sai", "Gok", "Ggs", "Asg", "Nyt", "Fks", "Mts"]
# 真の間、繰り返す
while True :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にmとnとする
  m, n  = map(int, input().split())
  # mが0のとき、
  if m == 0 :
    # 繰り返すのを中断する
    break
  # mのn乗をxとする
  x = m ** n
  # 0をindとする
  ind = 0
  # ""をansとする
  ans = ""
  # xの間、繰り返す
  while x :
    # xを10000で割った余りのとき、
    if x % 10000 :
      # {{xを10000で割った余り}}の文字列にdic(ind)を加えた値にansを加えた値をansとする
      ans = str(x % 10000) + dic[ind] + ans
    # ([[#Name 'x'], [#Int '10000']],)
    [[#Name 'x'], [#Int '10000']]
    # ([[#Name 'ind'], [#Int '1']],)
    [[#Name 'ind'], [#Int '1']]
  # ansを出力する
  print(ans)
# "a"の順序数をbaseとする
base = ord("a")
# {{'1から26未満までの2間隔の数列}}の各要素をiとし、{{iを13で割った余りの}}ときのiの列をalstとする
alst = [i for i in range(1, 26, 2) if i % 13]
# 関数restoreを[#FuncParam [#ParamDecl name: [#Name 's']]]のパラメータを持つように定義する
def restore (s) :
  # alstの各要素を順にaとして、繰り返す
  for a  in alst :
    # '0から26未満までの数列の各要素を順にbとして、繰り返す
    for b  in range(26) :
      # ({{{{xが" "と等しくない}}とき文字コード{{(a * (ord(x) - base) + b) % 26 にbaseを加えた値}}の文字、そうでなければ{{sの各要素をxとし、" "の列}}}})からなる列を文字列""で連結した文字列をnewとする
      new = "".join([chr((a * (ord(x) - base) + b) % 26 + base) if x != " " else " " for x in s])
      # "that"がnewに含まれ、または"this"がnewに含まれるとき、
      if "that" in new or "this" in new :
        # newを関数出力とする
        return new
# 入力された文字列の整数値をnとする
n = int(input())
# '0からn未満までの数列の各要素を順に_として、繰り返す
for _  in range(n) :
  # restore(入力された文字列)を出力する
  print(restore(input()))
Syntax Error ((unknown source):18:10+267)
  except EOFError:
          ^       
# map(整数,入力された文字列を空白で分割した列)を展開し順にh、a、bとする
h, a, b  = map(int, input().split())
# 0をansとする
ans = 0
# 'aからbに1を加えた値未満までの数列の各要素を順にiとして、繰り返す
for i  in range(a, b + 1) :
  # hをiで割った余りが0のとき、
  if h % i == 0 :
    # ([[#Name 'ans'], [#Int '1']],)
    [[#Name 'ans'], [#Int '1']]
# ansを出力する
print(ans)
Syntax Error ((unknown source):4:-1+34)


# 関数mainを[#FuncParam '()']のパラメータを持つように定義する
def main () :
  # 真の間、繰り返す
  while True :
    # 入力された文字列の整数値をnとする
    n = int(input())
    # nが0のとき、
    if n == 0 :
      # 繰り返すのを中断する
      break
    # 'map(整数,{{入力された文字列を空白で分割した列}})のリストをalstとする
    alst = list(map(int, input().split()))
    # alstの総和をsとする
    s = sum(alst)
    # alstの各要素をaとし、{{aに2を掛けた値}}の列をalstとする
    alst = [a * 2 for a in alst]
    # (-s)からなる列をlstとする
    lst = [-s]
    # alstの各要素を順にaとして、繰り返す
    for a  in alst :
      # lst.extend([i + a for i in lst])
      lst.extend([i + a for i in lst])
    # map(abs,lst)の最小値を出力する
    print(min(map(abs, lst)))
# main()
main()
# 真の間、繰り返す
while True :[#Try body: [#Block [#VarDecl name: [#Name 'n']expr: [#ApplyExpr name: [#Name 'int']params: [#Arguments [#ApplyExpr name: [#Name 'input']params: [#Arguments '']]]]][#VarDecl name: [#Name 'count']expr: [#Int '0']][#For each: [# [#Name 'a']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#For each: [# [#Name 'b']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#For each: [# [#Name 'c']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#For each: [# [#Name 'd']]list: [#ApplyExpr name: [#Name 'range']params: [#Arguments [#Int '10']]]body: [#Block [#If cond: [#Infix left: [#Infix left: [#Infix left: [#Infix left: [#Name 'a']name: [#Name '+']right: [#Name 'b']]name: [#Name '+']right: [#Name 'c']]name: [#Name '+']right: [#Name 'd']]name: [#Name '==']right: [#Name 'n']]then: [#Block [#SelfAssignment left: [#Name 'count']name: [# '+=']right: [#Int '1']]]]]]]]]]]][#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Name 'count']]]]]except: [# [#Except cond: [#Name 'EOFError']body: [#Block [#Break 'break']]]]]
Syntax Error ((unknown source):15:10+267)
  except EOFError:
          ^       
Syntax Error ((unknown source):31:14+589)
        elif score == last_score:
              ^                  
# 10の20乗をINFとする
INF = 10 ** 20
# map(整数,入力された文字列を空白で分割した列)を展開し順にnとmとする
n, m  = map(int, input().split())
# 'map(整数,{{入力された文字列を空白で分割した列}})のリストをc_lstとする
c_lst = list(map(int, input().split()))
# {{'0から{{nに1を加えた値}}未満までの数列}}の各要素を_とし、INFの列をdpとする
dp = [INF for _ in range(n + 1)]
# 0をdp[0] にする
dp[0]  = 0
# c_lstの各要素を順にcoinとして、繰り返す
for coin  in c_lst :
  # 'coinからnに1を加えた値未満までの数列の各要素を順にpriceとして、繰り返す
  for price  in range(coin, n + 1) :
    # dp(price)とdp({{priceからcoinを引いた値}})に1を加えた値の最小値をdp[price] にする
    dp[price]  = min(dp[price], dp[price - coin] + 1)
# dp(n)を出力する
print(dp[n])
# map(整数,入力された文字列を空白で分割した列)を展開し順にnとwとする
n, w  = map(int, input().split())
# 空列をvalueとする
value = []
# 空列をweightとする
weight = []
# '0からn未満までの数列の各要素を順に_として、繰り返す
for _  in range(n) :
  # map(整数,入力された文字列を空白で分割した列)を展開し順にviとwiとする
  vi, wi  = map(int, input().split())
  # value.append(vi)
  value.append(vi)
  # weight.append(wi)
  weight.append(wi)
# {{'0から{{wに1を加えた値}}未満までの数列}}の各要素を_とし、0の列をdpとする
dp = [0 for _ in range(w + 1)]
# '0からn未満までの数列の各要素を順にiとして、繰り返す
for i  in range(n) :
  # 'wからweight(i)から1を引いた値未満までの-1間隔の数列の各要素を順にjとして、繰り返す
  for j  in range(w, weight[i] - 1, -1) :
    # dp(j)とdp({{jからweight(i)を引いた値}})にvalue(i)を加えた値の最大値をdp[j] にする
    dp[j]  = max(dp[j], dp[j - weight[i]] + value[i])
# dp(w)を出力する
print(dp[w])
# 真の間、繰り返す
while True :
  # 入力された文字列の整数値をbとする
  b = int(input())
  # bが0のとき、
  if b == 0 :
    # 繰り返すのを中断する
    break
  # bに2を掛けた値をxとする
  x = b * 2
  # 'xの({{1を2で割った値}})の組乗の整数値から0未満までの-1間隔の数列の各要素を順にkとして、繰り返す
  for k  in range(int(x ** (1 / 2)), 0, -1) :
    # xをkで割った余りが0のとき、
    if x % k == 0 :
      # ({{{{-k に1を加えた値}}に(x // k)の組を加えた値}})の組を2で割った余りが0のとき、
      if (-k + 1 + (x // k)) % 2 == 0 :
        # ({{{{-kに1を加えた値}}に{{xをkで割った商}}を加えた値}})の組を2で割った商をaとする
        a = (-k + 1 + x // k) // 2
        # aが0より大きいとき、
        if a > 0 :
          # aとkを出力する
          print(a, k)
          # 繰り返すのを中断する
          break
# 関数mainを[#FuncParam '()']のパラメータを持つように定義する
def main () :
  # 真の間、繰り返す
  while True :
    # map(整数,入力された文字列を空白で分割した列)を展開し順にwとhとする
    w, h  = map(int, input().split())
    # wが0のとき、
    if w == 0 :
      # 繰り返すのを中断する
      break
    # {{'0からh未満までの数列}}の各要素を_とし、{{{{(-1)からなる列に'map(int, input().split())のリストを加えた値}}に(-1)からなる列を加えた値}}の列をmpとする
    mp = [[-1] + list(map(int, input().split())) + [-1] for _ in range(h)]
    # mp.insert(0, [-1] * (w + 2))
    mp.insert(0, [-1] * (w + 2))
    # mp.append([-1] * (w + 2))
    mp.append([-1] * (w + 2))
    # '1からhに1を加えた値未満までの数列の各要素を順にyとして、繰り返す
    for y  in range(1, h + 1) :
      # '1からwに1を加えた値未満までの数列の各要素を順にxとして、繰り返す
      for x  in range(1, w + 1) :
        # mp(y)(x)が2のとき、
        if mp[y][x] == 2 :
          # (xとy)の組をstartとする
          start = (x, y)
        # mp(y)(x)が3のとき、
        if mp[y][x] == 3 :
          # (xとy)の組をgoalとする
          goal = (x, y)
    # ((0と-1)の組、(0と1)の組、(-1と0)の組、(1と0)の組)の組をvecとする
    vec = ((0, -1), (0, 1), (-1, 0), (1, 0))
    # 関数searchを[#FuncParam [#ParamDecl name: [#Name 'now']][#ParamDecl name: [#Name 'goal']][#ParamDecl name: [#Name 'num']]]のパラメータを持つように定義する
    def search (now, goal, num) :
      # numが0以下のとき、
      if num <= 0 :
        # -1を関数出力とする
        return -1
      # nowを展開し順にbxとbyとする
      bx, by  = now
      # -1をretとする
      ret = -1
      # vecの各要素を順にdxとdyとして、繰り返す
      for dx, dy  in vec :
        # mp({{byにdyを加えた値}})({{bxにdxを加えた値}})が(-1と1)の組に含まれるとき、
        if mp[by + dy][bx + dx] in (-1, 1) :
          # 最初からもう一度、繰り返す
          continue
        # bxとbyをnxとnyとする
        nx, ny  = bx, by
        # not in(mp({{nyにdyを加えた値}})({{nxにdxを加えた値}}),(-1と1)の組)の間、繰り返す
        while mp[ny + dy][nx + dx] not in (-1, 1) :
          # ([[#Name 'nx'], [#Name 'dx']],)
          [[#Name 'nx'], [#Name 'dx']]
          # ([[#Name 'ny'], [#Name 'dy']],)
          [[#Name 'ny'], [#Name 'dy']]
          # (nxとny)の組がgoalのとき、
          if (nx, ny) == goal :
            # retとnumから1を引いた値の最大値をretとする
            ret = max(ret, num - 1)
            # 繰り返すのを中断する
            break
      # retを関数出力とする
      return ret
    # search(start,goal,10)をscoreとする
    score = search(start, goal, 10)
    # scoreが-1のとき、
    if score == -1 :
      # -1を出力する
      print(-1)
    # ()
    else :[#Else [#Block [#Expression [#ApplyExpr name: [#Name 'print']params: [#Arguments [#Infix left: [#Int '10']name: [#Name '-']right: [#Name 'score']]]]]]]
# main()
main()
Syntax Error ((unknown source):28:56+756)
        if not (nx, ny, new_direct) in dic or dic[nx, ny, new_direct] > total:
                                                        ^                     