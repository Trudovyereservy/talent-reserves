import { InputProps, InputValues } from './Input.props';

const Input = ({ className, register, nameInput, ...inputProps }: InputProps) => (
  <input
    type="text"
    placeholder="Phone"
    className={className}
    {...register(nameInput as keyof InputValues, {
      required: 'Введите телефон в формате +7-***-**-**',
      pattern: {
        value: /^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$/,
        message: 'Неверный формат телефона',
      },
    })}
    // {...restProps}
    {...inputProps}
  />
);
export { Input };
