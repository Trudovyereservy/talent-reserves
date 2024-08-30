interface BreakpointConfig {
  spaceBetween: number;
  slidesPerView: number | 'auto';
  initialSlide?: number;
  loop?: boolean;
  centeredSlides?: boolean;
}

export interface NConfig {
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

export interface NewsCard {
  id: number;
  title: string;
  description: string;
  date_published: string;
  images: string;
  tags: string[];
}

export interface News extends NewsCard {
  id: number;
}
