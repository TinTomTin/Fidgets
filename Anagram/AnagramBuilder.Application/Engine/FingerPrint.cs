using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kompot.Engine
{
   public class FingerPrint
   {
      public List<Occurence> Occurances;

      public FingerPrint(string word)
      {
         Occurances = word.ToLower().GroupBy(l => l).Select(g => new Occurence(g.Key, g.Count())).OrderBy(o => o.Chr).ToList();
      }

      public override string ToString()
      {
         return string.Join("", Occurances);
      }

      public int Find(char c)
      {
         var occ = Occurances.FirstOrDefault(o => o.Chr == c);
         return occ == null ? 0 : occ.Count;
      }

      public bool Contains(Occurence occ)
      {
         var charsHere = Occurances.FirstOrDefault(o => o.Chr == occ.Chr);
         return  charsHere == null ? false : ((charsHere.Count - occ.Count) >= 0) ? true: false;
      }

      public bool Contains(FingerPrint finger)
      {
         return finger.Occurances.Select(oc => this.Contains(oc)).All(e => e == true);
      }

   }
}
