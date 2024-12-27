/**
 * v0 by Vercel.
 * @see https://v0.dev/t/CdJCcquKrqx
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import Link from "next/link"
import { CardTitle, CardDescription, CardHeader, CardContent, CardFooter, Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import SiteDirectoryMenu from '@/components/dropdown_menu'; // Assuming SiteDirectoryMenu is a default export


export default function Component() {
  return (
    <div className="flex flex-col min-h-[100vh]">
      <header className="px-4 lg:px-6 h-14 flex items-center">
        <Link className="flex items-center justify-center" href="#">
          <MicIcon className="h-6 w-6" />
          <span className="ml-2 text-lg font-bold">VoiceOver AI</span>
        </Link>
        <div className="absolute top-0 right-0 mt-4 mr-4">
          <SiteDirectoryMenu />
        </div>
      </header>
      <p className="mt-2"> </p>
      <p className="mt-2"> </p>
      <p className="mt-2"> </p>
      <p className="mt-2"> </p>
      <p className="mt-2"> </p>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl">
                  Bring your content to life with AI
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                  Our AI-powered voiceover service creates realistic audio for your content. Perfect for podcasts,
                  audiobooks, and more.
                </p>
              </div>
              <div className="space-x-4">
                <Link
                  className="inline-flex h-9 items-center justify-center rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                  href="/signin"
                >
                  Get Started
                </Link>
                <Link
                  className="inline-flex h-9 items-center justify-center rounded-md border border-gray-200 px-4 py-2 text-sm font-medium shadow-sm transition-colors hover:bg-gray-100 hover:text-gray-900 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300"
                  href="#"
                >
                  Learn more
                </Link>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800" id="features">
          <div className="container px-4 md:px-6">
            <div className="grid items-center gap-6 lg:grid-cols-[1fr_500px] lg:gap-12 xl:grid-cols-[1fr_550px]">
              <img
                alt="Image"
                className="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full lg:order-last"
                height="310"
                src="/placeholder.svg"
                width="550"
              />
              <div className="flex flex-col justify-center space-y-4">
                <div className="space-y-2">
                  <div className="inline-block rounded-lg bg-gray-100 px-3 py-1 text-sm dark:bg-gray-800">Features</div>
                  <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">AI-Powered Voiceovers</h2>
                  <p className="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                    Our AI-powered voiceover service creates realistic audio for your content. Perfect for podcasts,
                    audiobooks, and more.
                  </p>
                </div>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Link
                    className="inline-flex h-10 items-center justify-center rounded-md bg-gray-900 px-8 text-sm font-medium text-gray-50 shadow transition-colors hover:bg-gray-900/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:bg-gray-50 dark:text-gray-900 dark:hover:bg-gray-50/90 dark:focus-visible:ring-gray-300"
                    href="#"
                  >
                    Learn More
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32" id="pricing">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
                  Simple, transparent pricing
                </h2>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Choose a subscription plan that best fits your needs. No hidden fees, cancel anytime.
                </p>
              </div>
              <div className="grid w-full grid-cols-1 md:grid-cols-3 items-center justify-center gap-8 lg:gap-12 [&>img]:mx-auto">
                <Card>
                  <CardHeader>
                    <CardTitle>Free</CardTitle>
                    <CardDescription>$0.00 /month</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul>
                      <li>Up to three Demos a day</li>
                      <li>Standard quality</li>
                      <li>Email support</li>
                    </ul>
                  </CardContent>
                  <CardFooter>
                    <Button>Choose Plan</Button>
                  </CardFooter>
                </Card>
                <Card>
                  <CardHeader>
                    <CardTitle>Pro</CardTitle>
                    <CardDescription>$5/month</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul>
                      <li>Up to 10 minutes of short clips</li>
                      <li>High quality</li>
                      <li>Early Feature Access</li>
                    </ul>
                  </CardContent>
                  <CardFooter>
                    <Button>Choose Plan</Button>
                  </CardFooter>
                </Card>
                <Card>
                  <CardHeader>
                    <CardTitle>Enterprise</CardTitle>
                    <CardDescription>Contact us</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul>
                      <li>Unlimited hours</li>
                      <li>High quality</li>
                      <li>Priority email support</li>
                      <li>API access</li>
                    </ul>
                  </CardContent>
                  <CardFooter>
                    <Button>Contact Us</Button>
                  </CardFooter>
                </Card>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800" id="contact">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Contact Us</h2>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                  Have any questions or need help? Get in touch with us.
                </p>
              </div>
              <div className="w-full max-w-md space-y-4">
                <form className="flex flex-col space-y-4">
                  <Input className="max-w-lg flex-1" placeholder="Name" type="text" />
                  <Input className="max-w-lg flex-1" placeholder="Email" type="email" />
                  <textarea
                    className="max-w-lg flex-1 h-32 p-2 rounded-md border border-gray-200 dark:border-gray-800"
                    placeholder="Message"
                  />
                  <Button type="submit">Send Message</Button>
                </form>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  )
}

function MicIcon(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
      <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
      <line x1="12" x2="12" y1="19" y2="22" />
    </svg>
  )
}
