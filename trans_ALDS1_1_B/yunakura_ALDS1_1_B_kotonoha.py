# map(整数,入力された文字列を空白で分割した列)を展開し順にaとbとする
a , b  = map(int, input().split())
# mathモジュールを用いる
import math
# math.gcd(a, b)を出力する
print(math.gcd(a, b))