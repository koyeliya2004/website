import { useEffect, useState } from 'react';
import Navbar from '../components/Navbar';
import OutfitCard from '../components/OutfitCard';
import MasonryGrid from '../components/MasonryGrid';
import api from '../utils/api';

export default function Results() {
  const [data, setData] = useState(null);
  useEffect(() => { setData(JSON.parse(localStorage.getItem('results') || 'null')); }, []);
  const onSave = async (outfit) => { await api.post('/save-look', { look: outfit }); alert('Saved!'); };
  if (!data) return <><Navbar /><div className="p-6">No results yet.</div></>;
  return <><Navbar /><main className="max-w-5xl mx-auto p-6"><p className="mb-4">Tags: {data.style_tags.join(', ')} | Palette: {data.color_palette.join(' · ')}</p><MasonryGrid>{data.recommendations.map(o => <OutfitCard key={o.id} outfit={o} onSave={onSave} />)}</MasonryGrid></main></>;
}
