import Image from 'next/image';
import Link from 'next/link';

import { ICardProps } from './Card.props';

import styles from './Card.module.scss';

const Card = ({ title, subtitle, text, imgUrl, linkUrl, linkText }: ICardProps) => (
  <li className={styles.card}>
    <Image
      className={styles.card__image}
      src={imgUrl}
      alt="Обложка новости"
      width={360}
      height={210}
      priority
    />
    <h2 className={styles.card__title}>{title}</h2>
    <h3 className={styles.card__subtitle}>{subtitle}</h3>
    <p className={styles.card__text}>{text}</p>
    <Link className={styles.card__link} href={linkUrl}>
      {linkText}
    </Link>
  </li>
);
export { Card };
