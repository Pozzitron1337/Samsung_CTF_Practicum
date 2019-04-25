import urllib.parse
import base64

url_encode = '%4e%6a%45%32%5a%54%4d%77%4e%7a%51%32%4f%44%59%31%4e%7a%49%31%5a%6a%63%30%4e%6a%45%33%4d%7a%5a%69'
url_decoded=urllib.parse.unquote(url_encode)
print("Url decoded: ", url_decoded)
hex_value=base64.b64decode(url_decoded).decode('ascii')
print("Hex: ", hex_value)
flag = bytes.fromhex(hex_value).decode('ascii')
print(flag)
