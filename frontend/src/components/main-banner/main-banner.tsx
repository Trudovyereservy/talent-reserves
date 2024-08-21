'use client';

import Image from 'next/image';

import pictureLogo from '@/../public/Mask group.png';
import pictureLogoMobile from '@/../public/Mask group_394px.png';
import { Button } from '@/components/Button/Button';
import { buttonsNames } from '@/utils/constants';

import styles from './main-banner.module.scss';

const MainBanner = () => (
  <div className={styles.mainbanner__wrapper}>
    <Image src={pictureLogo} alt="background_main_banner" className={styles.mainbanner__logo} />
    <Image
      src={pictureLogoMobile}
      alt="background_main_banner"
      className={styles.mainbanner__logo_mobile}
    />

    <div className={styles.mainbanner__background}></div>
    <div className={styles.mainbanner__container}>
      <h1 className={styles.mainbanner__title}>
        Пример <span className={styles.mainbanner__words}>текста пример текста</span> пример текста
        пример текста
      </h1>
      <p className={styles.mainbanner__subtitle}>
        Пример текста пример текста пример текста пример текста пример текста пример текста пример
        текста пример текста пример текста
      </p>
      <Button
        className={styles.mainbanner__button}
        disabled={false}
        active={true}
        onClick={() => {}}
      >
        {buttonsNames.mainButtonFooter}
      </Button>
    </div>
  </div>
);

export { MainBanner };
