import type { Metadata } from 'next';
import { DescriptionPages } from '@/components/DescriptionPages/DescriptionPages';
import { NewsCardsList } from '@/components/NewsCards/NewsCardsList/NewsCardsList';
import { Pagination } from '@/components/Pagination/Pagination';
import { newsCards, descriptionPages } from '@/utils/constants';

// Убедитесь, что этот тип соответствует вашему определению
interface NewsCard {
  id: string;
  title: string;
  tags?: string[];
  // другие свойства
}

interface NewsCardProps {
  id: string;
  title: string;
  tags: React.ReactNode;
}

const convertedNewsCards: NewsCardProps[] = newsCards.map(card => ({
  ...card,
  tags: card.tags ? card.tags.map(tag => <span key={tag}>{tag}</span>) : null,
}));

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
      <NewsCardsList newsCards={convertedNewsCards} />
      {/* TODO: Update with functionality */}
      <Pagination totalCards={117} currentPage={3} />
    </>
  );
}
