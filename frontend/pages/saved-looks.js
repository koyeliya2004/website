import { useEffect, useState } from 'react';
import Navbar from '../components/Navbar';
import OutfitCard from '../components/OutfitCard';
import MasonryGrid from '../components/MasonryGrid';
import api from '../utils/api';

export default function SavedLooks() {
  const [looks, setLooks] = useState([]);
  useEffect(() => { api.get('/saved-looks').then(r => setLooks(r.data)); }, []);
  return <><Navbar /><main className="max-w-5xl mx-auto p-6"><h2 className="text-xl font-semibold mb-4">Saved Looks</h2><MasonryGrid>{looks.map((o, i) => <OutfitCard key={i} outfit={o} onSave={() => {}} />)}</MasonryGrid></main></>;
}
