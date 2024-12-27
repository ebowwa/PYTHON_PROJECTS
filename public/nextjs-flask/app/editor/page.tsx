// app/editor/page.tsx
"use client";

import { NextPage } from 'next';
import AudioTrackList from './componets/ChracterList';
import AudioTranscriptionList from './componets/voiceoverTranscriptionList';
import AddAudioForm from './componets/CharacterPromptForm';
import Logo from '@/components/logo'; // Assuming you're still using the Logo component
import { Button } from "@/components/ui/button"; // Import the Button component
import SiteDirectoryMenu from '@/components/dropdown_menu'; // Assuming SiteDirectoryMenu is a default export

const EditorPage: NextPage = () => {
  return (
    <div className="grid h-screen grid-cols-[300px_1fr] gap-4">
      <div className="flex flex-col h-full overflow-auto">
        <div className="p-4">
          <h2 className="text-lg font-semibold">Character Library</h2>
          <p className="text-sm text-gray-500 dark:text-gray-400">Select a character to overlay on your video.</p>
        </div>
        <AudioTrackList />
        <AddAudioForm />
      </div>
      <div className="flex flex-col h-full overflow-auto">
        <div className="p-4">
          <h2 className="text-lg font-semibold">Audio Transcription</h2>
          <p className="text-sm text-gray-500 dark:text-gray-400">Review the transcriptions of your audio tracks.</p>
        </div>
        <AudioTranscriptionList />
        <div className="p-4 border-t">
          <Button className="w-full">Preview Transcription</Button>
        </div>
      </div>
    </div>
  );
};

export default EditorPage;
