import Link from 'next/link';
import Navbar from '../components/Navbar';
import WeatherWidget from '../components/WeatherWidget';

export default function Home() {
  return <><Navbar /><main className="max-w-5xl mx-auto p-6"><div className="card bg-blush"><h2 className="text-3xl font-bold">Find your next look ✨</h2><p className="my-2">Upload a selfie and get AI outfit recommendations.</p><Link href="/upload" className="bg-pink-500 text-white px-4 py-2 rounded-full inline-block">Start Styling</Link></div><div className="mt-4"><WeatherWidget /></div></main></>;
}
