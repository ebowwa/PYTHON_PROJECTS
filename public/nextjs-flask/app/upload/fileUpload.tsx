"use client";
import React, { useState } from 'react';
import axios from 'axios';
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { UploadCloudIcon } from 'lucide-react';

function FileUploadForm() {
  const [file, setFile] = useState<File | null>(null);
  const [uploadStatus, setUploadStatus] = useState('');

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files ? event.target.files[0] : null;
    setFile(file);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!file) {
      alert('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:3000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.output_video_path) {
        setUploadStatus(`Upload successful! Video processed at: ${response.data.output_video_path}`);
      } else {
        setUploadStatus('Upload failed.');
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      setUploadStatus('Error uploading file.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col w-full max-w-md items-center space-y-4">
      <div className="flex w-full items-center space-x-2">
        <Label htmlFor="url" className="min-w-[80px]">URL:</Label>
        <Input className="flex-grow" id="url" placeholder="Enter URL" type="text" />
      </div>
      <div className="flex w-full items-center space-x-2">
        <Label htmlFor="file" className="min-w-[80px]">File:</Label>
        <input className="flex-grow" id="file" type="file" onChange={handleFileChange} />
      </div>
      <Button type="submit" className="flex items-center space-x-2">
        <UploadCloudIcon className="h-5 w-5" />
        <span>Upload</span>
      </Button>
      {uploadStatus && <div className="mt-4 text-center">{uploadStatus}</div>}
    </form>
  );
}

export default FileUploadForm;
