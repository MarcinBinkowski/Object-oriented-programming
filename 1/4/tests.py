from main import encode, decode


print(encode('avasd asdas'))
print(decode(".- ...- .- ... -..  .- ... -.. .- ..."))

tadeusz = encode("Litwo Ojczyzno moja ty jestes jak zdrowie Ile cie trzeba cenic ten tylko sie dowie \
Kto cie stracil Dzis pieknosc twa w calej ozdobie Widze i opisuje bo tesknie po tobie")

print(decode(tadeusz))