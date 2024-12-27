// pages/api/addAudioTrack.js
import { createClient } from '@supabase/supabase-js';

const supabaseAdmin = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY
);

export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { title, description } = req.body;
    
    const { data, error } = await supabaseAdmin
      .from('audio_tracks')
      .insert([{ title, description }]);
    
    if (error) return res.status(400).json({ error });
    res.status(200).json(data);
  } else {
    // Handle any other HTTP method
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
