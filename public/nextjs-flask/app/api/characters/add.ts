// app/api/audioTracks/add.ts
import type { NextApiRequest, NextApiResponse } from 'next';
import { supabase } from '../../../supabase/supabaseClient'; // Adjust the path as necessary

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method === 'POST') {
    const { title, description } = req.body;

    const { data, error } = await supabase
      .from('audio_tracks')
      .insert([
        { title, description },
      ]);

    if (error) {
      return res.status(400).json({ error });
    }

    return res.status(200).json({ data });
  } else {
    // Handle any other HTTP method
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
