# python字符串replace替换无效

## 背景 

今天想把一个列表中符合条件的元素中 替换部分字符串， 发现怎么替换，改元素还是没有改变，本以为是内存引用的问题后来发现并不然。

## 经查阅解决

在Python中字符串是immutable对象，是不可变对象。

所以string使用replace需要重新赋值，生成一个新的对象。

```
str_a = 'hello world'
#replace 其实创建了新的字符串对象，需要重新引用这个字符串
str_a = str_a.replace('*****')
```

之前没有重新引用，导致该变量 指向的是 以前的对象，实则已经发生变化，只是没有重新引用而已。

# 装饰器示例

## 类装饰

```python
class RPAUniTutil:
    def __init__(self, timeInterval):
        self.timeInterval = timeInterval
        print("进入装饰器")

    def __call__(self, func):
        print("开始执行")
        print(self.timeInterval)
        def wrapper(*args, **kwargs):
            print("开始执行")
            res = func(*args, **kwargs)
            print("装饰器内的结果", res)
            return res
        return warpper
        
@RPAUniTutil("hahhh")
def test(t):
    print(t)
    return t + 10
```

