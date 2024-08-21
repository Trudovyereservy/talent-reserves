import { paginationRange } from '@/utils/pagination';

import { PaginationItem } from './PaginationItem';

type PaginationListProps = {
  start: number;
  end: number;
  currentPage: number;
};

export const PaginationList = ({ start, end, currentPage }: PaginationListProps) => (
  <>
    {paginationRange(start, end).map((page) => (
      <PaginationItem
        href={`?page=${page}`}
        pageNumber={page}
        currentPage={currentPage}
        key={page}
      />
    ))}
  </>
);
