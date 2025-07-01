"use client"
import { useEffect } from "react"
import { logoutUser } from "@/utils/logout"

export default function LogoutPage() {
  useEffect(() => {
    logoutUser()
  }, [])

  return <p>Logging out...</p>
}
