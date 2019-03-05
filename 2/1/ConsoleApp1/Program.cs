using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {

        static void Main(string[] args)
        {
            RandomWordStream newRandomWordStream = new RandomWordStream();
            for (int i = 0; i < 12; i++)
                Console.WriteLine(newRandomWordStream.Next());
            Console.ReadLine();
        }
    }
    class IntStream
    {
        protected int nextNumber = -1;

        public virtual int Next()
        {
            if (Eos() == true)
            {
                return -1;
            }
            nextNumber++;
            return nextNumber;
        }

        public bool Eos()
        {
            if (nextNumber >= int.MaxValue)
            {
                return true;
            }
            return false;
        }

        public void Reset()
        {
            nextNumber = -1;
        }
    }

    class PrimeStream : IntStream
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

        public override int Next()
        {
            nextNumber++;
            while (IsPrime(nextNumber) == false)
                nextNumber++;
            if (Eos() == true)
                return -1;
            else 
                return nextNumber;
        }
    }

    class RandomStream : IntStream
    {
        Random randomNumber = new Random();

        public override int Next()
        {
            return randomNumber.Next();
        }
    }

    class RandomWordStream : PrimeStream
    {
        private static string chars = "$%#@!*abcdefghijklmnopqrstuvwxyz1234567890?;:ABCDEFGHIJKLMNOPQRSTUVWXYZ^&";
        RandomStream randInt = new RandomStream();

        public new string Next()
        {
            string text = "";
            base.Next();
            int temp = nextNumber;
            while (temp > 0)
            {
                int newRand = randInt.Next();
                text = text + chars[newRand % chars.Length];
                temp--;
            }
            return text;
        }
    }
}
