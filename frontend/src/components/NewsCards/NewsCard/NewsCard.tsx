import Image from 'next/image';
import Link from 'next/link';

import { NewsCardProps } from './NewsCard.props';

import styles from './NewsCard.module.scss';

const NewsCard = ({ title, description, images }: NewsCardProps) => {
  return (
    <li className={styles.card}>
      <div className={styles.card__image_wrapper}>
        <Image
          className={styles.card__image}
          src={images}
          alt="Обложка новости"
          width={360}
          height={227}
        />
      </div>
      <Link href={images} className={styles.card__link}>
        <h2 className={styles.card__title}>{title}</h2>
        <p className={styles.card__text}>{description}</p>
      </Link>
    </li>
  );
};

export { NewsCard };
