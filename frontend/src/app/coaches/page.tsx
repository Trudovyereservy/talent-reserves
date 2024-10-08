import type { Metadata } from 'next';

import { CoachList } from '@/components/CoachCards/CoachList/CoachList';
import { DescriptionPages } from '@/components/DescriptionPages/DescriptionPages';
import { Pagination } from '@/components/Pagination/Pagination';
import { descriptionPages } from '@/utils/constants';

export const metadata: Metadata = {
  title: { absolute: 'Трудовые резервы | Тренерский состав' },
  description:
    'Эта страница создана для демонстрации блоков и элементов, которые используются на сайте...',
};

export default function CoachesPage() {
  return (
    <>
      <DescriptionPages descriptionPages={descriptionPages} />
      <CoachList />
      {/* TODO: Update with functionality */}
      <Pagination totalCards={117} currentPage={3} />
    </>
  );
}
