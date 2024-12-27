import { NextRequest, NextResponse } from 'next/server';
import { Groq } from 'groq-sdk';

export const runtime = "edge";

const groq = new Groq({
  apiKey: process.env.GROQ_API_KEY,
});

export async function POST(request: NextRequest) {
  try {
    const { prompt, model } = await request.json();
    const chatCompletion = await getGroqChatCompletion(prompt, model);
    return NextResponse.json({
      content: chatCompletion.choices[0]?.message?.content || '',
    });
  } catch (error) {
    console.error(error);
    return NextResponse.json({ error: 'Failed to get chat completion' }, { status: 500 });
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