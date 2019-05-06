require_relative  'MyPublic'
require_relative  'Encrypted'

a = MyPublic.new("marcin")
my_key = {"a" => "b",
          "b" => "a",
          "c" => "z",
          "m" => "x",
          "z" => "y",
          "i" => "n",
          "n" => "m"}

encrypted = a.encrypt(my_key)
puts encrypted
decrypted = encrypted.decrypt(my_key)
puts decrypted