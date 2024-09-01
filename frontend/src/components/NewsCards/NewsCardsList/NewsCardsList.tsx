'use client';

import { useMemo } from 'react';

import { useCardCount } from '@/hooks/useCardCount';
import useWindowSize from '@/hooks/useWindowSize';

import { NewsCard } from '../NewsCard/NewsCard';
import { NewsCardProps } from '../NewsCard/NewsCard.props';

import styles from './NewsCardsList.module.scss';

const NewsCardsList = ({ newsCards }: { newsCards: NewsCardProps[] }) => {
  const width: number = useWindowSize();
  const count = useCardCount(width, 'newsCardsComponent');

  const visibleNewsCards = useMemo(() => newsCards.slice(0, count), [newsCards, count]);

  return (
    <section className={styles.cardslist}>
      <ul className={styles.cardslist__container}>
        {visibleNewsCards.map((card) => (
          <NewsCard
            key={card.id}
            id={card.id}
            title={card.title}
            description={card.description}
            images={card.images}
            date_published={card.date_published}
            tags={card.tags}
          />
        ))}
      </ul>
    </section>
  );
};

export { NewsCardsList };
