'use client';

import { usePathname } from 'next/navigation';

import { IDescriptionPagesProps } from './DescriptionPages.props';

import styles from './DescriptionPages.module.scss';

const DescriptionPages = ({ descriptionPages }: IDescriptionPagesProps) => {
  const pathName = usePathname();
  const blockData = descriptionPages.find((item) => item.route === pathName);

  if (!blockData) {
    return null;
  }

  return (
    <article className={styles.description__container}>
      <h2 className={styles.description__title}>{blockData.page}</h2>
      <p className={styles.description__text}>{blockData.content}</p>
    </article>
  );
};
export { DescriptionPages };
