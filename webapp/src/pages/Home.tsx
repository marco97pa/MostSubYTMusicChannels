import React, { useState } from 'react';
import MessageListItem from '../components/ArtistListItem';
import { Artist, getArtists } from '../data/artists';
import {
  IonContent,
  IonHeader,
  IonList,
  IonPage,
  IonRefresher,
  IonRefresherContent,
  IonTitle,
  IonToolbar,
  IonCard,
  IonItem,
  IonIcon,
  IonLabel,
  IonButton,
  IonCardContent,
  IonGrid,
  IonRow,
  IonCol,
  useIonViewWillEnter
} from '@ionic/react';
import { logoTwitter, logoGithub, walletOutline } from 'ionicons/icons';
import './Home.css';

const Home: React.FC = () => {

  const [artists, setArtists] = useState<Artist[]>([]);

  useIonViewWillEnter(() => {
    const arts = getArtists();
    setArtists(arts);
  });

  const refresh = (e: CustomEvent) => {
    setTimeout(() => {
      e.detail.complete();
    }, 3000);
  };

  return (
    <IonPage id="home-page">

      <IonHeader color="primary">
        <IonToolbar color="primary">
          <IonTitle>Most Subscribed YouTube Music Channels</IonTitle>
        </IonToolbar>
      </IonHeader>

      <IonContent fullscreen>
        <IonRefresher slot="fixed" onIonRefresh={refresh}>
          <IonRefresherContent></IonRefresherContent>
        </IonRefresher>

        <IonList>
          {artists.map(a => <MessageListItem key={a.id} artist={a} />)}
        </IonList>


        <IonGrid>
          <IonRow>
            <IonCol size="12" size-sm="4">

              <IonCard>
                <IonItem>
                  <IonIcon icon={logoTwitter} slot="start" />
                  <IonLabel>Keep updated!</IonLabel>
                  <IonButton fill="outline" slot="end" href="https://twitter.com/mostSubYTMusic?s=09">Follow</IonButton>
                </IonItem>
                <IonCardContent>
                  Follow us on Twitter for daily updates about the most subscribed YouTube Music channels
                </IonCardContent>
              </IonCard>
            
            </IonCol>
            <IonCol size="12" size-sm="4">

            <IonCard>
                <IonItem>
                  <IonIcon icon={logoGithub} slot="start" />
                  <IonLabel>Open source</IonLabel>
                  <IonButton fill="outline" slot="end" href="https://github.com/marco97pa/MostSubYTMusicChannels">GitHub</IonButton>
                </IonItem>
                <IonCardContent>
                  The code behind this project is available on GitHub. Feel free to review it or help me by adding new features,
                  fixing bugs or improve this website.
                </IonCardContent>
              </IonCard>

            </IonCol>
            <IonCol size="12" size-sm="4">

            <IonCard>
                <IonItem>
                  <IonIcon icon={walletOutline} slot="start"/>
                  <IonLabel>Contribute!</IonLabel>
                  <IonButton fill="outline" slot="end" href="https://paypal.me/marco97pa">Donate</IonButton>
                </IonItem>
                <IonCardContent>
                  This service runs (almost) 24/24h on a Raspberry Pi. It could run way better if I had a proper server.
                  So if you are happy of this service and you would like to contribute, any donation is really appreciated.
                </IonCardContent>
              </IonCard>

            </IonCol>

          </IonRow>
        </IonGrid>

      </IonContent>
    </IonPage>
  );
};

export default Home;
