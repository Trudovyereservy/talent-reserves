'use client';

import { useMemo, useState, useEffect } from 'react';

import { Card } from '@/components/CoachCards/Card/Card';
import { ICardCoachProps, IDirection } from '@/components/CoachCards/Card/Card.props';
import { useCardCount } from '@/hooks/useCardCount';
import useWindowSize from '@/hooks/useWindowSize';

import styles from './CoachList.module.scss';

const fetchData = async () => {
  const response = await fetch('https://trudreserv.site/api/coaches/', {
  // const response = await fetch('http://127.0.0.1:8000/api/coaches/', {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  const data = await response.json();
  return data;
};

const CoachList = () => {
  const [trainers, setTrainers] = useState([]);

  const width: number = useWindowSize();
  const count = useCardCount(width, 'coachesComponent');

  const visibleCoachCards: ICardCoachProps[] = useMemo(
    () => trainers.slice(0, count),
    [trainers, count],
  );

  useEffect(() => {
    fetchData()
      .then((json) => {
        if (json && json.results) {
          setTrainers(json.results);
        } else {
          console.error('Data format is incorrect');
        }
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  return (
    <section className={styles.cardslist}>
      <ul className={styles.cardslist__container}>
        {visibleCoachCards.map((card) => (
          <Card
            id={card.id}
            key={card.id}
            name={card.name}
            surname={card.surname}
            directions={
              Array.isArray(card.directions) ? (
                <>
                  {card.directions.map((direction: IDirection) => (
                    <span key={direction.id}>{direction.title}</span>
                  ))}
                </>
              ) : null
            }
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
