import EmailForm from "@/components/(sections)/splash-waitlist/EmailFom";
import Image from "next/image";
import { Toaster } from "react-hot-toast";

export default function Home() {
  return (
    <>
      <Toaster />

      <section className="w-screen h-screen grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="md:h-full h-80 bg-[#FCD0A1] relative overflow-hidden">
          <Image
            src="/IMG_1570.png"
            alt="Mobile App Screenshots"
            fill
            className="object-contain mt-8 md:mt-24 px-14 object-bottom"
          />
        </div>

        <main className="flex flex-col gap-8 mt-8 justify-center px-6 pb-10">
          <h1 className="font-semibold tracking-tight text-zinc-900 text-3xl leading-tight md:text-4xl max-w-lg">
            Discover What Your Pet is Trying to Tell You
          </h1>
          <p className="text-gray-500">
            Imagine understanding your pet's every need, want, and emotion. No more guessing, no more wondering.
          </p>

          <p className="text-gray-500">
            Our revolutionary AI Pet Communication Collar makes it possible. Join our waitlist to be the first to experience the future of pet communication.
          </p>

          <EmailForm />
        </main>
      </section>
    </>
  );
}
