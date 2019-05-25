### Inspecting re.compile()

```python
>>> import inspect
>>> 
>>> import inspect
>>> import re
>>> 
>>> source = inspect.getsource(re.compile)
>>> 
>>> print(source)
def compile(pattern, flags=0):
    "Compile a regular expression pattern, returning a pattern object."
    return _compile(pattern, flags)

>>> 
```