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
            MyDictionary<string,string> exDictionary = new MyDictionary<string, string>();
            exDictionary.Add("1", "one");
            Console.WriteLine($"1 is spelled {exDictionary.Search("1")} ");
            exDictionary.Add("2", "two");
            Console.WriteLine($"2 is spelled {exDictionary.Search("2")} ");
            exDictionary.Add("3", "three");
            exDictionary.Remove("1");
            exDictionary.Search("1");

            Console.ReadLine();
        }
    }

    public class MyPair<K, V>
    {
        public K key { get; set; }
        public V value { get; set; }
    }
    public class MyDictionary<K, V> where K : IComparable
    {

        private List<MyPair<K, V>> listOfPairs { get; set; }

        public MyDictionary()
        {
            listOfPairs = new List<MyPair<K, V>>();
            MyPair<K, V> x = new MyPair<K,V>();
            listOfPairs.Add(x);
        }
    
        public void Add(K key, V value)
        {
            MyPair<K, V> x = new MyPair<K, V>();
            x.key = key;
            x.value = value;
            listOfPairs.Add(x);
        }

        public V Search(K query)
        {
            foreach (MyPair<K,V> pair in listOfPairs)
            {
                if (query.CompareTo(pair.key)==0)
                {
                    return pair.value;
                }
            }
            Console.WriteLine("Not such key in dictionary");
            return listOfPairs[0].value;
        }
        public void Remove(K query)
        {
            bool isRemoved = false;
            foreach (MyPair<K, V> pair in listOfPairs.ToList())
            {
                if (query.CompareTo(pair.key) == 0)
                {
                    listOfPairs.Remove(pair);
                    isRemoved = true;
                }
            }

            if (isRemoved == false)
            {
                Console.WriteLine("Not such key in dictionary");
            }
        }
    }
}
