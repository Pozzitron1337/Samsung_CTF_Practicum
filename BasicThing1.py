import hashlib
hashsum='fc5e038d38a57032085441e7fe7010b0'
flag='helloworld'
print(hashlib.md5(flag.encode('utf-8')).hexdigest())