import React from 'react';
import {
  IonAvatar,
  IonItem,
  IonLabel,
  IonNote
  } from '@ionic/react';
import { Artist } from '../data/artists';
import './ArtistListItem.css';

interface ArtistListItemProps {
  artist: Artist;
}

//Initialize index
let i: number = 0;

const ArtistListItem: React.FC<ArtistListItemProps> = ({ artist }) => { 
  i++;
  return (
    <IonItem href={"https://www.youtube.com/channel/" + artist.id} detail={false}>
      <IonNote slot="start">
        {i}
      </IonNote>
      <IonAvatar>
        <img src={artist.img} alt={artist.name}/>
      </IonAvatar>
      <IonLabel>
        <h2>
          {artist.name}
          <span className="date">
            <IonNote>{(artist.subs/1000000).toFixed(1)} Mln</IonNote>
          </span>
        </h2>
      </IonLabel>
    </IonItem>
  );
};

export default ArtistListItem;
