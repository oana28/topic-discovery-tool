import { useState } from "react";

interface IMessage {
  role: "user" | "assistant";
  content: string;
}

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<IMessage[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: IMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: input }),
      });

      const data = await res.json();
      const assistantMessage: IMessage = { role: "assistant", content: data };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Error: could not reach the server." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        maxWidth: 640,
        margin: "40px auto",
        fontFamily: "sans-serif",
        height: 800,
      }}
    >
      <h2 style={{ textAlign: "center", marginBottom: 16 }}>Topic Discovery</h2>

      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
          gap: 10,
          overflowY: "auto",
          padding: 16,
          border: "1px solid lightgrey",
          borderRadius: 8,
          backgroundColor: "white",
        }}
      >
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              maxWidth: 300,
              padding: "10px 14px",
              borderRadius: 12,
              fontSize: 14,
              alignSelf: msg.role === "user" ? "flex-end" : "flex-start",
              backgroundColor: msg.role === "user" ? "lightblue" : "#e1ddddff",
              color: msg.role === "user" ? "white" : "#111",
            }}
          >
            {msg.content}
          </div>
        ))}
        {loading && (
          <div
            style={{
              padding: "10px 14px",
              borderRadius: 12,
              fontSize: 14,
              alignSelf: "flex-start",
              color: "lightgrey",
            }}
          >
            Thinking...
          </div>
        )}
      </div>

      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        <input
          style={{
            flex: 1,
            padding: "10px 14px",
            fontSize: 14,
            border: "1px solid #d1d5db",
            borderRadius: 8,
            outline: "none",
          }}
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="What is your question?"
          disabled={loading}
        />
        <button
          style={{
            padding: "10px 20px",
            fontSize: 14,
            backgroundColor: "lightblue",
            color: "white",
            border: "none",
            borderRadius: 8,
            cursor: "pointer",
          }}
          onClick={sendMessage}
          disabled={loading}
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default App;
