import Image from 'next/image';

import { ISlidePreviewProps } from './SlidePreview.props';

import './SlidePreview.scss';

const SlidePreview = ({ imgUrl }: ISlidePreviewProps) => (
  <Image
    className="card__image"
    src={imgUrl}
    alt="Картинка из жизни спортшколы"
    width={150}
    height={130}
  />
);
export { SlidePreview };
