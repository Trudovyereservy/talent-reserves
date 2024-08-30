'use client';

import { newsCards } from '@/utils/constants';

import SwiperNews from '../SwiperNews/SwiperNews';

const SwiperNewsProvider = () => {
    return <SwiperNews newsCards={newsCards} />
}

export default SwiperNewsProvider;