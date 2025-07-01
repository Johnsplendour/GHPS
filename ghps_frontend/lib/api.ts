const BASE_URL = 'http://127.0.0.1:8000/api'

export async function register(email: string, password: string) {
  const res = await fetch(`${BASE_URL}/register/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: email, password })
  })

  if (!res.ok) throw new Error('Registration failed')
  return res.json()
}

export async function login(email: string, password: string) {
  const res = await fetch(`${BASE_URL}/token/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username: email, password })
  })

  if (!res.ok) throw new Error('Login failed')
  return res.json() // contains access & refresh tokens
}
