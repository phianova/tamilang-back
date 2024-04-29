"use client";

import { useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";

import Image from "next/image";
import LetterCard from "../components/LetterCard";
import ApiClient from "../utils/apiClient";

export default function Home() {
  const [letters, setLetters] = useState(null);
  const router = useRouter();
  // const params = useSearchParams();
  const client = new ApiClient();

  const getLetterFunction = () => {
    client.getLetters().then((data) => {
      setLetters(data);
    })
  }

  useEffect(() => {
    getLetterFunction();
  })

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1>Tamilang</h1>
      <button onClick={getLetterFunction}>View all letters</button>
      {letters && letters.map((letter) => <LetterCard key={letter.id} {...letter} />)}
    </main>
  );
}
