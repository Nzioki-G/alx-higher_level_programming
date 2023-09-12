# Python - Input/Output
* open a file thus ```with open(file_name, file_mode, encoding) as my_file``` to have it close by default afterwards

* write to file: ```my_file.write(str)```

* read from file: ```my_file.read()``` reads entire file or specified size<br> ```my_file.readline()``` reads line by line

* to move the cursor in a file do ```my_file.seek(offse, whence)```
    ```
    >>> f = open('workfile', 'rb+')
    >>> f.write(b'0123456789abcdef')
    16
    >>> f.seek(5)      # Go to the 6th byte in the file
    5
    >>> f.read(1)
    b'5'
    >>> f.seek(-3, 2)  # Go to the 3rd byte before the end
    13
    >>> f.read(1)
    b'd'
    ```
    <br>

## JSON - JavaScript Object Notation
* JSON is a lightweight data interchange format
* Basic Usage:<br>
    * ```json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)```
     <br>Serialize an object as json formatted stream to fp

    * ```json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, xseparators=None, default=None, sort_keys=False, **kw)```
    <br>Serialize obj to json formatted string

    * ```json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)```
    <br>Deserialize fp (containig a json document) to a Python object

    * ```json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)```
    Deserialize s (json str/bytes/byte_array) to a Python object

* Simple JSON decoder: <br>


| JSON | Python |
| :--: | :----: |
| object | dict |
| array | list |
| string | str |
| number(int) | int |
| number(real) | float |
| true | True |
| false | False |
| null | None |

<br>

### References
<a href=https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects>All about Python File Handling</a>

<a href=https://docs.python.org/3/library/json.html>All about JSON</a>