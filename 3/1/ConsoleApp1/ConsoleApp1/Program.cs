using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            MyList<int> myList = new MyList<int>();
            myList.AddFirst(1);
            myList.GetInfo();
            myList.IsEmpty();
            myList.AddFirst(2);
            myList.GetInfo();
            myList.AddFirst(3);
            myList.GetInfo();
            myList.AddLast(4);
            myList.GetInfo();
            myList.AddLast(5);
            myList.GetInfo();
            myList.RemoveFirst();
            myList.GetInfo();
            myList.RemoveLast();
            myList.GetInfo();
            myList.RemoveLast();
            myList.GetInfo();
            myList.RemoveFirst();
            myList.GetInfo();
            myList.RemoveFirst();
            myList.GetInfo();
            myList.AddFirst(1);
            myList.GetInfo();
            Console.ReadLine();
        }
    }

    public class Element<T>
    {

        public Element<T> next;
        public Element<T> prev;
        public T value { get; set; }

        public Element(T value)
        {
            this.value = value;
        }
    }

    public class MyList<T>
    {
        private Element<T> first;
        private Element<T> last;
        private int size;

        public MyList()
        {
            size = 0;
        }

        public void GetInfo()
        {
            Element<T> x = first;

            if (x != null)
            {
                Console.Write("[");
                Console.Write($"{x.value}, ");
                while (x.next != null)
                {
                    x = x.next;
                    Console.Write($"{x.value}, ");

                }
                Console.Write("]");
                Console.WriteLine();
            }
            else
            {
                Console.WriteLine("[]");
            }
 
        }

        public bool IsEmpty()
        {
            if (size == 0)
                return true;
            return false;
        }
        public void AddFirst(T newValue)
        {
            if (IsEmpty())
            {
                first = new Element<T>(newValue);
                last = first;
            }
            else
            {
                Element<T> newElement = new Element<T>(newValue);
                first.prev = newElement;
                newElement.next = first;
                first = newElement;
            }
            size++;
        }

        public void AddLast(T newValue)
        {
            if (last == null)
            {
                first = new Element<T>(newValue);
                last = first;
            }
            else
            {
                Element<T> newElement = new Element<T>(newValue);
                last.next = newElement;
                newElement.prev = last;
                last = newElement;
            }
            size++;
        }

        public void RemoveFirst()
        {
            if (size == 1)
            {
                first = null;
                last = null;
                size = 0;
            }
            else
            {
                Element<T> tempHead = first;
                first = tempHead.next;
                first.prev = null;
                size--;
            }
        }
        public void RemoveLast()
        {
            if (size == 1)
            {
                first = null;
                last = null;
                size = 0;
            }
            else
            {
                last = last.prev;
                last.next = null;
                size--;
            }
        }

    }
}
