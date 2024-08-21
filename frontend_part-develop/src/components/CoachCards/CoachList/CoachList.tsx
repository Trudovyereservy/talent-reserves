'use client';

import { useMemo } from 'react';

import { Card } from '@/components/CoachCards/Card/Card';
import { ICardCoachProps } from '@/components/CoachCards/Card/Card.props';
import { useCardCount } from '@/hooks/useCardCount';
import useWindowSize from '@/hooks/useWindowSize';

import styles from './CoachList.module.scss';

const CoachList = ({ coachCards }: { coachCards: ICardCoachProps[] }) => {
  const width: number = useWindowSize();
  const count = useCardCount(width, 'coachesComponent');

  const visibleCoachCards: ICardCoachProps[] = useMemo(
    () => coachCards.slice(0, count),
    [coachCards, count],
  );

  return (
    <section className={styles.cardslist}>
      <ul className={styles.cardslist__container}>
        {visibleCoachCards.map((card) => (
          <Card
            id={card.id}
            key={card.id}
            name={card.name}
            surname={card.surname}
            directions={card.directions}
            achievements={card.achievements}
            patronymic={card.patronymic}
            photo={card.photo}
          />
        ))}
      </ul>
    </section>
  );
};

export { CoachList };
