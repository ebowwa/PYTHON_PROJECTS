import Link from "next/link";
import { Button } from "@/components/ui/button";

export default function Component() {
  return (
    <div className="flex flex-col min-h-screen">
      <header className="flex justify-center items-center px-4 py-2 border-b">
        <Link className="flex items-center gap-2" href="#">
          <YoutubeIcon className="h-6 w-6 text-red-500" />{" "}
          <span className="text-lg font-semibold text-red-500">
            YouTube-Short-inator
          </span>{" "}
        </Link>
      </header>
      <main className="flex-1 p-4 md:p-6">
        <div className="flex justify-center items-center gap-4">
          <div className="relative group overflow-hidden rounded-lg border-red-400 border-4 p-4">
            <Link className="absolute inset-0 z-10" href="#">
              <span className="sr-only">View</span>
            </Link>
            <img
              alt="Actual thumbnail of video goes here"
              className="object-cover w-full h-60 rounded-md"
              height={300}
              src="https://images.unsplash.com/photo-1526512340740-9217d0159da9?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dmVydGljYWx8ZW58MHx8MHx8fDA%3D"
              style={{
                objectFit: "cover",
              }}
              width={400}
            />
            <div className="bg-white p-4 dark:bg-gray-950">
              <h3 className="font-semibold text-lg md:text-xl">Video Title</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400">
                15 seconds • 10.5 MB
              </p>
            </div>
          </div>
        </div>
        <div className="mt-8 flex justify-center">
          <Button>I'm ready to share!</Button>
        </div>
      </main>
    </div>
  );
}

function YoutubeIcon(props: any) {
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
      <path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17" />
      <path d="m10 15 5-3-5-3z" />
    </svg>
  );
}
