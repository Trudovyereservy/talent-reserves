import {
  BREAKPOINT_DESKTOP,
  BREAKPOINT_LAPTOP,
  BREAKPOINT_NETBOOK,
  BREAKPOINT_TABLET,
  BREAKPOINT_POCKETPC,
  BREAKPOINT_MOBILE,
} from '@/utils/constResizeWindow';

import { NConfig } from './NewsTypes';

export const newsConfig: NConfig = {
  breakpoints: {
    [BREAKPOINT_MOBILE]: {
      slidesPerView: 'auto',
      initialSlide: 0,
      spaceBetween: 29,
      centeredSlides: true,
      loop: false,
    },
    [BREAKPOINT_POCKETPC]: {
      spaceBetween: 20,
      initialSlide: 0,
      slidesPerView: 2,
      loop: false,
    },
    [BREAKPOINT_TABLET]: {
      spaceBetween: 20,
      slidesPerView: 2,
      initialSlide: 2,
      loop: true,
      centeredSlides: true,
    },
    [BREAKPOINT_NETBOOK]: {
      spaceBetween: 20,
      slidesPerView: 2,
    },
    [BREAKPOINT_LAPTOP]: {
      slidesPerView: 3,
      spaceBetween: 20,
      centeredSlides: true,
    },
    [BREAKPOINT_DESKTOP]: {
      spaceBetween: 40,
      // slidesPerView: 'auto',
      slidesPerView: 3,
      initialSlide: 0,
      loop: true,
    },
  },
  loop: true,
  slidesPerView: 'auto',
  initialSlide: 0,
  autoplay: {
    delay: 1000,
    disableOnInteraction: false,
  },
  speed: 1000,
  centeredSlides: true,
  spaceBetween: 40,
  grabCursor: true,
  pagination: {
    clickable: true,
  },
};
