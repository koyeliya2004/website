import { useState } from 'react';
import { useRouter } from 'next/router';
import Navbar from '../components/Navbar';
import ImageUploader from '../components/ImageUploader';
import MoodSelector from '../components/MoodSelector';
import FilterButtons from '../components/FilterButtons';
import api from '../utils/api';

export default function UploadPage() {
  const [file, setFile] = useState(null); const [style, setStyle] = useState(''); const [mood, setMood] = useState(''); const [weather, setWeather] = useState(''); const [loading, setLoading] = useState(false);
  const router = useRouter();
  const submit = async () => {
    if (!file) return;
    setLoading(true);
    const fd = new FormData(); fd.append('file', file);
    const up = await api.post('/upload', fd, { headers: { 'Content-Type': 'multipart/form-data' } });
    const rec = await api.post('/recommend', { image_path: up.data.image_path, style, mood, weather });
    localStorage.setItem('results', JSON.stringify(rec.data));
    router.push('/results');
  };
  return <><Navbar /><main className="max-w-3xl mx-auto p-6 space-y-4"><ImageUploader onFile={setFile} /><FilterButtons options={['soft girl','aesthetic','anime','casual','office','party']} value={style} onChange={setStyle}/><MoodSelector value={mood} onChange={setMood}/><FilterButtons options={['hot','cold','rainy']} value={weather} onChange={setWeather}/><button onClick={submit} className="bg-pink-500 text-white px-4 py-2 rounded-full">{loading ? 'Styling...' : 'Get Recommendations'}</button></main></>;
}
