import base64

data = "abc123!?$*&()'-=@~"

data2 = "bWFjaGluZV9yb2xle3JvbGU9IndvcmtlciJ9IDEK"

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

#ignition

# https://github.com/utilitywarehouse/on-prem-kube/blob/master/ignition/ic/worker0.ign

# terraform
#https://www.terraform.io/docs/providers/ignition/index.html

print(decodeB64(data2))
print(dump())
#print(decodeB64(encodeB64(data)))
