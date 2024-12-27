// app/components/ui/Header.tsx
import Link from "next/link";
import { MicIcon } from "../icons/mic"; // Ensure the path to MicIcon is correct for your project structure

const Header = () => {
  return (
    <header className="px-4 lg:px-6 h-14 flex items-center">
      <Link className="flex items-center justify-center" href="/signin">
        <MicIcon className="h-6 w-6" />
        <span className="ml-2 text-lg font-bold">VoiceOvers AI</span>
      </Link>
    </header>
  );
};

export default Header;
