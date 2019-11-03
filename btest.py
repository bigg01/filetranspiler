import base64

data = "abc123!?$*&()'-=@~"

def encodeB64(data):
  # URL and Filename Safe Base64 Encoding
  urlSafeEncodedBytes = base64.urlsafe_b64encode(data.encode("utf-8"))
  urlSafeEncodedStr = str(urlSafeEncodedBytes, "utf-8")
  #print(urlSafeEncodedStr)
  return urlSafeEncodedStr

def decodeB64(data):
  decodedBytes = base64.urlsafe_b64decode(data)
  decodedStr = str(decodedBytes, "utf-8")
  return decodedStr

def dump():
  return {'contents': {
                'source': 'data:text/plain;charset=utf-8;base64,{}'.format(encodeB64(data))
            }}

#print(encodeB64(data))
print(dump())
#print(decodeB64(encodeB64(data)))
