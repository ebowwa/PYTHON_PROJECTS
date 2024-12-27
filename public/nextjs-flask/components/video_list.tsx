import React, { useEffect, useState } from 'react';

// Define the interface for video objects
interface Video {
  filename: string;
  description: string;
}

const VideoList = () => {
  // Use the Video interface to type the videos state
  const [videos, setVideos] = useState<Video[]>([]);

  useEffect(() => {
    // Fetch the list of processed videos
    fetch('API_ENDPOINT_THAT_LISTS_VIDEOS')
      .then(response => response.json())
      .then((data: Video[]) => setVideos(data)); // Cast the response data to Video[]
  }, []);

  return (
    <div>
      {videos.map(video => (
        <div key={video.filename}>
          <video width="320" height="240" controls>
            <source src={`/api/videos/${video.filename}`} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          <p>{video.description}</p>
        </div>
      ))}
    </div>
  );
};

export default VideoList;
