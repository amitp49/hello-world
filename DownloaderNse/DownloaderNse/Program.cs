using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Mime;
using System.Text;

namespace DownloaderNse
{
    class Program
    {
        static void Main(string[] args)
        {
            string remoteUri = "https://www.nseindia.com/content/historical/EQUITIES/2016/NOV/";
            string fileName = "cm01NOV2016bhav.csv.zip", myStringWebResource = null;
            // Create a new WebClient instance.
            WebClient myWebClient = new WebClient();
 
            // Concatenate the domain with the Web resource filename.
            myStringWebResource = remoteUri + fileName;
            Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, myStringWebResource);
            // Download the Web resource and save it into the current filesystem folder.
            myWebClient.DownloadFile(myStringWebResource, fileName);
            Console.WriteLine("Successfully Downloaded File \"{0}\" from \"{1}\"", fileName, myStringWebResource);
            
        }
    }
}
