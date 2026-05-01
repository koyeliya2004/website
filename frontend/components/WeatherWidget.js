import { useEffect, useState } from 'react';
import api from '../utils/api';

export default function WeatherWidget() {
  const [w, setW] = useState(null);
  useEffect(() => { api.get('/weather?city=New York').then(r => setW(r.data)); }, []);
  if (!w) return <div className="card">Loading weather...</div>;
  return <div className="card">Weather in {w.city}: <b>{w.weather}</b> ({w.temperature_c}°C)</div>;
}
