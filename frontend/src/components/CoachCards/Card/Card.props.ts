export interface IDirection {
  id: number;
  title: string;
}

export interface ICardCoachProps {
  name: string;
  surname: string;
  directions: JSX.Element | null;
  achievements: string;
  patronymic: string;
  photo: string;
  id: number;
}
