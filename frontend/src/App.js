import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");

  const analyzeCode = async () => {
    const res = await fetch("http://127.0.0.1:8000/analyze-code", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({text: input})
    });
    const data = await res.json();
    setResult(data.result);
  };

  const analyzeSpecs = async () => {
    const res = await fetch("http://127.0.0.1:8000/analyze-specs", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({text: input})
    });
    const data = await res.json();
    setResult(data.result);
  };

  return (
    <div style={{padding:"20px"}}>
      <h1>LLM Security Helper</h1>

      <textarea rows="10" cols="60"
        value={input}
        onChange={(e)=>setInput(e.target.value)}
      />

      <br/>

      <button onClick={analyzeCode}>Analyze Code Security</button>
      <button onClick={analyzeSpecs}>Analyze GenAI Specs</button>

      <h3>Result:</h3>
      <pre>{result}</pre>
    </div>
  );
}

export default App;
