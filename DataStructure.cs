using System;
namespace m
{
	public class program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("It's a dog!");
			Console.WriteLine("hello boy \n hello boy");
			Console.WriteLine(@"hello boy \n hello boy");

			string c1="jikexueyuan";
			string c2=c1[0].ToString();
			string c3=(string)c1[7].ToString();
			string c4=c1.Substring(0,5);
			Console.WriteLine(c1+"\n"+c2+"\n"+c3+"\n"+c4);
			Console.ReadLine();
		}
	}
}
