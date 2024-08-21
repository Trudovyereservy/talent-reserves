import { Metadata } from 'next';

import { DescriptionPages } from '@/components/DescriptionPages/DescriptionPages';
import ContactsProvider from '@/components/ProviderComponents/ContactsProvider';
import { descriptionPages } from '@/utils/constants';

export const metadata: Metadata = {
  title: { absolute: 'Трудовые резервы | Контакты' },
  description:
    'Эта страница создана для демонстрации блоков и элементов, которые используются на сайте...',
};

export default function ContactsPage() {
  return (
    <>
      <DescriptionPages descriptionPages={descriptionPages} />
      <ContactsProvider />
    </>
  );
}
