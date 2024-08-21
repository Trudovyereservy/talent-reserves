import Link from 'next/link';

import { ILinksBlockProps } from './ILinksBlock.props';

import styles from './links.module.scss';

const LinksBlock = (links: ILinksBlockProps) => (
  <li className={styles.footer}>
    <Link className={styles.footer__list_item} href={links.linkUrl}>
      {links.linkText}
    </Link>
  </li>
);
export { LinksBlock };
