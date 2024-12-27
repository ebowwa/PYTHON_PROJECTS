// Importing necessary components and hooks
import './globals.css'
import { Inter } from 'next/font/google'
import { Toaster } from "@/components/ui/toaster"; // Import the Toaster component
import SupabaseProvider from './supabase-provider';


const inter = Inter({ subsets: ['latin'] }) // Loading the Inter font with 'latin' subset

export const meta = {
  title: 'voiceovers',
  description: '"Enhance your digital content with Voiceovers – the premier AI voiceover application designed to revolutionize video productions. Powered by cutting-edge artificial intelligence, Voiceovers offers an intuitive platform for adding lifelike, customizable voiceovers to any video, making it perfect for content creators, marketers, and educators seeking to elevate their media presence. Our user-friendly interface ensures seamless integration of high-quality audio into your projects, transforming your videos with engaging narrations that captivate your audience. Unlock the potential of your videos with Voiceovers, where innovation meets creativity."',
  cardImage: '/og.png',
  robots: 'follow, index',
  favicon: '/favicon.ico',
  url: 'https://subscription-starter.vercel.app',
  type: 'website'
}

export const metadata = {
  title: meta.title,
  description: meta.description,
  cardImage: meta.cardImage,
  robots: meta.robots,
  favicon: meta.favicon,
  url: meta.url,
  type: meta.type,
  openGraph: {
    url: meta.url,
    title: meta.title,
    description: meta.description,
    cardImage: meta.cardImage,
    type: meta.type,
    site_name: meta.title
  },
  twitter: {
    card: 'summary_large_image',
    site: '@vercel',
    title: meta.title,
    description: meta.description,
    cardImage: meta.cardImage
  }
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <SupabaseProvider>
        <main>{children}</main> {/* Main content area where child components will be rendered */}
        <Toaster /> {/* Placement of the Toaster component */}
        </SupabaseProvider>
      </body>
    </html>
  )
}
