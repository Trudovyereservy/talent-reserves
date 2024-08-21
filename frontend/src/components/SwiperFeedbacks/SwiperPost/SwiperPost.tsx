import { TPost } from '@/components/SwiperFeedbacks/FeedbackTypes';

// import styles from './SwiperPost.module.scss'; не использую модули, т.к. не получается в дальнейшем
// стилизовать блоки предыдущего и следующего слайдов из-за применения в модулях случайного хэша селектора класса.
import './SwiperPost.scss';

export const SwiperPost = ({ post, name, description }: TPost) => {
  return (
    <article className="feedbackCard">
      <p className="feedbackCard__textPost">{post}</p>
      <div className="feedbackCard__about">
        <h4 className="feedbackCard__textName">{name}</h4>
        <p className="feedbackCard__textDescription">{description}</p>
      </div>
    </article>
  );
};
