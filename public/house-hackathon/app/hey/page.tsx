// app/example/page.tsx
"use client";

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import 'tailwindcss/tailwind.css';

const InitialComponent = () => (
  <div className="p-4 bg-gray-200 rounded-lg">
    <h1 className="text-xl font-bold">This is the initial component</h1>
    {/* Other content */}
  </div>
);

const NewComponent = () => (
  <div className="p-4 bg-blue-200 rounded-lg">
    <h1 className="text-xl font-bold">This is the new component</h1>
    {/* Other content */}
  </div>
);

const ExamplePage = () => {
  const [showNewComponent, setShowNewComponent] = useState(false);

  const handleClick = () => {
    setShowNewComponent(true);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <div className="w-full max-w-md">
        {showNewComponent ? <NewComponent /> : <InitialComponent />}
        {!showNewComponent && (
          <Button 
            className="mt-4" 
            onClick={handleClick}>
            Load New Component
          </Button>
        )}
      </div>
    </div>
  );
};

export default ExamplePage;
