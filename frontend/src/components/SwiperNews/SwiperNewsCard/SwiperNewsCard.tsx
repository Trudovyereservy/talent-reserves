import Image from 'next/image';

import { NewsCard } from '../NewsTypes';

import './SwiperNewsCard.scss';

export const SwiperNewsCard = ({
  title,
  images,
  // id,
  // description,
  // date_published,
  // tags
}: NewsCard) => {
  return (
    <div className="swiper-news-card">
      <div className="swiper-news-card__image_wrapper">
        <Image
          className="swiper-news-card__image"
          src={images}
          alt="Изображение новости"
          width={460}
          height={400}
        />
        <span className="swiper-news-card__image_title">Пример</span>
      </div>
      <span className="swiper-news-card__title">{title}</span>
    </div>
  );
};
