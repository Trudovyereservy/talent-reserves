import type { Metadata } from 'next';

import { DescriptionPages } from '@/components/DescriptionPages/DescriptionPages';
import { NewsCardsList } from '@/components/NewsCards/NewsCardsList/NewsCardsList';
import { Pagination } from '@/components/Pagination/Pagination';
import SwiperNewsProvider from '@/components/ProviderComponents/SwiperNewsProvider';
import { newsCards, descriptionPages } from '@/utils/constants';

export const metadata: Metadata = {
  title: { absolute: 'Трудовые резервы | Новости' },
  description:
    'Эта страница создана для демонстрации блоков и элементов, которые используются на сайте...',
};

export default function NewsPage() {
  return (
    <>
      <head>
        <title>Трудовые резервы | Новости</title>
        <meta name="title" content="Новости" />
      </head>
      <DescriptionPages descriptionPages={descriptionPages} />
      <NewsCardsList
        newsCards={newsCards.map(card => ({
          ...card,
          tags: card.tags || [],
        }))}
      />
      {/* TODO: Update with functionality */}
      <Pagination totalCards={117} currentPage={3} />
    </>
  );
}
