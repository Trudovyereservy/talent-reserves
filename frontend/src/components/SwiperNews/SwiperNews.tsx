'use client';

import { Pagination, Autoplay } from 'swiper/modules';
import { Scrollbar } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';

import '@/styles/globals.scss';
// import { newsCards } from '@/utils/constants';

import { newsConfig } from './ConfigSwiperNews';
import { INewsSlides } from './SwiperNews.props';
import { SwiperNewsCard } from './SwiperNewsCard/SwiperNewsCard';

import styles from './newsSwiper.module.scss';
import './newsSwiper.scss';

const SwiperNews = ({ newsCards }: INewsSlides) => {
  return (
    <div className={styles.newsSwiperWrapper}>
      <Swiper
        scrollbar={{
          hide: false,
        }}
        modules={[Scrollbar]}
        loop={newsConfig.loop}
        slidesPerView={newsConfig.slidesPerView}
        initialSlide={newsConfig.initialSlide}
        autoplay={newsConfig.autoplay}
        speed={newsConfig.speed}
        centeredSlides={newsConfig.centeredSlides}
        spaceBetween={newsConfig.spaceBetween}
        grabCursor={newsConfig.grabCursor}
        pagination={newsConfig.pagination}
        breakpoints={newsConfig.breakpoints}
        className="mySwiperNews"
      >
        {newsCards.map((item) => (
            <SwiperSlide key={item.id}>
                <SwiperNewsCard
                id={item.id}
                title={item.title}
                description={item.description}
                date_published={item.date_published}
                images={item.images}
                tags={item.tags}
                />
            </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default SwiperNews;
