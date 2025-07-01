'use client'

import { useState } from 'react'

type Props = {
  type: 'login' | 'register'
  onSubmit: (email: string, password: string) => void
}

export default function AuthForm({ type, onSubmit }: Props) {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  return (
    <form
      className="max-w-md mx-auto space-y-4 p-6 border rounded-xl mt-10"
      onSubmit={(e) => {
        e.preventDefault()
        onSubmit(email, password)
      }}
    >
      <h2 className="text-xl font-bold text-center">
        {type === 'login' ? 'Login' : 'Register'}
      </h2>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="w-full p-2 border rounded"
        required
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="w-full p-2 border rounded"
        required
      />
      <button type="submit" className="w-full p-2 bg-black text-white rounded">
        {type === 'login' ? 'Login' : 'Register'}
      </button>
    </form>
  )
}
