import { FC } from 'react';

import styles from './Map.module.scss';

interface MapProps {
  mapUrl: string;
}

const Map: FC<MapProps> = ({ mapUrl }) => (
  <article className={styles.map}>
    <iframe className={styles.map__iframe} src={mapUrl} loading="lazy" title="map"></iframe>
  </article>
);

export default Map;
