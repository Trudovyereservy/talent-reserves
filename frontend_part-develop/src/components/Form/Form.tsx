'use client';

import Image from 'next/image';
import { useForm, SubmitHandler } from 'react-hook-form';

import lines from '@/../public/Lines.svg';
import { regularExpressions } from '@/utils/regularExpressions';

import styles from './Form.module.scss';

interface FormData {
  name: string;
  phoneNumber: number;
  eMail: string;
}

export default function Form() {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting, isValid },
  } = useForm<FormData>({ mode: 'all' });

  const onSubmit: SubmitHandler<FormData> = () => {
    reset();
  };

  return (
    <div className={styles.form}>
      <h2 className={styles.form__headerMobile}>Пример текста</h2>
      <div className={styles.form__photoContainer} />
      <Image className={styles.form__lines} src={lines} alt="Декоративные линии" />
      {/* <Image className={styles.form__lines} src={childHappy} alt="Декоративные линии" /> */}
      <div className={styles.form__formContainer}>
        <h2 className={styles.form__header}>Пример текста</h2>
        <p className={styles.form__subtitle}>
          Пример текста пример текста пример текста пример текста пример текста пример текста
        </p>
        <form className={styles.form__form} onSubmit={handleSubmit(onSubmit)}>
          <input
            className={styles.form__input}
            placeholder="Ваше имя"
            aria-invalid={errors.name ? true : false}
            {...register('name', {
              required: 'Поле обязательно для заполнения',
              minLength: {
                value: 2,
                message: 'Имя должно быть не менее двух букв',
              },
              maxLength: {
                value: 30,
                message: 'Имя должно быть не более тридцати букв',
              },
              pattern: {
                value: regularExpressions.name,
                message: 'Допускается латиница, кириллица, пробел и дефис',
              },
            })}
          ></input>
          <span className={styles.form__inputError}>{errors?.name?.message || ''}</span>
          <input
            className={styles.form__input}
            placeholder="Телефон"
            type="text"
            aria-invalid={errors.phoneNumber ? true : false}
            {...register('phoneNumber', {
              required: 'Поле обязательно для заполнения',
              maxLength: {
                value: 12,
                message: 'Не более одиннадцати цифр',
              },
              pattern: {
                value: regularExpressions.phoneNumber,
                message: 'Пожалуйста, введите номер телефона',
              },
            })}
          ></input>
          <span className={styles.form__inputError}>{errors?.phoneNumber?.message || ''}</span>
          <input
            className={styles.form__input}
            placeholder="E-mail"
            type="email"
            aria-invalid={errors.eMail ? true : false}
            {...register('eMail', {
              required: 'Поле обязательно для заполнения',
              maxLength: {
                value: 50,
                message: 'Email должен быть не более пятидесяти символов',
              },
              pattern: {
                value: regularExpressions.email,
                message: 'Пожалуйста, введите электронную почту',
              },
            })}
          ></input>
          <span className={styles.form__inputError}>{errors?.eMail?.message || ''}</span>
          <button
            className={styles.form__submitButton}
            type="submit"
            disabled={isSubmitting || !isValid}
          >
            Пример текста
          </button>
        </form>
      </div>
    </div>
  );
}
