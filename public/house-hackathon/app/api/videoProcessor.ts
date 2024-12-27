// src/api/videoProcessor.ts

import Backend from '../../lib/backend';

// Assuming the existence of a function to initialize FormData for upload
const prepareUploadData = (file: File): FormData => {
  const formData = new FormData();
  formData.append('file', file);
  return formData;
};

export const uploadVideoFile = async (file: File): Promise<Backend.VideoProcessingResponse> => {
  const formData = prepareUploadData(file);

  const response = await fetch('/upload', {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Failed to upload video');
  }

  const result = await response.json();
  return result as Backend.VideoProcessingResponse;
};
