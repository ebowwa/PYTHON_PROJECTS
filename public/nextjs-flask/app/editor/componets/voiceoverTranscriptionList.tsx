// app/audioLibrary/components/AudioTranscriptionList.tsx
"use client";

const AudioTranscriptionList = () => {
  return (
    <div className="flex-1 overflow-auto p-4 space-y-2">
      {/* List of transcriptions */}
      <div className="p-2 rounded-md hover:bg-gray-100 dark:hover:bg-gray-800">
        <h3 className="font-medium">Time: 00:01:23</h3>
        <p className="text-sm text-gray-500 dark:text-gray-400">"Hello, welcome to our podcast."</p>
      </div>
      {/* Additional transcriptions omitted for brevity */}
    </div>
  );
};

export default AudioTranscriptionList;
