export interface IContactCard {
  id: number;
  title: string;
  subtitle: string;
}

export interface IContactCardListProps {
  cards: IContactCard[];
}
