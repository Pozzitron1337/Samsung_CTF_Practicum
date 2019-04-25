import base64

encoded='dGgxc19vbmVfd2FzX3ByZXR0eV9lYXN5'
flag=base64.b64decode(encoded).decode('utf-8')
print(flag)