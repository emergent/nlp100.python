s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
di = { s[0:1] if i in [0,4,5,6,7,8,14,15,18] else s[0:2] : i for i, s in enumerate(s.split(' ')) }
print(di)
