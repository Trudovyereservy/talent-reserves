'use client';

import { useMemo } from 'react';

import { useCardCount } from '@/hooks/useCardCount';
import useWindowSize from '@/hooks/useWindowSize';

import { Card } from './Card/Card';
import { CardData } from './TCardsNews';

import styles from './CardsNews.module.scss';

const CardsNews = ({ cardsNews }: { cardsNews: CardData[] }) => {
  const width: number = useWindowSize();
  const count = useCardCount(width, 'mainComponent');
  const visibleCardsNews: CardData[] = useMemo(() => cardsNews.slice(0, count), [cardsNews, count]);
  return (
    <section className={styles.cardnews}>
      <h2 className={styles.cardslist__title}>Пример текста</h2>
      <ul className={styles.cardslist__container}>
        {visibleCardsNews.map((card) => (
          <Card
            key={card.id}
            imgUrl={card.imgUrl}
            linkUrl={card.linkUrl}
            linkText={card.linkText}
          />
        ))}
      </ul>
    </section>
  );
};

export { CardsNews };
