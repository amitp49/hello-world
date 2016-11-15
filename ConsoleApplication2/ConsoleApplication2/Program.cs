using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication2
{
    class Program
    {
        static void Main(string[] args)
        {

            String str = "https://www.nseindia.com/content/historical/EQUITIES/2016/NOV/cm11NOV2016bhav.csv.zip";
            String prefixUrl = "https://www.nseindia.com/content/historical/EQUITIES/";
            String[] years = new String[]{"2016","2015","2014","2013","2012","2011","2010","2009","2008",
            "2007","2006","2005","2004","2003","2002","2001"};
            String[] months = new String[] { "DEC","NOV","OCT","SEP","AUG","JUL","JUN","MAY","APR","MAR","FEB","JAN"};
            String[] days = new String[] { "31", "30", "29", "28", "27", "26", "25", "24", "23", "22", "21",
            "20","19","18","17","16","15","14","13","12","11",
            "10","09","08","07","06","05","04","03","02","01"};

            String header = "<tr> <td>openWindow</td> <td>";
            String footer = "</td><td>amit</td></tr>";
            using (StreamWriter outputFile = new StreamWriter(@"C:\Users\amitp49\Downloads\CM\WriteLines.txt"))
            {
                    foreach (var year in years)
                    {
                        foreach (var month in months)
                        {
                            foreach (var day in days)
                            {
                                String url = prefixUrl + year + "/" + month + "/" + "cm" + day +  month + year + "bhav.csv.zip";
                                outputFile.WriteLine(header + url + footer);
                            }
                        }
                    }
          
            }
            Console.ReadLine();
        }
    }
}
