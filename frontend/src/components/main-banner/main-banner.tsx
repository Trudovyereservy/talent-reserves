'use client';

import Image from 'next/image';

import pictureLogo from '@/../public/Mask group.png';
import pictureLogoMobile from '@/../public/Mask group_394px.png';
import { Button } from '@/components/Button/Button';
import { buttonsNames } from '@/utils/constants';

import styles from '../main-banner/main-banner.module.scss';

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
      Трудовые резервы – <span className={styles.mainbanner__words}>стань лидером</span> через спорт
      </h1>
      <p className={styles.mainbanner__subtitle}>
      Мы развиваем молодых лидеров через спорт и здоровый образ жизни. 
      Через спортивную подготовку и дисциплину учим достигать целей и нести ответственность за свою жизнь. 
      Воспитываем будущее поколение профессионалов своего дела.
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
