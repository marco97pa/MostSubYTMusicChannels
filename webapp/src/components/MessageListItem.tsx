import React from 'react';
import {
  IonAvatar,
  IonItem,
  IonLabel,
  IonNote
  } from '@ionic/react';
import { Message } from '../data/messages';
import './MessageListItem.css';

interface MessageListItemProps {
  message: Message;
}

let i: number = 0;

const MessageListItem: React.FC<MessageListItemProps> = ({ message }) => { 
  i++;
  return (
    <IonItem routerLink={`/message/${message.id}`} detail={false}>
      <IonAvatar slot="start">
        <img src={"https://unavatar.now.sh/twitter/" + message.username}/>
      </IonAvatar>
      <IonLabel>
        <h2>
          {message.name}
          <span className="date">
            <IonNote>{message.subs}</IonNote>
          </span>
        </h2>
        <h3>{i}</h3>
      </IonLabel>
    </IonItem>
  );
};

export default MessageListItem;
