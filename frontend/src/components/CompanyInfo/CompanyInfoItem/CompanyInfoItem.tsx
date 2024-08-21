import { ICompanyInfoItem } from './CompanyInfoItem.props';

import styles from './CompanyInfoItem.module.scss';

const CompanyInfoItem = ({ textItem, subtitle }: ICompanyInfoItem) => {
  return (
    <div className={styles.companyinfo__item}>
      <div className={styles.companyinfo__icon}></div>
      <h3 className={styles.companyinfo__subtitle}>{subtitle}</h3>
      <p className={styles.companyinfo__text}>{textItem}</p>
    </div>
  );
};

export { CompanyInfoItem };
