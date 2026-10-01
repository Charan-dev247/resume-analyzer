import { useState } from "react";
import "./App.css";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeResume = async (e) => {
    e.preventDefault();

    if (!resume || !jobDesc.trim()) {
      setError("Please upload a resume and enter a job description.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_desc", jobDesc);

    try {
      const response = await fetch("http://localhost:5000/api/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Analysis failed");
      }

      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="hero">
        <h1>AI Resume Intelligence</h1>
        <p>
          Analyze your resume against a job description using
          embeddings, semantic search, RAG and LLMs.
        </p>
      </header>

      <main className="container">
        <form onSubmit={analyzeResume} className="analyzer-card">
          <label>Upload Resume (PDF)</label>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setResume(e.target.files[0])}
          />

          <label>Job Description</label>

          <textarea
            value={jobDesc}
            onChange={(e) => setJobDesc(e.target.value)}
            placeholder="Paste the job description here..."
            rows="12"
          />

          <button type="submit" disabled={loading}>
            {loading ? "Analyzing..." : "Analyze Resume"}
          </button>
        </form>

        {error && <div className="error">{error}</div>}

        {result && (
          <section className="results">
            <div className="score-card">
              <h2>AI Match Score</h2>
              <div className="score">
                {result.rag_analysis.match_score}%
              </div>
            </div>

            <div className="comparison">
              <div>
                <h3>AI / RAG Score</h3>
                <strong>
                  {result.rag_analysis.match_score}%
                </strong>
              </div>

              <div>
                <h3>TF-IDF Similarity</h3>
                <strong>{result.tfidf_score}%</strong>
              </div>
            </div>

            <ResultSection
              title="Matching Skills"
              items={result.rag_analysis.matching_skills}
            />

            <ResultSection
              title="Missing Skills"
              items={result.rag_analysis.missing_skills}
            />

            <ResultSection
              title="Relevant Experience"
              items={result.rag_analysis.relevant_experience}
            />

            <ResultSection
              title="Skill Gaps"
              items={result.rag_analysis.skill_gaps}
            />

            <ResultSection
              title="Recommendations"
              items={result.rag_analysis.recommendations}
            />
          </section>
        )}
      </main>
    </div>
  );
}

function ResultSection({ title, items }) {
  return (
    <div className="result-section">
      <h2>{title}</h2>

      <ul>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;