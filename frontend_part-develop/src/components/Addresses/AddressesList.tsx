import { FC } from 'react';

import { IAddressListProps } from './AddressesList.props';
import AddressItem from './AddressItem/AddressItem';

import styles from './AddressesList.module.scss';

const Addresses: FC<IAddressListProps> = ({ addresses, onClick }) => (
  <article className={styles.addresses}>
    {addresses.map((address) => (
      <AddressItem key={address.id} address={address} onClick={onClick} />
    ))}
  </article>
);

export default Addresses;
