// number of pagination items to display depending on screen resolution
const paginationItemsDesktop = 5;
const paginationItemsMobile = 3;

// getting an array with page numbers to display
function paginationRange(start: number, end: number) {
  const length = end - start + 1;

  return Array.from({ length }, (_, i) => i + start);
}

// checking if pagination arrow is disabled
function getIsChevronDisabled(direction: string, currentPage: number, lastPage: number) {
  const isNextDisabled = currentPage === lastPage;
  const isPreviousDisabled = currentPage === 1;
  const isDisabled =
    (isNextDisabled && direction === 'next') || (isPreviousDisabled && direction === 'previous');

  return isDisabled;
}
// returning the styles for pagination arrow
function getChevronStyles(direction: string, styles: Record<string, string>, isDisabled: boolean) {
  if (direction === 'next') {
    const chevronStyle = isDisabled
      ? [styles.pagination__chevron, styles.pagination__chevron_disabled]
      : styles.pagination__chevron;

    return chevronStyle;
  } else {
    const chevronStyleInverse = isDisabled
      ? [styles.pagination__chevronInverse, styles.pagination__chevronInverse_disabled]
      : styles.pagination__chevronInverse;

    return chevronStyleInverse;
  }
}

export {
  paginationItemsDesktop,
  paginationItemsMobile,
  paginationRange,
  getIsChevronDisabled as getIsDisabled,
  getChevronStyles,
};
