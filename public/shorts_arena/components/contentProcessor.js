import React, { useState } from 'react';
import useSWR from 'swr';

/**
 * Custom fetcher function for SWR to handle POST requests.
 * @param {string} url - The URL of the API endpoint.
 * @param {Object} data - The data to be sent in the request.
 */
const fetcher = async (url, data) => {
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    const error = new Error('An error occurred while fetching the data.');
    error.info = await response.json();
    error.status = response.status;
    throw error;
  }

  return response.json();
};

/**
 * The ContentProcessor component.
 */
function ContentProcessor() {
  const [inquiry, setInquiry] = useState('');
  const [shouldFetch, setShouldFetch] = useState(false);

  // SWR hook for data fetching
  const { data, error, mutate } = useSWR(
    shouldFetch ? ['/api/process_content', { inquiry }] : null, 
    fetcher, 
    {
      shouldRetryOnError: false,
      revalidateOnFocus: false,
    }
  );

  /**
   * Handles the form submission and triggers the SWR mutate function.
   * @param {Object} e - The event object.
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (inquiry) {
      setShouldFetch(true);
      await mutate();
    }
  };

  /**
   * Renders the loading, error, and data states.
   */
  const renderContent = () => {
    if (error) return <div>Failed to process content: {error.info?.message || error.message}</div>;
    if (!data) return <div>Submit an inquiry to process content</div>;
    return <div>Processed Content: {JSON.stringify(data)}</div>;
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inquiry}
          onChange={(e) => setInquiry(e.target.value)}
          placeholder="Enter your inquiry"
        />
        <button type="submit">Process</button>
      </form>
      {renderContent()}
    </div>
  );
}

export default ContentProcessor;
