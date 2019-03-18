using Android.App;
using Android.Widget;
using Android.OS;

using System.IO;
using Kompot.Engine;
using Android.Content;

namespace Kompot
{
    [Activity(Label = "Kompot", MainLauncher = true)]
    public class MainActivity : Activity
    {
        AnagramFinder asFuck = new AnagramFinder();

        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);

            
            Android.Content.Res.AssetManager assets = this.Assets;

            asFuck.LoadList(assets.Open("english-words.txt"), 5);
            
            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.Main);

            EditText wordList = FindViewById<EditText>(Resource.Id.wordList);
            EditText availableCharacters = FindViewById<EditText>(Resource.Id.input);
            TextView wordsFound = FindViewById<TextView>(Resource.Id.textWordCount);
            Button search = FindViewById<Button>(Resource.Id.searchButton);
            Button soduku = FindViewById<Button>(Resource.Id.sodSolver);

            
            search.Click += (sender, e) =>
            {
                wordList.Text = string.Empty;
                var matches = asFuck.Find(availableCharacters.Text);
                wordsFound.Text = string.Format("Found {0} words.", matches.Count);
                matches.ForEach(w => wordList.Text += string.Format("{0}\n",w));
            };

            soduku.Click += (sender, e) =>
            {
                var intent = new Intent(this, typeof(SentenceSolver));
                StartActivity(intent);
            };

            
        }
    }
}

