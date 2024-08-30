'use client';

import classNames from 'classnames';
import Link from 'next/link';
import { useForm } from 'react-hook-form';

import { Button } from '@/components/Button/Button';
import { Input } from '@/components/Input/Input';
import { LinksBlock } from '@/components/Links/LinksBlock';
import { linksItems, buttonsNames } from '@/utils/constants';

import { ILinkItem, FormValues } from './Footer.props';

import styles from './Footer.module.scss';

const Footer = () => {
  const {
    register,
    handleSubmit,
    formState: { errors, isValid },
  } = useForm<FormValues>({ mode: 'onChange' });

  const createLinks = (index: number, sectionName: string, linksItems: Array<ILinkItem>) => (
    <ul key={index} className={styles.footer__list}>
      <h3 className={styles.footer__list_title}>{sectionName}</h3>
      {linksItems.map((link) => (
        <LinksBlock key={link.id} linkUrl={link.linkUrl} linkText={link.linkText} />
      ))}
    </ul>
  );

  return (
    <footer className={styles.footer__container}>
      <div className={styles.footer__wrapper}>
        <div className={styles.footer__links}>
          <div className={styles.footer__about}>
            <Link href="#">
              <div className={styles.footer__logo}></div>
            </Link>
            <h3 className={classNames(styles.footer__about_title, styles.footer__hidden)}>
              Пример текста
            </h3>
            <p className={classNames(styles.footer__about_subtitle, styles.footer__hidden)}>
              Пример текста пример текста пример текста пример текста пример текста пример текста{' '}
            </p>
          </div>
          <nav className={styles.footer__menu}>
            {createLinks(1, 'Список1', linksItems.exampleOne)}
            {createLinks(2, 'Список2', linksItems.exampleTwo)}
            {createLinks(3, 'Список3', linksItems.exampleThree)}
          </nav>
        </div>

        <div className={styles.footer__contacts}>
          <div className={styles.footer__social}>
            <Link href="#">
              <div
                className={classNames(styles.footer__social_icon, styles.footer__social_facebook)}
              ></div>
            </Link>
            <Link href="#">
              <div
                className={classNames(styles.footer__social_icon, styles.footer__social_twitter)}
              ></div>
            </Link>
          </div>
          <div className={styles.footer__adress}>
            <Link href="#">
              <p className={styles.footer__contacts_item}>Пример</p>
            </Link>
            <Link href="#">
              <p className={styles.footer__contacts_item}>Пример</p>
            </Link>
          </div>
          <form
            className={classNames(styles.footer__phone_number, styles.footer__hidden)}
            onSubmit={handleSubmit(() => {})}
          >
            <Input className={styles.footer__input_phone} register={register} nameInput={'Phone'} />
            <Button
              className={styles.footer__button}
              disabled={!isValid}
              active={true}
              onClick={() => {}}
            >
              {buttonsNames.mainButtonFooter}
            </Button>
            <div className={styles.footer__form_error}>
              {errors?.Phone && <p>{errors?.Phone?.message || 'введите номер телефона'}</p>}
            </div>
          </form>
        </div>
      </div>
    </footer>
  );
};

export { Footer };
