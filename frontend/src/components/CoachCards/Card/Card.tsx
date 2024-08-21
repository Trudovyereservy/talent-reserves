import { useState } from 'react';

import classNames from 'classnames';
import Image from 'next/image';

import { ICardCoachProps } from './Card.props';

import styles from './Card.module.scss';

const Card = ({ photo, name, surname, directions, achievements, patronymic }: ICardCoachProps) => {
  const [openInfo, setOpenInfo] = useState(true);

  function openCard() {
    setOpenInfo((prevState) => !prevState);
  }

  return (
    <li className={styles.card}>
      <div className={styles.card__photo_wrapper}>
        <Image
          className={styles.card__image}
          src={photo}
          alt="Фотография тренера"
          width={360}
          height={360}
          priority
        />
        <button
          className={classNames(styles.card__info_additional, {
            [styles.card__info_additional_active]: !openInfo,
          })}
          onClick={openCard}
        ></button>
      </div>
      {openInfo ? (
        <div className={styles.card__info}>
          <h3 className={styles.card__name}>{surname}</h3>
          <h3 className={styles.card__name}>{name}</h3>
          <h3 className={styles.card__name}>{patronymic}</h3>
          <p className={styles.card__directions}>{directions}</p>
        </div>
      ) : (
        <p className={styles.card__achievements}>{achievements}</p>
      )}
    </li>
  );
};
export { Card };
