
namespace Kompot.Engine
{
   public class Occurence
   {
      public Occurence(char c, int count)
      {
         Chr = c;
         Count = count;
      }
      public char Chr { get; set; }
      public int Count { get; set; }

      public override string ToString()
      {
         return string.Format("{0}{1}", Chr, Count);
      }
   }
}
