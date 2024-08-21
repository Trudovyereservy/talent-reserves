'use client';

import { useState } from 'react';

import { testAddresses, testContancts } from '../../utils/constants';
import AddressesList from '../Addresses/AddressesList';
import ContactCardList from '../ContactCards/ContactCardsList/ContactCardList';
import Map from '../Map/Map';

export default function ContactsProvider() {
  const [mapUrl, setMapUrl] = useState(testAddresses[0].mapUrl);
  const handleAddressChange = (mapUrl: string) => {
    setMapUrl(mapUrl);
  };

  return (
    <>
      <Map mapUrl={mapUrl} />
      <AddressesList addresses={testAddresses} onClick={handleAddressChange} />
      <ContactCardList cards={testContancts} />
    </>
  );
}
