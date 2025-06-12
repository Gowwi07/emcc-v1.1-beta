import { useState, FormEvent } from 'react';

function App() {
  const [message, setMessage] = useState<string>('');
  const [response, setResponse] = useState<string>('');
  const [mode, setMode] = useState<string>('full');
  const [menuOpen, setMenuOpen] = useState<boolean>(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch('http://127.0.0.1:5000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, mode })
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      console.error(err);
      setResponse("Error contacting backend.");
    }
  };

  const handleModeSelect = (selectedMode: string) => {
    setMode(selectedMode);
    setMenuOpen(false);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md relative">

        {/* Three-dot menu */}
        <div className="absolute top-2 right-2">
          <button onClick={() => setMenuOpen(!menuOpen)} className="text-2xl font-bold">⋯</button>
          {menuOpen && (
            <div className="absolute right-0 mt-2 bg-white border rounded shadow">
              <button onClick={() => handleModeSelect('short')} className="block px-4 py-2 hover:bg-gray-200">Short</button>
              <button onClick={() => handleModeSelect('paragraph')} className="block px-4 py-2 hover:bg-gray-200">Paragraph</button>
              <button onClick={() => handleModeSelect('full')} className="block px-4 py-2 hover:bg-gray-200">Full</button>
            </div>
          )}
        </div>

        <h1 className="text-2xl font-bold mb-4">EMCC Chat (TypeScript)</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your question..."
            className="w-full p-2 border rounded mb-4"
          />
          <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
            Ask
          </button>
        </form>
        {response && (
          <div className="mt-4 p-4 bg-gray-200 rounded">
            <strong>Response:</strong> {response}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
