// Home.tsx

import Image from 'next/image';
import Header from './header';
import Footer from './footer';
import FeatureLink from './featurelink';

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-between min-h-screen p-10 lg:p-24">
      <Header />
      <section className="z-10 flex flex-col items-center w-full max-w-5xl space-y-8">
        <Image
          className="relative dark:drop-shadow-[0_0_0.3rem_#ffffff70]"
          src="/concrete_guy.png"
          alt="meet concrete guy"
          width={540}
          height={96}
          priority
        />
        <div className="grid w-full grid-cols-1 gap-6 mb-10 text-center lg:grid-cols-4 lg:text-left">
          {/* FeatureLinks */}
        </div>
      </section>
      <Footer />
    </main>
  );
}
