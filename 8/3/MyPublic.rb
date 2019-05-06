class MyPublic
  def initialize (text)
    @text = text
  end

  def encrypt(key)
    def encrypt_iter(my_key, text)
      if text.length >= 1
        if my_key.key?(text[0])
          my_key[text[0]] + encrypt_iter(my_key, text[1..-1])
        else
          text[0] + encrypt_iter(my_key, text[1..-1])
        end
      else
        ""
      end
    end
    Encrypted.new(encrypt_iter(key, @text))
  end

  def to_s
    @text
  end
end

