export interface Message {
  name: string;
  username: string;
  subs: number;
  id: number;
}

//Declare variables and constants
const Papa = require('papaparse')
const url = "https://raw.githubusercontent.com/marco97pa/MostSubYTMusicChannels/master/channels.csv";
let messages: Message[];

/* getDataFromCSV
 * url: string -> url that points to the CSV file
 *
 * Uses [Papaparse](https://www.papaparse.com/) to parse a CSV file, given an URL
 * Shows the data in log and returns an array of objects
 */
function getDataFromCSV(url: string){
  Papa.parse(url, {
    download: true,
    header: true,
    complete: function(results: any) {
      //Show results on the log (contains even more info debugging info than the array of objects itself)
      console.log(results);
      //Remove the last item because it is empty
      results.data.pop(); 
      //Populate data
      messages = results.data;
    }
  })
}

//MAIN
getDataFromCSV(url);

//Methods to be called by pages
export const getMessages = () => messages;

export const getMessage = (id: number) => messages.find(m => m.id === id);
