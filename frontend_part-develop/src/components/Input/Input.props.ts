import { RegisterOptions, UseFormRegister } from 'react-hook-form';

export interface InputValues {
  nameInput: string;
  required: string;
  pattern: { value: RegExp; message: string };
}

export interface InputProps {
  className?: string;
  register: UseFormRegister<InputValues>;
  nameInput: string;
  rest?: RegisterOptions;
}
