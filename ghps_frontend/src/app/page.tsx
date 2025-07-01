"use client"

import Link from "next/link"

export default function Home() {
  return (
    <div className="min-h-screen bg-white text-black">
      {/* Hero Section */}
      <section className="relative bg-gray-100 py-20 px-6 text-center">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-4xl md:text-5xl font-bold mb-4">
            Your Poultry Platform
          </h1>
          <p className="text-lg md:text-xl mb-6">
            Learn poultry farming, order products, and connect with farms.
          </p>
          <Link
            href="/auth/register"
            className="bg-black text-white py-2 px-6 rounded hover:bg-gray-800 transition"
          >
            Get Started
          </Link>
        </div>
        <div className="absolute top-0 right-0 bottom-0 left-0 -z-10">
          <img
            src="/images/hero.jpg"
            alt="Hero background"
            className="w-full h-full object-cover opacity-30"
          />
        </div>
      </section>

      {/* Features Section */}
      <section className="max-w-6xl mx-auto py-16 px-6">
        <h2 className="text-3xl font-bold text-center mb-10">
          What You Can Do
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="bg-white rounded-2xl p-6 shadow-md hover:shadow-xl transform hover:-translate-y-1 transition-all border border-gray-200"
            >
              <img
                src={feature.image}
                alt={feature.title}
                className="w-full h-40 object-cover rounded-xl mb-4"
              />
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.description}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}

const features = [
  {
    title: "Order Chicks",
    description: "Get high-quality day-old chicks from trusted farms.",
    image: "/images/chicks.jpg",
  },
  {
    title: "Learn Poultry",
    description: "Step-by-step guides for every stage of poultry farming.",
    image: "/images/learn.jpg",
  },
  {
    title: "Nearby Farms",
    description: "Find and connect with poultry farms near you.",
    image: "/images/map.jpg",
  },
]
