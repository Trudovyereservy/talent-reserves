import classNames from 'classnames';
import Link from 'next/link';

import styles from './Pagination.module.scss';

type PaginationItemProps = {
  href: string;
  pageNumber: number;
  currentPage?: number;
};

export const PaginationItem = ({ href, pageNumber, currentPage }: PaginationItemProps) => {
  const isSelected = pageNumber === currentPage;

  return (
    <li
      className={classNames(styles.pagination__item, {
        [styles.pagination__item_type_selected]: isSelected,
      })}
    >
      {isSelected ? (
        <span>{pageNumber}</span>
      ) : (
        <Link
          aria-label={`Go to page ${pageNumber}`}
          className={styles.pagination__link}
          href={href}
        >
          <span>{pageNumber}</span>
        </Link>
      )}
    </li>
  );
};
