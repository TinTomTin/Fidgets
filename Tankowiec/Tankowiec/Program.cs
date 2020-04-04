using System;
using System.Threading.Tasks;

using Mono.Options;

namespace FillMeUp
{
   class Program
   {
      static void Main(string[] args)
      {
         Tankowiec franek = new Tankowiec();
         Boolean showHelp = false;

         var p = new OptionSet() {
            { "s|source=", "Source folder of the music", v => franek.SourceFolder = v},
            { "d|destination=", "Where the player is at", v => franek.DestinationFolder = v},
            { "c|capacity=", "Size in Gb to upload", (double v) => franek.Size = (long)(v * 1024 * 1024 * 1024)},
            { "h|help","Show help", v => showHelp = v != null}
         };

         try
         {
            p.Parse(args);
            Console.WriteLine(showHelp);
         }
         catch (OptionException e)
         {
            Console.Write(String.Format("Tankowanie nocom nie wyszlo: {0}\n", e.Message));
            ShowHelp(p);
            return;
         }

         if(showHelp)
         {
            ShowHelp(p);
            return;
         }
         
         Console.WriteLine("Still in program, about to start task...");
         Task f = Task.Run(() => franek.FillErUp(), franek.StopToken);

         Console.ReadLine();
         franek.TokenSource.Cancel();
         Console.WriteLine("Tankowanie nocom skonczone: {0} skopiowane", franek.CopiedFiles);

      }

      private static void ShowHelp(OptionSet opts)
      {
         opts.WriteOptionDescriptions(Console.Out);
      }
   }
}
