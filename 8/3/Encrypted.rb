class Encrypted
  def initialize (text)
    @text = text
  end

  def decrypt(key)
    def decrypt_iter(my_key, text)
      if text.length >= 1
        if my_key.key?(text[0])
          my_key[text[0]] + decrypt_iter(my_key, text[1..-1])
        else
          text[0] + decrypt_iter(my_key, text[1..-1])
        end
      else
        ""
      end
    end
    MyPublic.new(decrypt_iter(key.invert, @text))
  end

  def to_s
    @text
  end
end

