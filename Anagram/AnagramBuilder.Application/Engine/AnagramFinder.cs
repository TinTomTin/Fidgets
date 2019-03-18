using System.Collections.Generic;
using System.Linq;
using System.IO;

namespace Kompot.Engine
{
    public class AnagramFinder
    {
        private List<WordPrint> englishWords;

        public AnagramFinder()
        {
            englishWords = new List<WordPrint>();
        }

        public void LoadList(Stream inputStream, int minLength)
        {
            string line;
            StreamReader fileReader = new StreamReader(inputStream);
            while ((line = fileReader.ReadLine()) != null)
            {
                if (line.Length >= minLength && char.IsLower(line[0]))
                {
                    englishWords.Add(new WordPrint(line));
                }
            }
            fileReader.Close();
        }

        public void LoadList(string fileName, int minLength)
        {
            string line;

            StreamReader file = new StreamReader(fileName);
            while ((line = file.ReadLine()) != null)
            {
                if (line.Length >= minLength)
                {
                    englishWords.Add(new WordPrint(line));
                }
            }
            file.Close();
        }

        public List<string> Find(string availableChars)
        {
            WordPrint available = new WordPrint(availableChars);
            return englishWords.Where(wp => available.Print.Contains(wp.Print)).Select(w => w.Word).ToList();
        }
    }
}
