import hashlib

obj = hashlib.md5()

obj.update("XuYao".encode("utf-8"))

ret = obj.hexdigest()

print(ret)
