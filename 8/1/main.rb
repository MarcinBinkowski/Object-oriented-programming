class Integer
  def my_factors
    (1..self).select { |n| self % n  == 0}
  end
  def ack(num)
    def ack_iter(n, m)
      if n == 0
        m + 1
      elsif m == 0
        ack_iter(n-1, 1)
      else
        ack_iter(n-1, ack_iter(n, m-1))
      end
    end
    ack_iter(self, num)
  end
  def perfect_number
    self == (1..self/2).select{|n| self % n == 0}.sum
  end
  def verbally
    my_dict = {
        "-" => "minus",
        "0" => "zero",
        "1" => "one",
        "2" => "two",
      "3" => "three",
      "4" => "four",
      "5" => "five",
      "6" => "six",
      "7" => "seven",
      "8" => "eight",
      "9" => "nine",
    }
    def verbally_iter(my_dict, number)
      if number.to_i >= 10 or number.to_i <= -10
        my_dict[number[0]] + " " + verbally_iter(my_dict, number[1..-1])
      else
        my_dict[number[0]]
      end
    end
    verbally_iter(my_dict,self.to_s)
  end
end


print 10.my_factors
puts
puts 2.ack(1)
puts 5.perfect_number
puts 6.perfect_number
puts 123.verbally
puts -123.verbally


