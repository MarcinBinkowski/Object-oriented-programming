using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp2
{
    class Program
    {
        static void Main(string[] args)
        {
            LazyList list1 = new LazyList();
            list1.Element(10);
            foreach (int element in list1.numbers)
            {
                Console.WriteLine(element);
            }
            LazyPrime list2 = new LazyPrime();
            list2.Element(10);
            foreach (int element in list2.numbers)
            {
                Console.WriteLine(element);
            }
            Console.ReadKey();
        }
    }

    class LazyList
    {
        public List<int> numbers;
        protected Random randNumber = new Random();

        public int Size()
        {
            return numbers.Count;
        }


        public int Element(int i)
        {
            if (numbers == null)
            {
                numbers = new List<int>(i);
                AssignValues(i);
            }
            if (Size() < i-1)
            {
                AssignValues(i);
            }
            return numbers[i-1];
        }

        protected virtual void AssignValues(int i)
        {
            for (int size = Size(); size < i; size++)
            {
                int newElement = randNumber.Next(int.MinValue, int.MaxValue);
                numbers.Add(newElement);
            }
        }
    }

    class LazyPrime : LazyList
    {
        private bool IsPrime(int number)
        {
            if (number < 2)
                return false;
            for (int i = 2; i <= Math.Sqrt(number); i++)
            {
                if ((number % i) == 0)
                    return false;
            }
            return true;
        }

        private int NextPrime(int x)
        {
            while (x < int.MaxValue)
            {
                x++;
                if (IsPrime(x) == true)
                    return x;
            }

            return -1;
        }

        protected override void AssignValues(int i)
        {
            for (int size = Size(); size < i; size++)
            {
                if (size > 1)
                {
                    int newElement = NextPrime(numbers[size - 1]);
                    numbers.Add(newElement);
                }
                else if (numbers.Any() == false)
                {
                    numbers.Add(2);
                }
                else
                {
                    numbers.Add(3);
                }
            }
        }

    }
}
