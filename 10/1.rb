require "benchmark"

class Collection
  attr_accessor :array

  def initialize(array)
    @array = array
  end

  def swap(i, j)
    @array[i], @array[j] = @array[j], @array[i]
  end

  def length
    @array.length
  end

  def get(i)
    @array[i]
  end

end

class Sorting
  def self.bubble_sort(collection)
    n = collection.length
    swapped = true
    while swapped == true
      swapped = false
      (n-1).times do |i|
        if collection.get(i) > collection.get(i+1)
          collection.swap(i, i + 1)
          swapped = true
        end
      end
    end
  end

  def self.selection_sort(collection)
    n = collection.length
    for i in 0...n
      min=i
      for j in (i + 1)...n
        if collection.get(j) < collection.get(min)
          collection.swap(j, min)
        end
      end
    end
    collection
  end

end

a1 = [5,4,3,2,1]
a2 = [5,4,3,2,1]
a3 = (0...5000).to_a.reverse
a4 = (0...5000).to_a.reverse

Sorting.bubble_sort(Collection.new(a1))
print(a1.sort)
Sorting.selection_sort(Collection.new(a2))
print(a2.sort)
how_long = Benchmark.measure do
  Sorting.bubble_sort(Collection.new(a3))
end

how_long2 = Benchmark.measure do
  Sorting.selection_sort(Collection.new(a4))
end
puts
puts how_long
puts how_long2