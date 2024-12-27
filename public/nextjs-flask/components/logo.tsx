import React from 'react';
import Link from 'next/link'; // Import Link from next/link

const Logo: React.FC = () => {
  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <div className="absolute top-0 left-0 mt-4 ml-4">
        {/* Directly apply Link without wrapping it in an <a> tag */}
        <Link href="/" className="text-xl font-bold" legacyBehavior>
          voiceovers
        </Link>
      </div>
    </div>
  );
};

export default Logo;
