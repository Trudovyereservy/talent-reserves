import React, { FC } from 'react';

import classNames from 'classnames';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

import { navLinksMenu } from '@/utils/constants';

import { IMenuProps } from './Menu.props';

import styles from './menu.module.scss';

const Menu: FC<IMenuProps> = ({ handler, handleToggleMenu }) => {
  const closeMenu = () => {
    handleToggleMenu(false);
  };

  const pathName = usePathname();

  return (
    <section className={`${styles.menu} ${handler ? `${styles.menu_active}` : ''}`}>
      <div
        className={classNames(styles.menu__overlay, {
          [styles.menu__overlay_active]: handler,
        })}
      ></div>
      <section className={styles.menu__container}>
        <button className={styles.menu__button_close} type="button" onClick={closeMenu}></button>
        <nav className={styles.menu__nav}>
          <>
            {navLinksMenu.map((link) => {
              const isActive = pathName === link.href;
              return (
                <Link
                  className={classNames(styles.menu__link, {
                    [styles.menu__link_active]: isActive,
                  })}
                  onClick={closeMenu}
                  href={link.href}
                  key={link.id}
                >
                  {link.name}
                </Link>
              );
            })}
          </>
        </nav>
      </section>
    </section>
  );
};

export default Menu;
