"use client";
import React from 'react';
import  ContentProcessor from "@/components/contentProcessor";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Component() {
  return (
    <main className="flex flex-col items-center justify-center h-screen px-4 py-12 bg-gray-100 dark:bg-gray-900">
      <div className="text-center space-y-4">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100">
          YouTube-Short-inator
        </h1>
        <p className="text-gray-600 dark:text-gray-400">
          Create the perfect YouTube Short in an instant, with the power of AI
        </p>
      </div>
      <ContentProcessor />
    </main>
  );
}
