"use client";

import React from 'react';
import * as DropdownMenu from '@radix-ui/react-dropdown-menu';
import { HamburgerMenuIcon, ChevronRightIcon, CheckIcon } from '@radix-ui/react-icons';
import Link from 'next/link'; // Importing Link from next/link

const SiteDirectoryMenu = () => {
  return (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild>
        <button
          className="rounded-full w-[35px] h-[35px] inline-flex items-center justify-center text-violet11 bg-white shadow-[0_2px_10px] shadow-blackA4 outline-none hover:bg-violet3 focus:shadow-[0_0_0_2px] focus:shadow-black"
          aria-label="Open site directory"
        >
          <HamburgerMenuIcon />
        </button>
      </DropdownMenu.Trigger>

      <DropdownMenu.Portal>
        <DropdownMenu.Content
          className="min-w-[220px] bg-gray-100 rounded-lg p-4 shadow-sm border border-gray-200"
          sideOffset={5}
        >
          {/* Wrapped DropdownMenu.Item with Link */}
          <Link href="/" passHref><DropdownMenu.Item className="dropdown-item">Home</DropdownMenu.Item></Link>
          <Link href="/pricing" passHref><DropdownMenu.Item className="dropdown-item">Pricing</DropdownMenu.Item></Link>
          <Link href="/team" passHref><DropdownMenu.Item className="dropdown-item">Team</DropdownMenu.Item></Link>

          {/* For nested dropdowns, consider using onClick handlers to navigate or keep as is if deeper navigation structure is intended */}
          <DropdownMenu.Sub>
            <DropdownMenu.SubTrigger className="dropdown-trigger">Store</DropdownMenu.SubTrigger>
            <DropdownMenu.SubContent className="dropdown-content">
              <Link href="/store/all-products" passHref><DropdownMenu.Item className="dropdown-item">All Products</DropdownMenu.Item></Link>
              <Link href="/store/new-arrivals" passHref><DropdownMenu.Item className="dropdown-item">New Arrivals</DropdownMenu.Item></Link>
              <Link href="/store/best-sellers" passHref><DropdownMenu.Item className="dropdown-item">Best Sellers</DropdownMenu.Item></Link>
            </DropdownMenu.SubContent>
          </DropdownMenu.Sub>

          {/* Documentation section with nested dropdown */}
          <DropdownMenu.Sub>
            <DropdownMenu.SubTrigger className="dropdown-trigger">Documentation</DropdownMenu.SubTrigger>
            <DropdownMenu.SubContent className="dropdown-content">
              <Link href="/documentation/api-docs" passHref><DropdownMenu.Item className="dropdown-item">API Docs</DropdownMenu.Item></Link>
              <Link href="/documentation/component-usage" passHref><DropdownMenu.Item className="dropdown-item">Component Usage</DropdownMenu.Item></Link>
            </DropdownMenu.SubContent>
          </DropdownMenu.Sub>

          <Link href="/login" passHref><DropdownMenu.Item className="dropdown-item">Login</DropdownMenu.Item></Link>
          <Link href="/share" passHref><DropdownMenu.Item className="dropdown-item">Share</DropdownMenu.Item></Link>
          <Link href="/affiliate-program" passHref><DropdownMenu.Item className="dropdown-item">Affiliate Program</DropdownMenu.Item></Link>
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  );
};

export default SiteDirectoryMenu;
//           <Link href="/signup" passHref><DropdownMenu.Item className="dropdown-item">Sign Up</DropdownMenu.Item></Link>
