export interface NewsCardProps {
  id: number;
  title: string;
  description: string;
  date_published: string;
  images: string;
  // tags: string[];
  tags: JSX.Element | null;
}

export interface NewsCardProp {
  id: number;
  title: string;
  description: string;
  date_published: string;
  images: string;
  tags: ITags[];
}

export interface ITags {
  id: number;
  name: string;
}
