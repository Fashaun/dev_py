
## 基本原理
import會在sys.path中尋找.py或已編譯的.pyc，如果.py尚未編譯則編譯為.pyc

而後載入執行一次，再次import同一個模組並不會再執行一次模組，如果找到.py與.pyc，而.pyc的版本並沒有比.py舊，則略過編譯直接執行

如果僅找到.pyc而沒有找到.py，也會直接執行。

## 進階想法
Python的import是執行時期的運算，

- import某個模組，就會執行該模組中定義的內容，被import的模組名稱會成為目前模組的變數
- 而被import的模組中的變數，就是以被import模組名稱為名稱空間。

### import

- import 兩次不會重新執行 module
- 只會設回與被匯入模組的同名變數 (import/main.py)

### import as

```
import some as other
print(other.name)   # Justin
```

import as 改變的是被匯入模組在當前模組的名稱，而不是 sys.modules 中的名稱，
以上例來說，sys.modules中的名稱仍然是some。上例比較像是：
```
import some
other = some
del some
print(other.name)
```

### from import

### from import *
- 會將被匯入模組中所有變數，在當前模組中都建立相同的名稱。
- 有些變數，不想被```from import *``` 建立同名變數, 有兩種做法
    - 可以用底線作為變數開頭
    - ```__all__ = ['x', 'some'] #x, some 為開放 from import * 使用的變數／函數``` 

### Check how many module you import

```
import sys
sys.modules.keys()
```

### 如何解決同名稱的模組名稱衝突問題

https://openhome.cc/Gossip/Python/ImportPackage.html

### Module 相容性的相關問題

Python是個不斷演進的語言，有些新語法或功能會不相容於舊版本Python，
甚至破壞舊版本Python原本的功能，如果你想要體驗一下將來版本可能有的新語法或功能，

可以透過__future__模組。例如在 Python 2.6 中，print是個陳述句

在Python 3中，print是個函式，若要在Python 2.6中使用Python 3中的print函式，則可以：

```
from __future__ import print_function
```
