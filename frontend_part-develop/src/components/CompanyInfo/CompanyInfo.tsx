'use client';

import { useMemo } from 'react';

import useWindowSize from '@/hooks/useWindowSize';

import { cardsCompanyInfo } from '../../utils/constants';
import SwiperGalleryProvider from '../ProviderComponents/SwiperGalleryProvider';

import { CompanyInfoItem } from './CompanyInfoItem/CompanyInfoItem';

import styles from './CompanyInfo.module.scss';

const CompanyInfo = () => {
  const widthWindow = useWindowSize();
  const cards = useMemo(
    () =>
      cardsCompanyInfo.map((item) => (
        <CompanyInfoItem key={item.id} textItem={item.textItem} subtitle={item.subtitle} />
      )),
    [],
  );

  const mobileView = () => (
    <article className={styles.companyinfo__wrapper}>
      <h2 className={styles.companyinfo__title}>Пример текста</h2>
      <div className={styles.companyinfo__info}>
        <div className={styles.companyinfo__description}>
          Пример текста пример текста пример текста...
        </div>
        <div className={styles.companyinfo__items}>
          <SwiperGalleryProvider />
        </div>
        <div className={styles.companyinfo__items_wrapper}>{cards}</div>
      </div>
    </article>
  );

  const desktopView = () => (
    <article className={styles.companyinfo__wrapper}>
      <h2 className={styles.companyinfo__title}>Пример текста</h2>
      <div className={styles.companyinfo__infowrapper}>
        <div className={styles.companyinfo__info}>
          <div className={styles.companyinfo__description}>
            Пример текста пример текста пример текста...
          </div>
          <div className={styles.companyinfo__items}>{cards}</div>
        </div>
        <SwiperGalleryProvider />
      </div>
    </article>
  );

  return (
    <section className={styles.companyinfo}>
      {widthWindow <= 768 ? mobileView() : desktopView()}
    </section>
  );
};

export { CompanyInfo };
