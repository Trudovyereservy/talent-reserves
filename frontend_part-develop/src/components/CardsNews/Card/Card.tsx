import Image from 'next/image';
import Link from 'next/link';

import { ICardNewsMainProps } from './Card.props';

import styles from './Card.module.scss';

const Card = ({ imgUrl, linkUrl, linkText }: ICardNewsMainProps) => (
  <li className={styles.card}>
    <Image
      className={styles.card__image}
      src={imgUrl}
      alt="Обложка новости"
      width={260}
      height={263}
    />
    <Link className={styles.card__link} href={linkUrl}>
      {linkText}
    </Link>
  </li>
);
export { Card };
