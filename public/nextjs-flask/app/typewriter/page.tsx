"use client";

import React from 'react';
import DynamicTextComponent from '../typewriter/dynamic'; // Adjust the import path as necessary

const Page = () => {
  return (
    <DynamicTextComponent
      name="Elijah Arbee"
      interestMessage="thank you for your interest"
      roles={['helpful resource', 'coder', 'tinkerer', 'innovator', 'friend']}
    />
  );
};

export default Page;
