require 'squid'

class MyFunction

  def initialize (&block)
    @function = block
  end

  def value(x)
    @function.call(x)
  end

  def derivative(x) #pochodna
    h = 0.000000001
    (value(x + h) - value(x)) / h
  end

  def zeros(a, b, e)

    precision = e.to_s.length
    arr = []
    i = a
    while (i <= b)
      if @function.call(i).round(10) == 0.0
        arr.push(i)
      end
      i = i + e
      i = i.round(precision)
    end
    if arr.empty?
      nil
    else
      arr
    end
  end


  def integral(x, y)
    area = 0.0
    n = 10000
    z = (y - x)/n.to_f
    n.times{|a| area += z * value( x + a * z)}
    area
  end

  def chart(start_point, end_point, n)
    jump = (end_point - start_point).to_f / n
    points = Hash.new
    i = 0
    while i <= n
      points[start_point.to_f+(i*jump).round(2)] = value(start_point.to_f+(i*jump)).round(2)
      i += 1
    end
    points
  end
end

f = MyFunction.new{|x| x * x }

puts f.value(10)
puts f.derivative(4)
puts f.integral(0, 100)
print f.zeros(-10, 10, 0.001)

data = {}
data['value'] = f.chart(-10,10,10)
Prawn::Document.generate 'chart.pdf' do
  chart data, type: :point
end