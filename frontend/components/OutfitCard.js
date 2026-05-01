export default function OutfitCard({ outfit, onSave }) {
  return (
    <div className="card break-inside-avoid mb-4">
      <img src={outfit.image} alt={outfit.style} className="rounded-xl mb-3" />
      <h3 className="font-semibold capitalize">{outfit.style}</h3>
      <p className="text-sm">{outfit.items.join(', ')}</p>
      <button className="mt-3 bg-pink-400 text-white px-3 py-1 rounded-full" onClick={() => onSave(outfit)}>Save</button>
    </div>
  );
}
