'use server';

import { Groq } from 'groq-sdk';

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
});

export async function translateAudio(file: File, model: string) {
    const [arrayBuffer, text] = await Promise.all([
      file.arrayBuffer(),
      file.text(),
    ]);
  
    const uploadable: Uploadable = {
      name: file.name,
      size: file.size,
      type: file.type,
      lastModified: file.lastModified,
      arrayBuffer: async () => arrayBuffer,
      text: async () => text,
      slice: (start, end) => new Blob([arrayBuffer], { type: file.type }).slice(start, end),
    };
  
    const translation = await groq.audio.translations.create({
      file: uploadable,
      model: model || 'whisper-large-v3',
    });
  
    return { text: translation.text };
  }


export async function generateResponse(prompt: string, model: string = 'llama3-8b-8192') {
  const chatCompletion = await groq.chat.completions.create({
    messages: [
      {
        role: 'user',
        content: prompt,
      },
    ],
    model: model,
  });

  return { content: chatCompletion.choices[0]?.message?.content || '' };
}

interface Uploadable {
  name: string;
  size: number;
  type: string;
  lastModified: number;
  arrayBuffer: () => Promise<ArrayBuffer>;
  text: () => Promise<string>;
  slice: (start: number, end: number) => Blob;
}