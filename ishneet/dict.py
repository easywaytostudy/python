>>> dic={"brand":"ford","model":"dezire"}
>>> x=dic.copy()
>>> print x
{'brand': 'ford', 'model': 'dezire'}
>>> x=('key1','key2','key3')
>>> y=0
>>> dict=dic.fromkeys(x,y)
>>> print dict
{'key3': 0, 'key2': 0, 'key1': 0}
>>> x=dic.get("brand")
>>> print x
ford
>>> dic.pop("model")
'dezire'
>>> dic.update({"color":"red"})
>>> print dic
{'color': 'red', 'brand': 'ford'}
>>> x=dic.values()
>>> print x
['red', 'ford']
>>> dic.setdefault("model","tyota")
'tyota'
>>> dic.popitem()
('color', 'red')
>>> 

