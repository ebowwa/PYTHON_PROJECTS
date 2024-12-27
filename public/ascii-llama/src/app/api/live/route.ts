// app/api/llm/route.ts
import { NextRequest, NextResponse } from 'next/server';
import { createReadStream } from 'fs';
import { Groq } from 'groq-sdk';

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
});

export async function POST(request: NextRequest) {
  try {
    const { file, model, prompt } = await request.json();
    let translation;
    let chatCompletion;

    if (file) {
      const fileStream = createReadStream(file);
      translation = await groq.audio.translations.create({
        file: fileStream,
        model: model || 'whisper-large-v3',
      });
    }

    if (prompt) {
      chatCompletion = await getGroqChatCompletion(prompt, model);
    }

    return NextResponse.json({
      translation: translation?.text,
      chatCompletion: chatCompletion?.choices[0]?.message?.content || '',
    });
  } catch (error) {
    console.error(error);
    return NextResponse.json({ error: 'Failed to create translation or get chat completion' }, { status: 500 });
  }
}

async function getGroqChatCompletion(prompt: string, model: string = 'llama3-8b-8192') {
  return groq.chat.completions.create({
    messages: [
      {
        role: 'user',
        content: prompt,
      },
    ],
    model: model,
  });
}