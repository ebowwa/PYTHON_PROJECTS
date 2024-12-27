"use client";

import { useState, useEffect } from 'react';
import { useSupabase } from '@/app/supabase-provider';

const AudioTrackList = () => {
  const [prompts, setPrompts] = useState<{ id: string, title: string, description: string }[]>([]);
  const { supabase } = useSupabase();

  useEffect(() => {
    const fetchPrompts = async () => {
      // Fetch the current session and then get the user details from the session
      const session = supabase.auth.session();
      const user = session?.user;

      if (!user) {
        console.error('No user logged in');
        return;
      }

      // Adjust the query to filter prompts based on the user's ID or other criteria
      const { data, error } = await supabase
        .from('prompts')
        .select('*')
        .eq('user_id', user.id) // Assuming prompts have a 'user_id' field to filter by
        .order('created_at', { ascending: false });

      if (error) {
        console.error('Error fetching prompts:', error);
        return;
      }

      setPrompts(data);
    };

    fetchPrompts();
  }, [supabase]);

  return (
    <div className="flex-1 overflow-auto p-4 space-y-2">
      {prompts.map((prompt) => (
        <div key={prompt.id} className="p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800">
          <h3 className="font-medium">{prompt.title}</h3>
          <p>{prompt.description}</p>
        </div>
      ))}
    </div>
  );
};

export default AudioTrackList;
