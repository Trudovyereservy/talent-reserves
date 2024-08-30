import { Card } from '@/components/Card/Card';
import { testCards } from '@/utils/constants';

import styles from './CardsList.module.scss';

const CardsList = () => (
  <section className={styles.cardslist}>
    <h2 className={styles.cardslist__title}>Пример текста</h2>
    <ul className={styles.cardslist__container}>
      {testCards.map((card) => (
        <Card
          key={card.id}
          title={card.title}
          subtitle={card.subtitle}
          text={card.text}
          imgUrl={card.imgUrl}
          linkUrl={card.linkUrl}
          linkText={card.linkText}
        />
      ))}
    </ul>
  </section>
);

export { CardsList };
