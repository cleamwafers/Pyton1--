#引数：関数に引き渡すデータのこと。
#商品の本体価格を渡すと、消費税計算を行い、消費税込みの金額がわかる関数(④関数も戻り値もある関数)
def postTaxPrice(price):
#def 関数名(引数1,引数２,・・・)：
    ans = price * 1.1
#関数で行う処理
    return ans
#return 戻り値

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")