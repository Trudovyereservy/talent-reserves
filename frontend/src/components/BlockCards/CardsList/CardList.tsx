'use client';

import { useMemo } from 'react';

import { Card } from '@/components/BlockCards/Card/Card';
import { ICardBlogProps } from '@/components/BlockCards/Card/Card.props';
import { useCardCount } from '@/hooks/useCardCount';
import useWindowSize from '@/hooks/useWindowSize';

import styles from './CardsList.module.scss';

const CardsList = ({ blogCards }: { blogCards: ICardBlogProps[] }) => {
  const width: number = useWindowSize();
  const count = useCardCount(width, 'blogsComponent');

  const visibleCoachCards: ICardBlogProps[] = useMemo(
    () => blogCards.slice(0, count),
    [blogCards, count],
  );

  return (
    <section className={styles.cardslist}>
      <ul className={styles.cardslist__container}>
        {visibleCoachCards.map((card) => (
          <Card
            id={card.id}
            key={card.id}
            title={card.title}
            shortDescription={card.shortDescription}
            imgUrl={card.imgUrl}
            linkUrl={card.linkUrl}
          />
        ))}
      </ul>
    </section>
  );
};

export { CardsList };
