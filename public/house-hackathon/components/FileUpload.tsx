// src/components/VideoUploader.tsx

import React, { useState } from 'react';
import { uploadVideoFile } from '@/api/videoProcessor';

const VideoUploader: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files[0]) {
      setFile(event.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (file) {
      try {
        const response = await uploadVideoFile(file);
        console.log('Upload successful', response);
        // Handle further actions with response here
      } catch (error) {
        console.error('Upload failed', error);
      }
    }
  };

  return (
    <div className="grid w-full max-w-md items-center gap-4 p-6 bg-white dark:bg-gray-800 rounded-md shadow-md">
      <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">Upload File</h2>
      <form onSubmit={handleSubmit} className="grid w-full items-center gap-1.5">
        <label htmlFor="file" className="text-sm font-medium leading-none">File</label>
        <input id="file" type="file" onChange={handleFileChange} className="flex h-10 w-full rounded-md" />
        <button type="submit" className="inline-flex items-center justify-center h-10 px-4 w-full py-2 bg-blue-500 text-white rounded-md">Submit</button>
      </form>
    </div>
  );
};

export default FileUpload;
