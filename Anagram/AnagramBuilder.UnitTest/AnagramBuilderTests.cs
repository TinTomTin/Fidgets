using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

using Kompot.Engine;

namespace AnagramBuilder.UnitTest
{
   [TestClass]
   public class AnagramBuilderTests
   {
      [TestMethod]
      public void TestFingerprintConstruction()
      {
         var fingerPrint = new FingerPrint("Boobs");
         Assert.AreEqual("b2o2s1", fingerPrint.ToString());
      }

      [TestMethod]
      public void TestFindIfFound()
      {
         var count = new FingerPrint("Boobs").Find('o');
         Assert.AreEqual(2, count);
      }

      [TestMethod, Description("Test that contains fails if there are not enough characters")]
      public void TestContainsFalse()
      {
         var fingerPrint = new FingerPrint("Boobs");
         var occ = new Occurence('o', 3);
         Assert.AreEqual(false, fingerPrint.Contains(occ));
      }

      [TestMethod]
      public void TestContainsTrue()
      {
         var fingerPrint = new FingerPrint("Boobs");
         var occ = new Occurence('o', 2);
         Assert.AreEqual(true, fingerPrint.Contains(occ));
      }

      [TestMethod]
      public void TestContainsForNonExistant()
      {
         var fingerPrint = new FingerPrint("Boobs");
         var occ = new Occurence('v', 1);
         Assert.AreEqual(false, fingerPrint.Contains(occ));
      }

      [TestMethod, Description("Contains with letters left over")]
      public void TestContainsFP1()
      {
         var targetPrint = new FingerPrint("Boobs");
         var inputPrint = new FingerPrint("Bos");

         Assert.AreEqual(true, targetPrint.Contains(inputPrint));
      }

      [TestMethod, Description("Contains with too little of one letter")]
      public void TestContainsFP2()
      {
         var targetPrint = new FingerPrint("Boobs");
         var inputPrint = new FingerPrint("Boss");

         Assert.AreEqual(false, targetPrint.Contains(inputPrint));
      }

      [TestMethod, Description("Contains with missing letters")]
      public void TestContainsFP3()
      {
         var targetPrint = new FingerPrint("Boobs");
         var inputPrint = new FingerPrint("Beebs");

         Assert.AreEqual(false, targetPrint.Contains(inputPrint));
      }

      [TestMethod, Description("Contains with input much longer")]
      public void TestContainsFP4()
      {
         var targetPrint = new FingerPrint("Boobs");
         var inputPrint = new FingerPrint("Boasegsdss");

         Assert.AreEqual(false, targetPrint.Contains(inputPrint));
      }

      [TestMethod, Description("Contains with exact match")]
      public void TestContainsFP5()
      {
         var targetPrint = new FingerPrint("evil");
         var inputPrint = new FingerPrint("live");

         Assert.AreEqual(true, targetPrint.Contains(inputPrint));
      }

      [TestMethod]
      public void TestFindIfNotFound()
      {
         var count = new FingerPrint("Boobs").Find('k');
         Assert.AreEqual(0, count);
      }

      [TestMethod]
      public void TestFindsTwoWords()
      {
         var af = new AnagramFinder();
         af.LoadList("TestWords.txt", 4);
         var words = af.Find("evil");

         words.ForEach(a => Console.WriteLine(a));

         Assert.AreEqual(2, words.Count);
      }
   }
}
