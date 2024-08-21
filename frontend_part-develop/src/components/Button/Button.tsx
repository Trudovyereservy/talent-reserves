import { ButtonProps } from './Button.props';

const Button = (props: ButtonProps) => {
  const { onClick, className, disabled, children } = props;

  return (
    <button className={className} disabled={disabled} onClick={onClick}>
      {children}
    </button>
  );
};

export { Button };
