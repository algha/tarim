def array2str(arr):
    arr = arr.replace('[', '.')
    arr = arr.replace(']', '')
    return arr

def str2arr(str):
    if '.' not in str:
        return str
    arr = str.split('.')
    _str = arr[0]
    for item in arr[1:]:
        _str = _str + '[{}]'.format(item)
    return _str

def isarr(data):
    if '.' in data:
        return True
    if '[' in data:
        return True
    return False

def getArrRoot(data):
    _data = array2str(data)
    _data = _data.split('.')
    return _data[0]

def getArrChild(data):
    _data = array2str(data)
    root = getArrRoot(data)
    replacement = '{}.'.format(root)
    return _data.replace(replacement,'')
