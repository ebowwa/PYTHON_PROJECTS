// components/HeaderSection.tsx

import Link from "next/link";

interface HeaderSectionProps {
  title: string;
  description: string;
}

export const HeaderSection: React.FC<HeaderSectionProps> = ({ title, description }) => {
  return (
    <div className="bg-gray-50/90 py-12 lg:py-24">
      <div className="container px-4 md:px-6">
        <div className="grid max-w-3xl gap-4 mx-auto items-start space-y-4 lg:gap-10 lg:flex lg:items-center lg:space-y-0">
          <div className="space-y-2 text-center lg:text-left">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl">{title}</h1>
            <p className="text-gray-500 dark:text-gray-400">{description}</p>
          </div>
          <div className="flex flex-col gap-2 min-[400px]:flex-row justify-center lg:justify-end">
            <Link className="your-button-class" href="#">Back to assist.org</Link>
            <Link className="your-button-class" href="#">Documentation</Link>
          </div>
        </div>
      </div>
    </div>
  );
};
