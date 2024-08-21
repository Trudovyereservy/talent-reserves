export interface ILinkItem {
  text: string;
  id: number;
  linkText: string;
  linkUrl: string;
}

export type FormValues = {
  nameInput: string;
  required: string;
  pattern: { value: RegExp; message: string };
  Phone?: React.ReactNode;
};
