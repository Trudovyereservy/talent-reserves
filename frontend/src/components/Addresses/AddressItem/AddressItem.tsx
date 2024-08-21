import { FC } from 'react';

import { IAddress } from '../AddressesList.props';

import styles from './AddressItem.module.scss';

interface AddressProps {
  address: IAddress;
  onClick: (arg0: string) => void;
}

const AddressItem: FC<AddressProps> = ({ address, onClick }) => (
  <div className={styles.addressItem}>
    <button
      className={styles.addressItem__title}
      onClick={() => onClick(address.mapUrl)}
      tabIndex={0}
      onKeyDown={(event) => {
        if (event.key === 'Enter') {
          onClick(address.mapUrl);
        }
      }}
    >
      {address.title}
    </button>
    <p className={styles.addressItem__address}>{address.address}</p>
  </div>
);

export default AddressItem;
