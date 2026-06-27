it = (len(x) for x in open('EffectivePython/myfile.txt'))
print(it)


roots = ((x * 0.5) for x in it)
print(roots)

# 唯一需要注意的是，生成器表达式返回的迭代器是有状态的，跑完一整轮之后，就不能继续使用了
# 生成器表达式用圆括号表示，可以嵌套
