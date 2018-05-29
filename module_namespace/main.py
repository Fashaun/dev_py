import mod

print(mod.x)  # 10

mod.some()    # 10

other = mod.Other(20)
other.show()  # 20


## Python中一個可作為名稱空間的物件，都具有__dict__特性
## 模組也不例外。例如，若要存取上例中mod模組的x變數、some函式或Other類別

print(mod.__dict__['x'])            # 10

mod.__dict__['some']()              # 10

other = mod.__dict__['Other'](20)
other.show()                        # 20
