// app/page.tsx
"use client"; // Ensures this page is treated as a client-side only component
// app/page.tsx
import { useState } from 'react';

export default function HomePage() {
  const [uploading, setUploading] = useState(false);
  const [uploadResult, setUploadResult] = useState('');

  const handleUpload = async () => {
    const fileInput = document.getElementById('file') as HTMLInputElement;
    if (!fileInput.files || fileInput.files.length === 0) {
      alert('Please select a file to upload');
      return;
    }
    const file = fileInput.files[0];

    // Prepare form data
    const formData = new FormData();
    formData.append('file', file);

    try {
      setUploading(true);
      // Make the request to the Flask backend
      const response = await fetch('https://house-hackathon-git-main-ebowwa.vercel.app/upload', {
        method: 'POST',
        body: formData,
      });

      const result = await response.json();
      if (response.ok) {
        setUploadResult('Success: ' + result.message);
        // Handle success scenario, such as displaying the result or redirecting the user
      } else {
        setUploadResult('Error: ' + (result.error || 'File upload failed'));
        // Handle error scenario
      }
    } catch (error) {
      console.error('Upload error:', error);
      setUploadResult('Error: Upload failed due to a network or server error.');
    } finally {
      setUploading(false);
    }
  };

  return (
    <main className="flex min-h-screen items-center justify-center p-24">
      <section className="flex w-full max-w-md flex-col items-center space-y-4">
        <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-200">Upload File</h2>
        
        {/* File input */}
        <div className="grid w-full items-center gap-1.5">
          <label htmlFor="file" className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">File</label>
          <input className="form-input" id="file" type="file" />
        </div>

        {/* URL input */}
        <div className="grid w-full items-center gap-1.5">
          <label htmlFor="url" className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">URL</label>
          <input className="form-input" id="url" placeholder="Enter URL" type="text" />
        </div>

        {/* Submit button */}
        <button 
          className={`btn-primary ${uploading ? 'bg-gray-500' : ''}`} 
          type="button" 
          onClick={handleUpload} 
          disabled={uploading}>
          {uploading ? 'Uploading...' : 'Upload'}
        </button>

        {/* Upload result */}
        {uploadResult && <div className="mt-4 text-center text-sm">{uploadResult}</div>}
      </section>
    </main>
  );
}