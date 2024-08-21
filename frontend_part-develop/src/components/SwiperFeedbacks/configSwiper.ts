import {
  BREAKPOINT_DESKTOP,
  BREAKPOINT_LAPTOP,
  BREAKPOINT_NETBOOK,
  BREAKPOINT_TABLET,
  BREAKPOINT_POCKETPC,
  BREAKPOINT_MOBILE,
} from '@/utils/constResizeWindow';

import { TConfig } from './FeedbackTypes';

export const config: TConfig = {
  breakpoints: {
    [BREAKPOINT_MOBILE]: {
      slidesPerView: 'auto',
      initialSlide: 0,
      spaceBetween: 31,
      centeredSlides: true,
      loop: false,
    },
    [BREAKPOINT_POCKETPC]: {
      spaceBetween: 20,
      initialSlide: 1,
      slidesPerView: 2,
      loop: true,
    },
    [BREAKPOINT_TABLET]: {
      spaceBetween: 20,
      slidesPerView: 2,
    },
    [BREAKPOINT_NETBOOK]: {
      spaceBetween: 20,
      slidesPerView: 2,
    },
    [BREAKPOINT_LAPTOP]: {
      slidesPerView: 'auto',
      spaceBetween: 20,
      centeredSlides: true,
    },
    [BREAKPOINT_DESKTOP]: {
      spaceBetween: 34,
      slidesPerView: 'auto',
    },
  },
  loop: true,
  slidesPerView: 'auto',
  initialSlide: 1,
  autoplay: {
    delay: 1000,
    disableOnInteraction: true,
  },
  speed: 1000,
  centeredSlides: true,
  spaceBetween: 35,
  grabCursor: true,
  pagination: {
    clickable: true,
  },
};
