import {
  BREAKPOINT_DESKTOP,
  BREAKPOINT_LAPTOP,
  BREAKPOINT_MOBILE,
  CARD_COUNT_MOBILE,
  CARD_COUNT_LAPTOP,
  CARD_COUNT_DESKTOP,
} from './constResizeWindow';

type CardCountConfig = {
  default: number;
  [BREAKPOINT_LAPTOP]?: number;
  [BREAKPOINT_DESKTOP]?: number;
  [BREAKPOINT_MOBILE]?: number;
};

const cardCountConfigs: Record<string, CardCountConfig> = {
  mainComponent: {
    default: CARD_COUNT_MOBILE,
    [BREAKPOINT_MOBILE]: CARD_COUNT_LAPTOP,
  },
  blogsComponent: {
    default: CARD_COUNT_LAPTOP,
    [BREAKPOINT_DESKTOP]: CARD_COUNT_DESKTOP,
    [BREAKPOINT_LAPTOP]: CARD_COUNT_LAPTOP,
    [BREAKPOINT_MOBILE]: CARD_COUNT_LAPTOP,
  },
  coachesComponent: {
    default: CARD_COUNT_LAPTOP,
    [BREAKPOINT_DESKTOP]: CARD_COUNT_DESKTOP,
    [BREAKPOINT_LAPTOP]: CARD_COUNT_LAPTOP,
    [BREAKPOINT_MOBILE]: CARD_COUNT_LAPTOP,
  },
  newsCardsComponent: {
    default: CARD_COUNT_LAPTOP,
    [BREAKPOINT_DESKTOP]: CARD_COUNT_DESKTOP,
    [BREAKPOINT_LAPTOP]: CARD_COUNT_LAPTOP,
    [BREAKPOINT_MOBILE]: CARD_COUNT_LAPTOP,
  },
};

export default cardCountConfigs;
