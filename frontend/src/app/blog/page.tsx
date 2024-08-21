import type { Metadata } from 'next';

import { CardsList } from '@/components/BlockCards/CardsList/CardList';
import { DescriptionPages } from '@/components/DescriptionPages/DescriptionPages';
import { Pagination } from '@/components/Pagination/Pagination';
import { blogCards, descriptionPages } from '@/utils/constants';

export const metadata: Metadata = {
  title: { absolute: 'Трудовые резервы | Блог' },
  description:
    'Эта страница создана для демонстрации блоков и элементов, которые используются на сайте...',
};

export default function BlogPage() {
  return (
    <>
      <DescriptionPages descriptionPages={descriptionPages} />
      <CardsList blogCards={blogCards} />
      {/* TODO: Update with functionality */}
      <Pagination totalCards={320} currentPage={1} />
    </>
  );
}
