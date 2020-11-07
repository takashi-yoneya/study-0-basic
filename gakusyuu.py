### Pythonの基本文法学習用

## 変数
def study1():
    name1="ぎゆう"
    name2="ねずこ"
    name3="ぜんいつ"

    print(name1 + "と" + name2 + "は仲間です")

## if文
def study2():
    # 条件分岐
    name1="ぎゆう"
    name2="むざん"

    if name1=="ぎゆう" and name2=="ねずこ":
        print(name1 + "と" + name2 + "は仲間です")
    else:
        print(name1 + "と" + name2 + "は仲間ではありません")

## for 文
def search_name(name,search_word):
    # 同じ処理の繰り返し    
    for n in name:
        if search_word == n:
            print(search_word + "はいます")
    
## 配列(List)
def get_list():
    name=["たんじろう","ぎゆう","ねずこ","むざん"]
    print(name)
    
    name.append("ぜんいつ")
    
    print(name)
    return name

## 実用的な関数
def study5():
    search_word="ぎゆう"
    name_list=get_list()
    #引数
    search_name(name_list,search_word)

study5()