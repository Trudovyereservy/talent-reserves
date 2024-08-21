'use client';

import React, { useState } from 'react';
import { useMemo } from 'react';

import { Swiper as SwiperType } from 'swiper';
import { FreeMode, Navigation, Thumbs } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';

import useWindowSize from '@/hooks/useWindowSize';
import '@/styles/globals.scss';

import { ISwiperGalleryProps } from './SwiperGallery.props';

import { config } from './configSwiper';
import { SlidePreview } from './SlidePreview/SlidePreview';
import { Slide } from './SwiperSlide/Slide';

import './Styles.scss';

export const SwiperGallery = ({ slidesSwiperGallery }: ISwiperGalleryProps) => {
  const [thumbsSwiper, setThumbsSwiper] = useState<SwiperType | null>(null);
  const width = useWindowSize();

  const slides = useMemo(
    () =>
      slidesSwiperGallery.map((item) => (
        <SwiperSlide className="swiperGallery__custom" key={item.id}>
          <Slide imgUrl={item.imgUrl} linkUrl={item.linkUrl} />
        </SwiperSlide>
      )),
    [slidesSwiperGallery],
  );

  const slidesPreview = useMemo(
    () =>
      slidesSwiperGallery.map((item) => (
        <SwiperSlide key={item.id}>
          <SlidePreview imgUrl={item.imgUrl} />
        </SwiperSlide>
      )),
    [slidesSwiperGallery],
  );

  return (
    <div className="wrapper">
      <Swiper
        loop={config.loop}
        spaceBetween={config.spaceBetween}
        navigation={config.navigation}
        thumbs={{ swiper: thumbsSwiper }}
        modules={[FreeMode, Navigation, Thumbs]}
        centeredSlides={config.centeredSlides}
        breakpoints={config.breakpoints}
        className="swiperGalleryMain"
      >
        {slides}
      </Swiper>
      {width > 480 && (
        <Swiper
          onSwiper={setThumbsSwiper}
          loop={true}
          spaceBetween={17}
          slidesPerView={3}
          freeMode={true}
          watchSlidesProgress={true}
          modules={[FreeMode, Navigation, Thumbs]}
          className="mySwiper"
        >
          {slidesPreview}
        </Swiper>
      )}
    </div>
  );
};
