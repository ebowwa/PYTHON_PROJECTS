// app/editor/AudioLibrary.tsx
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from '@/components/ui/textarea'

// app/editor/AudioLibrary.tsx
import React, { useState, useEffect } from 'react';
import { SupabaseClient } from '@supabase/supabase-js';
import { useSupabase } from '@/hooks/useSupabase'; // Assuming this hook initializes and provides the Supabase client

interface Track {
  id: number;
  title: string;
  description: string;
}

interface AudioLibraryProps {
  onSelect: (audioTitle: string) => void;
}

export const AudioLibrary: React.FC<AudioLibraryProps> = ({ onSelect }) => {
  const [tracks, setTracks] = useState<Track[]>([]);
  const [newTitle, setNewTitle] = useState('');
  const [newDescription, setNewDescription] = useState('');
  const supabase: SupabaseClient = useSupabase();

  // Function to fetch tracks from Supabase
  const fetchTracks = async () => {
    let { data: tracks, error } = await supabase
      .from('tracks')
      .select('*');

    if (error) console.error('Error fetching tracks:', error);
    else setTracks(tracks);
  };

  useEffect(() => {
    fetchTracks();
  }, []);

  const handleAddTrack = async () => {
    const { data, error } = await supabase
      .from('tracks')
      .insert([
        { title: newTitle, description: newDescription, userId: supabase.auth.user()?.id }
      ]);

    if (error) {
      console.error("Error adding new track:", error);
    } else {
      setTracks([...tracks, ...data]);
      sendTrackToServer(data[0]);
      setNewTitle('');
      setNewDescription('');
    }
  };

  // Function to send track to the server
  const sendTrackToServer = async (track: Track) => {
    try {
      const response = await fetch('/api/tracks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(track),
      });

      if (!response.ok) {
        throw new Error(`Error: ${response.statusText}`);
      }

      const result = await response.json();
      console.log('Track successfully sent to the server:', result);
    } catch (error) {
      console.error('Failed to send track to the server:', error);
    }
  };

  return (
    <div className="flex flex-col h-full overflow-auto">
      {/* UI elements for listing tracks and adding a new track */}
      {tracks.map((track, index) => (
        <div key={index} onClick={() => onSelect(track.title)} className="p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800">
          <h3 className="font-medium">{track.title}</h3>
        </div>
      ))}
      <div className="p-4 border-t">
        <Input className="mb-2" value={newTitle} onChange={(e) => setNewTitle(e.target.value)} placeholder="New audio track title" />
        <Textarea className="mb-2" value={newDescription} onChange={(e) => setNewDescription(e.target.value)} placeholder="New audio track description" />
        <Button className="w-full" onClick={handleAddTrack}>Add to Library</Button>
      </div>
    </div>
  );
};
