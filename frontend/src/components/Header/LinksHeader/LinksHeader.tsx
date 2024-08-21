import classNames from 'classnames';
import Link from 'next/link';

import { ILinksHeaderProps } from './ILinksHeader.props';

import styles from '../header.module.scss';

const LinksHeader = (links: ILinksHeaderProps) => (
  <li className={styles.footer}>
    <Link
      className={classNames(styles.header__navitem, styles.header__navhidden)}
      href={links.href}
    >
      {links.title}
    </Link>
  </li>
);
export { LinksHeader };
