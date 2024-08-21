import classNames from 'classnames';
import Link from 'next/link';

import { getIsDisabled, getChevronStyles } from '@/utils/pagination';

import styles from './Pagination.module.scss';

type PaginationArrowProps = {
  href: string;
  currentPage: number;
  lastPage?: number;
  direction: 'previous' | 'next';
};

export const PaginationArrow = ({
  href,
  currentPage,
  lastPage,
  direction,
}: PaginationArrowProps) => {
  const isDisabled = getIsDisabled(direction, currentPage, lastPage!);
  const chevronStyles = getChevronStyles(direction, styles, isDisabled);

  return (
    <li className={classNames(styles.pagination__item, chevronStyles)}>
      {isDisabled ? null : (
        <Link
          aria-label={`Go to ${direction} page`}
          title={`Go to ${direction} page`}
          className={styles.pagination__link}
          href={href}
        />
      )}
    </li>
  );
};
