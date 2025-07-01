"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"

const navItems = [
  { label: "Home", href: "/" },
  { label: "Learn", href: "/learn" },
  { label: "Order", href: "/order" },
  { label: "Ask AI", href: "/ask" },
  { label: "Login", href: "/auth/login" },
  { label: "Register", href: "/auth/register" },
]

export default function Navbar() {
  const pathname = usePathname()

  return (
    <nav className="sticky top-0 z-50 w-full px-4 py-3 shadow-sm bg-white text-black">
      <div className="max-w-6xl mx-auto flex items-center justify-between">
        <Link href="/" className="text-xl font-bold">
          GhPs
        </Link>
        <div className="flex space-x-4">
          {navItems.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className={`text-sm font-medium ${
                pathname === item.href ? "text-blue-600" : "text-gray-700"
              } hover:text-blue-600`}
            >
              {item.label}
            </Link>
          ))}
        </div>
      </div>
    </nav>
  )
}
