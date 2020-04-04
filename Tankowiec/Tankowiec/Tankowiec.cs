using System;
using System.IO;
using System.Collections.Generic;

using System.Threading;

namespace FillMeUp
{
    //TODO: Get track listing of destination, and don't copy those files either during the session, so that all the music is new every time
    //TODO: Don't copy large (mix) mp3 files
    public class Tankowiec
    {
        private List<String> pCopiedFiles;
        private long pCopiedSize;
        private Random pGenerator;

        private CancellationTokenSource tokenSource;
        private CancellationToken token;

        private int consoleY;
        private ConsoleColor originalColor;

        public string SourceFolder { get; set; }
        public string DestinationFolder { get; set; }
        public long Size { get; set; }
        public int CopiedFiles { get { return pCopiedFiles.Count; } }

        public CancellationToken StopToken { get { return token; } }
        public CancellationTokenSource TokenSource { get { return tokenSource; } }


        public Tankowiec()
        {
            pCopiedFiles = new List<string>();
            pCopiedSize = 0;
            pGenerator = new Random();
            tokenSource = new CancellationTokenSource();
            token = tokenSource.Token;
            consoleY = Console.CursorTop;
            originalColor = Console.ForegroundColor;
        }


        public void FillErUp()
        {
            Console.WriteLine("Looking for music in {0}", SourceFolder);
            string[] files = Directory.GetFiles(SourceFolder, "*.mp3", SearchOption.AllDirectories);
           
            while (!token.IsCancellationRequested && pCopiedSize < Size)
            {
                int trackNumber = pGenerator.Next(files.Length - 1);
                string file = files[trackNumber];
                string fileName = Path.GetFileName(file);
                if (!pCopiedFiles.Contains(fileName))
                {
                    
                    long fileSize = new FileInfo(file).Length;
                    if (pCopiedSize + fileSize < Size)
                    {
                        string destinationFile = Path.Combine(DestinationFolder, fileName);
                        WriteStatusInfo(fileName, pCopiedSize);
                        File.Copy(file, Path.Combine(DestinationFolder, fileName), true);
                    }
                    pCopiedSize += fileSize;
                    pCopiedFiles.Add(fileName);
                }
            }

            Console.ForegroundColor = originalColor;
            if (!token.IsCancellationRequested) Console.WriteLine("\nRand to completion with no cancellation");
        }

        private void WriteStatusInfo(string fileName, long memCopied)
        {
            Console.ForegroundColor = Console.BackgroundColor;
            Console.SetCursorPosition(0, consoleY);
            Console.Write(new string(' ', Console.WindowWidth));
            Console.ForegroundColor = ConsoleColor.White;
            Console.SetCursorPosition(0, consoleY);
            Console.WriteLine("Copying: {0}", fileName);
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("Memory: {0:G} Mb of {1:G} Mb", (memCopied / 1048576), (Size / 1048576));
        }

    }
}
