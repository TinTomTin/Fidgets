

namespace Kompot.Engine
{
   public class WordPrint
   {
      public string Word;
      public FingerPrint Print;

      public WordPrint(string theWord)
      {
         Word = theWord;
         Print = new FingerPrint(theWord);
      }
   }
}
