interface BreakpointConfig {
  spaceBetween: number;
  slidesPerView: number | 'auto';
  initialSlide?: number;
  loop?: boolean;
  centeredSlides?: boolean;
}

export interface TConfig {
  breakpoints: {
    [key: string]: BreakpointConfig;
  };
  loop: boolean;
  slidesPerView: number | 'auto';
  initialSlide: number;
  autoplay: {
    delay: number;
    disableOnInteraction: boolean;
  };
  speed: number;
  centeredSlides: boolean;
  spaceBetween: number;
  grabCursor: boolean;
  pagination: {
    clickable: boolean;
  };
}

export interface TPost {
  post: string;
  name: string;
  description: string;
}

export interface TFeedback extends TPost {
  id: number;
}
