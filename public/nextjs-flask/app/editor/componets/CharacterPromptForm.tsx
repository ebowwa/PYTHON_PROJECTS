"use client";
import { useState, useEffect } from 'react';
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { supabase } from '../../../supabase/supabaseClient'; // Adjust the path as necessary

const CharacterPromptForm = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [userId, setUserId] = useState(null);

  useEffect(() => {
    const session = supabase.auth.session; // Access the session directly, not as a function call
    setUserId(session?.user?.id || null);
  }, []);
  

  const handleAddPrompt = async (e) => {
    e.preventDefault();
    // Ensure there's a user signed in before attempting to add a prompt
    if (!userId) {
      console.error("User must be signed in to add prompts");
      return;
    }

    const { data, error } = await supabase
      .from('prompts') // Ensure this is the correct table name
      .insert([{ title, description, user_id: userId }]); // Match these fields to your table's schema
    
    if (error) {
      console.error("Error inserting data: ", error);
    } else {
      console.log("Prompt added successfully: ", data);
      // Optionally reset form fields and provide user feedback
      setTitle('');
      setDescription('');
    }
  };

  return (
    <form onSubmit={handleAddPrompt} className="p-4 border-t">
      <Input
        className="mb-2"
        placeholder="Add new prompt title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <Textarea
        className="mb-2 h-20"
        placeholder="Add new prompt personality and instructions"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <Button className="w-full" type="submit">Add to Library</Button>
    </form>
  );
};

export default CharacterPromptForm;
