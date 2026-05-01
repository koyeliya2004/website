import { useState } from 'react';

export default function ImageUploader({ onFile }) {
  const [dragging, setDragging] = useState(false);
  return (
    <div
      className={`card border-2 border-dashed ${dragging ? 'border-pink-400' : 'border-pink-200'}`}
      onDragOver={(e) => { e.preventDefault(); setDragging(true); }}
      onDragLeave={() => setDragging(false)}
      onDrop={(e) => { e.preventDefault(); setDragging(false); onFile(e.dataTransfer.files[0]); }}
    >
      <input type="file" accept="image/*" onChange={(e) => onFile(e.target.files[0])} />
      <p className="text-xs mt-2">Drag & drop or select an image.</p>
    </div>
  );
}
