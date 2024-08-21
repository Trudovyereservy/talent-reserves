'use client';

import { useEffect, useState } from 'react';

function useWindowSize(): number {
  const [width, setWidth] = useState<number>(0);
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const handleResize = () => {
        setWidth(window.innerWidth);
      };
      window.addEventListener('resize', handleResize);
      handleResize();
      return () => {
        window.removeEventListener('resize', handleResize);
      };
    }
  }, []);

  return width;
}

export default useWindowSize;
