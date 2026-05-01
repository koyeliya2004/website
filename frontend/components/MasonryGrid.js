export default function MasonryGrid({ children }) {
  return <div className="columns-1 md:columns-2 lg:columns-3 gap-4">{children}</div>;
}
