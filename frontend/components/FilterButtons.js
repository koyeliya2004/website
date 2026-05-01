export default function FilterButtons({ title, options, value, onChange }) {
  return <div className="flex gap-2 flex-wrap">{options.map(o => <button key={o} onClick={() => onChange(o)} className={`px-3 py-1 rounded-full border ${value===o?'bg-pink-300':'bg-white'}`}>{o}</button>)}</div>
}
