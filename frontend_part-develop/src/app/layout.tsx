import type { Metadata } from 'next';

import { Roboto, Inter } from 'next/font/google';

import { Footer } from '@/components/Footer/Footer';
import { Header } from '@/components/Header/Header';

import '../styles/globals.scss';

const roboto = Roboto({
  subsets: ['latin'],
  style: 'normal',
  display: 'swap',
  variable: '--font-roboto',
  weight: ['400', '500', '700'],
});
const inter = Inter({
  weight: '400',
  style: 'normal',
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

export const metadata: Metadata = {
  title: { absolute: 'Трудовые резервы' },
  description:
    'Общественно полезный фонд кадрового и спортивно-культурного развития “Трудовые резервы”',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="ru" className={`${inter.variable} ${roboto.variable}`}>
      <body>
        <div className="page__wrapper">
          <Header />
          <main>{children}</main>
          <Footer />
        </div>
      </body>
    </html>
  );
}
