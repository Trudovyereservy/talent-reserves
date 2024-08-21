'use client';

import { useMemo } from 'react';

import styles from '@/components/Pagination/Pagination.module.scss';
import usePagination from '@/hooks/usePagination';

import { PaginationArrow } from './PaginationArrow';
import { PaginationEllipsis } from './PaginationEllipsis';
import { PaginationItem } from './PaginationItem';
import { PaginationList } from './PaginationList';

type PaginationItemProps = {
  totalCards: number;
  currentPage: number;
};

export const Pagination = ({ totalCards, currentPage }: PaginationItemProps) => {
  const { paginationItemsToDisplay, totalPages, lastPage } = usePagination(totalCards);

  // minimal number of pagination items to display
  const paginationItemsMinimum = 3;
  // number of items to display before and after the current page
  const siblings = Math.floor((paginationItemsToDisplay - paginationItemsMinimum) / 2);

  const isPaginationNecessary = totalPages > paginationItemsToDisplay;
  const isCurrentPageNearEnd = currentPage + siblings * 2 >= totalPages;
  const isCurrentPageNearStart = currentPage <= siblings + 2;
  const isCurrentPageAwayFromBothEnds = currentPage > siblings * 2 + 1;

  const ellipsisNotVisible = !isPaginationNecessary;
  const ellipsisLeftVisible = isPaginationNecessary && isCurrentPageNearEnd;
  const ellipsisRightVisible = isPaginationNecessary && isCurrentPageNearStart;
  const ellipsisLeftAndRightVisible = isPaginationNecessary && isCurrentPageAwayFromBothEnds;

  function renderPaginationItems() {
    // no dots are visible
    if (ellipsisNotVisible) {
      return <PaginationList start={1} end={totalPages} currentPage={currentPage} />;
    }

    // only the left dots are visible
    if (ellipsisLeftVisible) {
      return (
        <>
          <PaginationItem href={`?page=${1}`} pageNumber={1} />
          <PaginationEllipsis />
          <PaginationList
            start={totalPages - (siblings * 2 + 1)}
            end={totalPages}
            currentPage={currentPage}
          />
        </>
      );
    }

    // only the right dots are visible
    if (ellipsisRightVisible) {
      return (
        <>
          <PaginationList start={1} end={siblings * 2 + 2} currentPage={currentPage} />

          <PaginationEllipsis />
          <PaginationItem href={`?page=${lastPage}`} pageNumber={lastPage} />
        </>
      );
    }

    // both the left and the right dots are visible
    if (ellipsisLeftAndRightVisible) {
      return (
        <>
          <PaginationItem href={`?page=${1}`} pageNumber={1} />
          <PaginationEllipsis />

          <PaginationList
            start={currentPage - siblings}
            end={currentPage + siblings}
            currentPage={currentPage}
          />

          <PaginationEllipsis />
          <PaginationItem href={`?page=${lastPage}`} pageNumber={lastPage} />
        </>
      );
    }
  }

  const renderedPagination = useMemo(() => renderPaginationItems(), [totalPages, currentPage]);

  return (
    <nav role="navigation" aria-label="pagination" className={styles.pagination}>
      <ul className={styles.pagination__content}>
        <PaginationArrow
          href={`?page=${currentPage - 1}`}
          currentPage={currentPage}
          direction="previous"
        />

        {renderedPagination}

        <PaginationArrow
          href={`?page=${currentPage + 1}`}
          currentPage={currentPage}
          lastPage={lastPage}
          direction="next"
        />
      </ul>
    </nav>
  );
};
