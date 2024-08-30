'use client';

import { Pagination, Autoplay } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';

import '@/styles/globals.scss';

import { config } from './configSwiper';
import { ISwiperFeedbacksProps } from './SwiperFeedbacks.props';
import { SwiperPost } from './SwiperPost/SwiperPost';

import './SwiperCustom.scss';
import styles from './SwiperFeedbacks.module.scss';

const SwiperFeedbacks = ({ sliderPosts }: ISwiperFeedbacksProps) => {
  return (
    <>
      <h2 className={styles.feedbacks__title}>Федерации</h2>
      <Swiper
        modules={[Pagination, Autoplay]}
        loop={config.loop}
        slidesPerView={config.slidesPerView}
        initialSlide={config.initialSlide}
        autoplay={config.autoplay}
        speed={config.speed}
        centeredSlides={config.centeredSlides}
        spaceBetween={config.spaceBetween}
        grabCursor={config.grabCursor}
        pagination={config.pagination}
        breakpoints={config.breakpoints}
        className="slidecustom"
      >
        {sliderPosts.map((item) => (
          <SwiperSlide key={item.id} className="slide-custom">
            <SwiperPost post={item.post} name={item.name} description={item.description} />
          </SwiperSlide>
        ))}
      </Swiper>
    </>
  );
};

export default SwiperFeedbacks;
