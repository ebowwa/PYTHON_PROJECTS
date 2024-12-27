// components/FooterSection.tsx

import Link from "next/link";

export const FooterSection = () => {
  return (
    <footer className="border-t">
      <div className="container flex flex-col gap-4 py-12 md:py-24 lg:py-32 px-4 md:px-6">
        <nav className="flex flex-col gap-2 md:flex-row md:gap-4 lg:gap-0 lg:space-x-4 xl:space-x-6">
          <Link className="your-footer-link-class" href="#">Home</Link>
          <Link className="your-footer-link-class" href="#">API</Link>
          <Link className="your-footer-link-class" href="#">Documentation</Link>
          <Link className="your-footer-link-class" href="#">Support</Link>
        </nav>
      </div>
    </footer>
  );
};
