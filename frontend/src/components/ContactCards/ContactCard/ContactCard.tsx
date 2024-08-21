import { FC } from 'react';

import { IContactCard } from '../ContactCardsList/ContactCardList.props';

import styles from './ContactCard.module.scss';

interface CardProp {
  card: IContactCard;
}

const ContactCard: FC<CardProp> = ({ card }) => (
  <div className={styles.card}>
    <h3 className={styles.card__title}>{card.title}</h3>
    <p className={styles.card__subtitle}>{card.subtitle}</p>
  </div>
);

export default ContactCard;
