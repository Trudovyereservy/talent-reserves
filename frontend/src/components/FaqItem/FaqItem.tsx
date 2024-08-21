'use client';

import { useState } from 'react';

import classNames from 'classnames';

import { FaqItemProps } from './FaqItem.props';

import styles from './FaqItem.module.scss';

const FaqItem = ({ title, text }: FaqItemProps) => {
  const [isItemOpened, setIsItemOpened] = useState(false);
  const handleOpenItem = () => {
    setIsItemOpened(!isItemOpened);
  };

  return (
    <li className={styles.faqitem}>
      <div
        className={classNames(styles.faqitem__wrapper, {
          [styles.faqitem__wrapper_open]: isItemOpened,
        })}
      >
        <h3 className={styles.faqitem__title}>{title}</h3>
        <button
          className={classNames(styles.faqitem__button, {
            [styles.faqitem__button_active]: isItemOpened,
          })}
          onClick={handleOpenItem}
        />
      </div>
      <p
        className={classNames(styles.faqitem__paragraph, {
          [styles.faqitem__paragraph_open]: isItemOpened,
        })}
      >
        {text}
      </p>
    </li>
  );
};

export { FaqItem };
