import { slidesSwiperGallery } from '@/utils/constants';

import { SwiperGallery } from '../SwiperGallery/SwiperGallery';

const SwiperGalleryProvider = () => {
  return <SwiperGallery slidesSwiperGallery={slidesSwiperGallery} />;
};

export default SwiperGalleryProvider;
