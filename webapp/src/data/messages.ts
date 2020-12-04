export interface Message {
  name: string;
  username: string;
  subs: number;
  id: number;
}

const Papa = require('papaparse')

let messages: Message[];

function getDataFromCSV(url: string){
  Papa.parse(url, {
    download: true,
    header: true,
    complete: function(results: any) {
      console.log(results);
      messages = results.data;
    }
  })
}

const url = "https://raw.githubusercontent.com/marco97pa/MostSubYTMusicChannels/master/channels.csv";

getDataFromCSV(url);

export const getMessages = () => messages;

export const getMessage = (id: number) => messages.find(m => m.id === id);
