/**
 * v0 by Vercel.
 * @see https://v0.dev/t/sSucORtbDp0
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
import React from 'react';

// Assuming these components are available in the specified path
import { Carousel, CarouselContent, CarouselItem, CarouselPrevious, CarouselNext } from "@/components/ui/carousel";

export default function Component() {
  return (
    <section className="w-full py-12 md:py-24 lg:py-32">
      <div className="container grid items-center justify-center gap-4 px-4 text-center md:px-6 lg:gap-10">
        <div className="space-y-3">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Featured On</h2>
          <p className="mx-auto max-w-[700px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
            Our products and services have been recognized by industry leaders and trusted by top companies.
          </p>
        </div>
        <Carousel className="w-full max-w-6xl">
          <CarouselContent>
            <CarouselItem>
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 lg:gap-10">
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
              </div>
            </CarouselItem>
            <CarouselItem>
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 lg:gap-10">
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
                <div className="flex items-center justify-center">
                  <img
                    src="/placeholder.svg"
                    width="140"
                    height="70"
                    alt="Logo"
                    className="aspect-[2/1] overflow-hidden rounded-lg object-contain object-center transition-transform duration-300 ease-in-out transform hover:-translate-y-2 hover:scale-105"
                  />
                </div>
              </div>
            </CarouselItem>
          </CarouselContent>
          <CarouselPrevious />
          <CarouselNext />
        </Carousel>
      </div>
    </section>
  );
}