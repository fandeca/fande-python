# Python常用操作

## 1、center 在前后插入想要的str

```python
>>> s = 'name'
>>> print (s.center(20,'-'))
--------name--------

```

## 2、count 计算字符串中存在几个字符

```python
>>> s = 'name fande'
>>> print (s.count('n')) #不加索引范围默认是全局搜索
2
>>>
>>> print (s.count('e',0,4)) #指定要取值的范围根据索引进行操作 
1
>>>

```

## 3、endswith 判断字符中以什么结尾，正确返回True反则False

```python
s = 'name fande'
>>> print (s.endswith('e'))
True
>>> print (s.endswith('d')) 
False
>>>

```

## 4、startswith 判断字符中以什么开头，正确返回True反则False

```python
s = 'name fande'
>>> print (s.endswith('e'))
True
>>> print (s.endswith('d')) 
False
>>>

```

## 5、find 查找字符串中是否存在该字符，查询正确返回该字符串的索引值，反则，返回-1

```python
>>> name = 'fand 范登军'
>>> print (name.find('军'))  
7
>>> print (name.find('i'))  
-1
>>>

```

## 6、isdigit 判断是否是整数，是整数返回Ture反则是False

```python
>>> s = 'fande ' 
>>> print (s.isdigit())
False
>>> print ("22".isdigit())
True
>>>
>>> s= "222" 
>>> print (s.isdigit())
True
>>>

```

## 7、join 连接符 join用法 “” 引号中是设置连接符

```python
>>> name = 'fande','echo','zhudi'
>>> print ("".join(name))
fandeechozhudi
>>> print ("-".join(name)) 
fande-echo-zhudi
>>>
```

## 8、replace 替换字符串

```python
>>> a = "aaaaa"
>>> print (a.replace('a','m',1))
maaaa
>>>
>>> a = 'name'
>>> print (a.replace('name','fande'))
fande
>>> print (a.replace('n','q'))        
qame
>>>
>>> a = "aaaaa"
>>> print (a.replace('a','m',1))#可以指定你想要替换的字符串次数
maaaa
>>>

```

## 9、split 讲字符串转换为列表的形式，以空格区分

```python
>>> name = "fande name zudi "
>>> print (name.split())
['fande', 'name', 'zudi']
>>>

```

