import {
  BREAKPOINT_DESKTOP,
  BREAKPOINT_LAPTOP,
  BREAKPOINT_NETBOOK,
  BREAKPOINT_TABLET,
  BREAKPOINT_POCKETPC,
  BREAKPOINT_MOBILE,
} from '@/utils/constResizeWindow';

import { TConfigSwiper } from './SwiperGalleryTypes';

export const config: TConfigSwiper = {
  slidesPerView: 'auto',
  initialSlide: 0,
  spaceBetween: 30,
  centeredSlides: true,
  loop: true,
  grabCursor: true,
  pagination: {
    clickable: true,
  },
  navigation: false,
  breakpoints: {
    [BREAKPOINT_MOBILE]: {
      spaceBetween: 31,
      slidesPerView: 'auto',
      initialSlide: 0,
      loop: false,
    },
    [BREAKPOINT_POCKETPC]: {
      spaceBetween: 30,
      slidesPerView: 'auto',
      initialSlide: 0,
      loop: false,
    },
    [BREAKPOINT_TABLET]: {
      slidesPerView: 1,
      spaceBetween: 30,
      loop: true,
    },
    [BREAKPOINT_NETBOOK]: {
      slidesPerView: 1,
      spaceBetween: 20,
    },
    [BREAKPOINT_LAPTOP]: {
      slidesPerView: 1,
      spaceBetween: 20,
    },
    [BREAKPOINT_DESKTOP]: {
      spaceBetween: 34,
      slidesPerView: 1,
    },
  },
};
