"use client";
import React from 'react';
import Logo from '@/components/logo'; // Assuming Logo is a default export
import SiteDirectoryMenu from '@/components/dropdown_menu'; // Assuming SiteDirectoryMenu is a default export
import FileUploadForm from './fileUpload'; // Adjust the path as necessary

const UploadPage = () => {
  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <Logo />
      <div className="absolute top-0 right-0 mt-4 mr-4">
        <SiteDirectoryMenu />
      </div>
      <div className="flex justify-center items-center flex-grow">
        <FileUploadForm />
      </div>
    </div>
  );
};

export default UploadPage;
