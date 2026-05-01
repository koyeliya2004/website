import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-20 bg-white/80 backdrop-blur border-b border-pink-100">
      <div className="max-w-5xl mx-auto p-4 flex justify-between">
        <h1 className="font-bold text-pink-500">AI Fashion Stylist</h1>
        <div className="space-x-4 text-sm">
          <Link href="/">Home</Link><Link href="/upload">Upload</Link><Link href="/saved-looks">Saved Looks</Link>
        </div>
      </div>
    </nav>
  );
}
