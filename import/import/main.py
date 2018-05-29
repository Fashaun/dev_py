import some
print(some.name)  # Justin
del some
#print(some.name)  # NameError: name 'some' is not defined
import some # import again
print(some.name)  # Justin
